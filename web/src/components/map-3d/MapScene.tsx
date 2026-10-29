import React, { useState, useCallback } from 'react';
import { OrbitControls } from '@react-three/drei';
import { IslandPoints } from './IslandPoints';
import { ScannerBeam } from './ScannerBeam';
import { RadarGrid } from './RadarGrid';

interface MapSceneProps {
  isDark: boolean;
}

export const MapScene: React.FC<MapSceneProps> = ({ isDark }) => {
  const [scanState, setScanState] = useState<{ scanX: number; isPaused: boolean }>({
    scanX: 10.2,
    isPaused: false,
  });

  const handleScanUpdate = useCallback((scanX: number, isPaused: boolean) => {
    setScanState({ scanX, isPaused });
  }, []);

  return (
    <>
      {/* Gentle ambient and directional lights */}
      <ambientLight intensity={isDark ? 0.4 : 0.7} />
      <directionalLight position={[0, 10, 15]} intensity={isDark ? 0.8 : 1.2} />

      {/* Camera Controls with damping and safe rotation boundaries */}
      <OrbitControls
        enableZoom={false}
        enablePan={false}
        enableDamping={true}
        dampingFactor={0.08}
        rotateSpeed={0.4}
        maxPolarAngle={Math.PI / 2.1}
        minPolarAngle={Math.PI / 3.8}
        maxAzimuthAngle={Math.PI / 5}
        minAzimuthAngle={-Math.PI / 5}
      />

      {/* Main 3D archipelago and radar elements */}
      <group position={[0, -0.2, 0]} rotation={[-0.22, 0, 0]}>
        {/* Background Radar Range Rings */}
        <RadarGrid isDark={isDark} />

        {/* 3D Holographic Island Point Cloud */}
        <IslandPoints isDark={isDark} onScanUpdate={handleScanUpdate} />

        {/* Radar Scanning Laser Beam */}
        <ScannerBeam
          isDark={isDark}
          scanX={scanState.scanX}
          isPaused={scanState.isPaused}
        />
      </group>
    </>
  );
};
