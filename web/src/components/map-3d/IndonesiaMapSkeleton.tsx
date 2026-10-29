import React from 'react';
import { Radio } from 'lucide-react';

export const IndonesiaMapSkeleton: React.FC = () => {
  return (
    <div className="w-full h-full min-h-[380px] sm:min-h-[460px] lg:min-h-[500px] relative overflow-hidden rounded-2xl border border-border/40 bg-card/20 backdrop-blur-sm flex flex-col items-center justify-center p-6 select-none">
      {/* Background Radar Rings Placeholder */}
      <div className="absolute inset-0 flex items-center justify-center pointer-events-none opacity-25">
        <div className="w-96 h-48 border border-border/60 rounded-[100%] animate-pulse" />
        <div className="absolute w-[540px] h-[270px] border border-border/40 rounded-[100%]" />
        <div className="absolute w-[720px] h-[360px] border border-border/20 rounded-[100%]" />
        <div className="absolute w-full h-[1px] bg-border/40" />
        <div className="absolute h-full w-[1px] bg-border/40" />
      </div>

      {/* Loading Indicator */}
      <div className="relative z-10 flex flex-col items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-500 dark:text-cyan-400 animate-spin">
          <Radio className="w-5 h-5 animate-pulse" />
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-xs font-mono font-medium tracking-widest text-foreground uppercase">
            Inisialisasi Sistem Radar 3D
          </span>
          <span className="text-[11px] font-mono text-muted-foreground mt-0.5">
            Sinkronisasi 8.611 Titik Teritorial Kepulauan RI...
          </span>
        </div>
      </div>
    </div>
  );
};
