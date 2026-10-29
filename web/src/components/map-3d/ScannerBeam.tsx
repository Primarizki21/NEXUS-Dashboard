import React, { useMemo, useEffect, useRef } from 'react';
import * as THREE from 'three';
import { useFrame } from '@react-three/fiber';
import { createScannerBeamMaterial } from './shaders';

interface ScannerBeamProps {
  isDark: boolean;
  scanX: number;
  isPaused: boolean;
}

export const ScannerBeam: React.FC<ScannerBeamProps> = ({ isDark, scanX, isPaused }) => {
  const meshRef = useRef<THREE.Mesh>(null);

  const material = useMemo(() => {
    return createScannerBeamMaterial(isDark);
  }, []);

  useEffect(() => {
    return () => {
      material.dispose();
    };
  }, [material]);

  useFrame((state, delta) => {
    if (!meshRef.current) return;

    // Follow scanX directly
    meshRef.current.position.x = scanX;

    // Update material uniform time
    material.uniforms.uTime.value = state.clock.elapsedTime;

    // Color lerp based on theme
    const targetColor = isDark ? new THREE.Color('#06b6d4') : new THREE.Color('#0284c7');
    material.uniforms.uColor.value.lerp(targetColor, delta * 4.0);

    // Fade when paused at boundary
    const targetOpacity = (isPaused ? 0.25 : 0.8) * (isDark ? 0.85 : 0.65);
    material.uniforms.uOpacity.value = THREE.MathUtils.lerp(
      material.uniforms.uOpacity.value,
      targetOpacity,
      delta * 5.0
    );
  });

  return (
    <mesh ref={meshRef} position={[scanX, 0, 0.05]}>
      {/* 0.7 units wide beam spanning Y [-4.8, 4.8] */}
      <planeGeometry args={[0.7, 9.6]} />
      <primitive object={material} attach="material" />
    </mesh>
  );
};
