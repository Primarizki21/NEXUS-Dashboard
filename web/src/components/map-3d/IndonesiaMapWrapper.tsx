'use client';

import React, { Suspense, lazy } from 'react';
import { IndonesiaMapSkeleton } from './IndonesiaMapSkeleton';
import { Compass, Activity, ShieldCheck, Eye } from 'lucide-react';

const IndonesiaMapCanvas = lazy(() => import('./IndonesiaMapCanvas'));

interface IndonesiaMapWrapperProps {
  isDark?: boolean;
}

export const IndonesiaMapWrapper: React.FC<IndonesiaMapWrapperProps> = ({ isDark = true }) => {
  return (
    <div className="relative w-full h-[380px] sm:h-[460px] lg:h-[500px] rounded-2xl border border-border/50 bg-card/25 overflow-hidden select-none transition-colors duration-300">
      {/* Top Tactical Telemetry Bar */}
      <div className="absolute top-3 left-3 sm:top-4 sm:left-4 z-10 flex items-center gap-2 pointer-events-none">
        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 text-[11px] font-mono tracking-wider">
          <span className="w-1.5 h-1.5 rounded-full bg-cyan-500 dark:bg-cyan-400 animate-ping" />
          <span>RADAR AKTIF</span>
        </div>
        <div className="hidden sm:inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-muted/60 border border-border text-muted-foreground text-[11px] font-mono">
          <Activity className="w-3 h-3 text-cyan-500 dark:text-cyan-400" />
          <span>SWEEP: 0.17 Hz</span>
        </div>
      </div>

      {/* Top Right Geolocation Status */}
      <div className="absolute top-3 right-3 sm:top-4 sm:right-4 z-10 flex items-center gap-2 pointer-events-none">
        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-background/80 backdrop-blur-md border border-border text-[11px] font-mono text-muted-foreground shadow-sm">
          <Compass className="w-3.5 h-3.5 text-cyan-500 dark:text-cyan-400" />
          <span className="hidden md:inline">RENTANG: 95° BT — 141° BT</span>
          <span className="md:hidden">38 PROV</span>
        </div>
      </div>

      {/* Main 3D Canvas with Zero-CLS Suspense boundary */}
      <div className="w-full h-full">
        <Suspense fallback={<IndonesiaMapSkeleton />}>
          <IndonesiaMapCanvas isDark={isDark} />
        </Suspense>
      </div>

      {/* Bottom Telemetry & Navigation Hints */}
      <div className="absolute bottom-3 left-3 right-3 sm:bottom-4 sm:left-4 sm:right-4 z-10 flex items-center justify-between pointer-events-none">
        <div className="inline-flex items-center gap-1.5 text-[11px] font-mono text-muted-foreground bg-background/70 backdrop-blur-md px-2.5 py-1 rounded-md border border-border/40">
          <ShieldCheck className="w-3.5 h-3.5 text-emerald-500 dark:text-emerald-400" />
          <span>8.611 Titik Teritorial Kepulauan</span>
        </div>

        <div className="inline-flex items-center gap-1.5 text-[11px] font-mono text-muted-foreground bg-background/70 backdrop-blur-md px-2.5 py-1 rounded-md border border-border/40">
          <Eye className="w-3.5 h-3.5 text-cyan-500 dark:text-cyan-400" />
          <span className="hidden sm:inline">Geser untuk rotasi sudut pandang</span>
          <span className="sm:hidden">Rotasi 3D</span>
        </div>
      </div>
    </div>
  );
};

export default IndonesiaMapWrapper;
