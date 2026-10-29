import React from 'react';
import { Canvas } from '@react-three/fiber';
import { MapScene } from './MapScene';

interface IndonesiaMapCanvasProps {
  isDark: boolean;
}

export const IndonesiaMapCanvas: React.FC<IndonesiaMapCanvasProps> = ({ isDark }) => {
  return (
    <Canvas
      dpr={[1, 1.75]}
      camera={{ position: [0, -0.6, 15.8], fov: 42 }}
      gl={{
        powerPreference: 'high-performance',
        antialias: true,
        alpha: true,
      }}
      onCreated={({ gl }) => {
        gl.setClearColor(0x000000, 0);
      }}
      className="w-full h-full cursor-grab active:cursor-grabbing"
    >
      <MapScene isDark={isDark} />
    </Canvas>
  );
};

export default IndonesiaMapCanvas;
