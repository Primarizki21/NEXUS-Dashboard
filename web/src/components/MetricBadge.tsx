import React from 'react';

interface MetricBadgeProps {
  label: string;
  value: string | number;
  subtext?: string;
  variant?: 'cyan' | 'emerald' | 'amber' | 'rose' | 'slate';
}

export const MetricBadge: React.FC<MetricBadgeProps> = ({
  label,
  value,
  subtext,
  variant = 'cyan'
}) => {
  const variantStyles = {
    cyan: 'bg-cyan-950/40 border-cyan-800/60 text-cyan-400',
    emerald: 'bg-emerald-950/40 border-emerald-800/60 text-emerald-400',
    amber: 'bg-amber-950/40 border-amber-800/60 text-amber-400',
    rose: 'bg-rose-950/40 border-rose-800/60 text-rose-400',
    slate: 'bg-slate-900 border-slate-800 text-slate-300'
  };

  const textStyles = {
    cyan: 'text-cyan-400',
    emerald: 'text-emerald-400',
    amber: 'text-amber-400',
    rose: 'text-rose-400',
    slate: 'text-slate-200'
  };

  return (
    <div className={`p-4 rounded-xl border transition-all ${variantStyles[variant]}`}>
      <span className="text-xs font-mono tracking-wider uppercase opacity-75 block mb-1">
        {label}
      </span>
      <div className={`text-2xl font-bold font-mono tracking-tight ${textStyles[variant]}`}>
        {value}
      </div>
      {subtext && (
        <span className="text-xs opacity-70 mt-1 block">
          {subtext}
        </span>
      )}
    </div>
  );
};
