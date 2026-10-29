import React, { useMemo, useEffect, useRef } from 'react';
import * as THREE from 'three';
import { useFrame } from '@react-three/fiber';
import pointData from '../../data/indonesia_points.json';
import { createRadarScanMaterial } from './shaders';

interface IslandPointsProps {
  isDark: boolean;
  onScanUpdate?: (scanX: number, isPaused: boolean) => void;
}

const X_MAX = 10.2;
const X_MIN = -10.2;
const SCAN_DURATION = 2.4; // seconds to travel from one side to the other
const PAUSE_DURATION = 0.5; // seconds to pause at each end

export const IslandPoints: React.FC<IslandPointsProps> = ({ isDark, onScanUpdate }) => {
  const pointsRef = useRef<THREE.Points>(null);

  // Buffer Geometry initialization
  const geometry = useMemo(() => {
    const geom = new THREE.BufferGeometry();
    const positions = new Float32Array(pointData.positions);
    const types = new Float32Array(pointData.types);

    geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geom.setAttribute('aType', new THREE.BufferAttribute(types, 1));
    geom.computeBoundingBox();
    return geom;
  }, []);

  // Material initialization
  const material = useMemo(() => {
    return createRadarScanMaterial(isDark);
  }, []);

  // Disposal on unmount
  useEffect(() => {
    return () => {
      geometry.dispose();
      material.dispose();
    };
  }, [geometry, material]);

  // Ping-pong State Machine refs
  // Phase 0: Scan Left (X_MAX -> X_MIN)
  // Phase 1: Pause Left (0.5s)
  // Phase 2: Scan Right (X_MIN -> X_MAX)
  // Phase 3: Pause Right (0.5s)
  const stateRef = useRef({
    phase: 0,
    timer: 0,
    scanX: X_MAX,
    direction: -1.0,
    intensity: 1.0,
    isPaused: false,
  });

  useFrame((state, delta) => {
    const s = stateRef.current;
    s.timer += delta;

    if (s.phase === 0) {
      // Moving Right to Left
      const progress = Math.min(s.timer / SCAN_DURATION, 1.0);
      // Smooth smoothstep movement
      const ease = progress * progress * (3 - 2 * progress);
      s.scanX = X_MAX - (X_MAX - X_MIN) * ease;
      s.direction = -1.0;
      s.intensity = 1.0;
      s.isPaused = false;

      if (progress >= 1.0) {
        s.phase = 1;
        s.timer = 0;
        s.scanX = X_MIN;
        s.isPaused = true;
      }
    } else if (s.phase === 1) {
      // Pause at Left boundary for exactly 0.5s
      s.scanX = X_MIN;
      s.isPaused = true;
      // Soft fade of scan intensity while resting
      s.intensity = Math.max(0.3, 1.0 - (s.timer / PAUSE_DURATION) * 0.7);

      if (s.timer >= PAUSE_DURATION) {
        s.phase = 2;
        s.timer = 0;
        s.isPaused = false;
      }
    } else if (s.phase === 2) {
      // Moving Left to Right
      const progress = Math.min(s.timer / SCAN_DURATION, 1.0);
      const ease = progress * progress * (3 - 2 * progress);
      s.scanX = X_MIN + (X_MAX - X_MIN) * ease;
      s.direction = 1.0;
      s.intensity = 1.0;
      s.isPaused = false;

      if (progress >= 1.0) {
        s.phase = 3;
        s.timer = 0;
        s.scanX = X_MAX;
        s.isPaused = true;
      }
    } else if (s.phase === 3) {
      // Pause at Right boundary for exactly 0.5s
      s.scanX = X_MAX;
      s.isPaused = true;
      s.intensity = Math.max(0.3, 1.0 - (s.timer / PAUSE_DURATION) * 0.7);

      if (s.timer >= PAUSE_DURATION) {
        s.phase = 0;
        s.timer = 0;
        s.isPaused = false;
      }
    }

    // Update material uniforms
    material.uniforms.uTime.value = state.clock.elapsedTime;
    material.uniforms.uScanX.value = s.scanX;
    material.uniforms.uDirection.value = s.direction;
    material.uniforms.uScanIntensity.value = s.intensity;

    // Theme color smooth lerping without canvas remount
    const targetBase = isDark ? new THREE.Color('#334155') : new THREE.Color('#94a3b8');
    const targetGlow = isDark ? new THREE.Color('#06b6d4') : new THREE.Color('#0284c7');
    const targetOpacity = isDark ? 0.45 : 0.6;

    material.uniforms.uBaseColor.value.lerp(targetBase, delta * 4.0);
    material.uniforms.uScanGlowColor.value.lerp(targetGlow, delta * 4.0);
    material.uniforms.uBaseOpacity.value = THREE.MathUtils.lerp(
      material.uniforms.uBaseOpacity.value,
      targetOpacity,
      delta * 4.0
    );

    // Subtle gentle floating tilt on the whole archipelago
    if (pointsRef.current) {
      pointsRef.current.rotation.z = Math.sin(state.clock.elapsedTime * 0.4) * 0.012;
      pointsRef.current.position.y = Math.sin(state.clock.elapsedTime * 0.7) * 0.04;
    }

    if (onScanUpdate) {
      onScanUpdate(s.scanX, s.isPaused);
    }
  });

  return (
    <points ref={pointsRef} geometry={geometry}>
      <primitive object={material} attach="material" />
    </points>
  );
};
