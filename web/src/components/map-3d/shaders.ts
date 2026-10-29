import * as THREE from 'three';

export interface ScanShaderUniforms {
  uTime: { value: number };
  uScanX: { value: number };
  uDirection: { value: number };
  uScanIntensity: { value: number };
  uBeamWidth: { value: number };
  uTrailDecay: { value: number };
  uBaseColor: { value: THREE.Color };
  uScanGlowColor: { value: THREE.Color };
  uBaseOpacity: { value: number };
  uPointSize: { value: number };
}

export const createRadarScanMaterial = (isDark: boolean = true): THREE.ShaderMaterial => {
  const baseColor = isDark ? new THREE.Color('#334155') : new THREE.Color('#94a3b8');
  const glowColor = isDark ? new THREE.Color('#06b6d4') : new THREE.Color('#0284c7');

  return new THREE.ShaderMaterial({
    transparent: true,
    depthWrite: false,
    blending: THREE.NormalBlending,
    uniforms: {
      uTime: { value: 0 },
      uScanX: { value: 12.0 },
      uDirection: { value: -1.0 },
      uScanIntensity: { value: 1.0 },
      uBeamWidth: { value: 0.9 },
      uTrailDecay: { value: 3.5 },
      uBaseColor: { value: baseColor },
      uScanGlowColor: { value: glowColor },
      uBaseOpacity: { value: isDark ? 0.35 : 0.5 },
      uPointSize: { value: 2.4 },
    },
    vertexShader: /* glsl */ `
      uniform float uTime;
      uniform float uScanX;
      uniform float uDirection;
      uniform float uBeamWidth;
      uniform float uTrailDecay;
      uniform float uPointSize;

      attribute float aType;

      varying vec3 vWorldPosition;
      varying float vType;
      varying float vScanIntensity;

      void main() {
        vType = aType;

        vec4 worldPos = modelMatrix * vec4(position, 1.0);
        vWorldPosition = worldPos.xyz;

        // Proximity to radar beam
        float d = worldPos.x - uScanX;
        float beam = exp(-(d * d) / (2.0 * uBeamWidth * uBeamWidth));
        float trailDist = -d * uDirection;
        float trail = (trailDist > 0.0) ? exp(-trailDist / uTrailDecay) : 0.0;
        vScanIntensity = clamp(beam * 1.5 + trail * 0.75, 0.0, 1.0);

        vec4 mvPosition = viewMatrix * worldPos;
        gl_Position = projectionMatrix * mvPosition;

        // Coastlines are slightly sharper, and pulse gently when scanned
        float sizeMultiplier = (aType > 0.5) ? 1.25 : 0.95;
        float pulseMultiplier = 1.0 + vScanIntensity * 0.6;

        // Moderate distance attenuation so points stay crisp
        gl_PointSize = uPointSize * sizeMultiplier * pulseMultiplier * (18.0 / -mvPosition.z);
      }
    `,
    fragmentShader: /* glsl */ `
      uniform float uTime;
      uniform float uScanX;
      uniform float uDirection;
      uniform float uScanIntensity;
      uniform vec3 uBaseColor;
      uniform vec3 uScanGlowColor;
      uniform float uBaseOpacity;

      varying vec3 vWorldPosition;
      varying float vType;
      varying float vScanIntensity;

      void main() {
        // Crisp circular dot
        vec2 coord = gl_PointCoord - vec2(0.5);
        float dist = length(coord);
        if (dist > 0.5) discard;
        float circleAlpha = smoothstep(0.5, 0.28, dist);

        // Holographic breathing pulse
        float breath = sin(uTime * 1.5 + vWorldPosition.x * 0.35) * 0.08 + 0.92;

        // Color transition between baseline and radar scan glow
        vec3 col = mix(uBaseColor * breath, uScanGlowColor, vScanIntensity * uScanIntensity);

        // Alpha calculation
        float typeAlpha = (vType > 0.5) ? 1.0 : 0.7;
        float alpha = mix(uBaseOpacity * typeAlpha, 0.98, vScanIntensity * uScanIntensity) * circleAlpha;

        gl_FragColor = vec4(col, alpha);

        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }
    `,
  });
};

export const createScannerBeamMaterial = (isDark: boolean = true): THREE.ShaderMaterial => {
  const glowColor = isDark ? new THREE.Color('#22d3ee') : new THREE.Color('#0284c7');

  return new THREE.ShaderMaterial({
    transparent: true,
    depthWrite: false,
    side: THREE.DoubleSide,
    blending: THREE.NormalBlending,
    uniforms: {
      uColor: { value: glowColor },
      uOpacity: { value: isDark ? 0.75 : 0.6 },
      uTime: { value: 0 },
    },
    vertexShader: /* glsl */ `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: /* glsl */ `
      uniform vec3 uColor;
      uniform float uOpacity;
      uniform float uTime;
      varying vec2 vUv;

      void main() {
        // Vertical laser beam with soft Gaussian horizontal profile
        float core = exp(-pow((vUv.x - 0.5) * 7.5, 2.0));
        // Vertical fade at top and bottom edges
        float fadeY = smoothstep(0.0, 0.12, vUv.y) * smoothstep(1.0, 0.88, vUv.y);
        // Subtle high-tech flicker
        float flicker = 0.95 + 0.05 * sin(uTime * 12.0);

        float alpha = core * fadeY * uOpacity * flicker;
        if (alpha < 0.005) discard;

        gl_FragColor = vec4(uColor, alpha);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }
    `,
  });
};
