import React, { useMemo } from 'react';
import * as THREE from 'three';
import { useFrame } from '@react-three/fiber';

interface RadarGridProps {
  isDark: boolean;
}

export const RadarGrid: React.FC<RadarGridProps> = ({ isDark }) => {
  const lineMaterial = useMemo(() => {
    return new THREE.LineBasicMaterial({
      color: isDark ? new THREE.Color('#334155') : new THREE.Color('#cbd5e1'),
      transparent: true,
      opacity: isDark ? 0.22 : 0.35,
      depthWrite: false,
    });
  }, []);

  useFrame((_, delta) => {
    const targetColor = isDark ? new THREE.Color('#334155') : new THREE.Color('#cbd5e1');
    lineMaterial.color.lerp(targetColor, delta * 4.0);
    lineMaterial.opacity = THREE.MathUtils.lerp(lineMaterial.opacity, isDark ? 0.22 : 0.35, delta * 4.0);
  });

  // Concentric radar circles
  const circleGeometries = useMemo(() => {
    const radii = [4.5, 7.5, 10.5];
    return radii.map((r) => {
      const pts: THREE.Vector3[] = [];
      const segments = 64;
      for (let i = 0; i <= segments; i++) {
        const theta = (i / segments) * Math.PI * 2;
        pts.push(new THREE.Vector3(Math.cos(theta) * r, Math.sin(theta) * (r * 0.42), -0.15));
      }
      return new THREE.BufferGeometry().setFromPoints(pts);
    });
  }, []);

  // Axis grid lines
  const axisGeometry = useMemo(() => {
    const pts: THREE.Vector3[] = [
      new THREE.Vector3(-11, 0, -0.15),
      new THREE.Vector3(11, 0, -0.15),
      new THREE.Vector3(0, -4.5, -0.15),
      new THREE.Vector3(0, 4.5, -0.15),
    ];
    return new THREE.BufferGeometry().setFromPoints(pts);
  }, []);

  return (
    <group position={[0, 0, 0]}>
      {circleGeometries.map((geom, idx) => (
        <primitive key={idx} object={new THREE.Line(geom, lineMaterial)} />
      ))}
      <primitive object={new THREE.LineSegments(axisGeometry, lineMaterial)} />
    </group>
  );
};
