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
    cyan: 'bg-cyan-500/10 border-cyan-500/30 text-cyan-800 dark:text-cyan-300',
    emerald: 'bg-emerald-500/10 border-emerald-500/30 text-emerald-800 dark:text-emerald-300',
    amber: 'bg-amber-500/10 border-amber-500/30 text-amber-800 dark:text-amber-300',
    rose: 'bg-rose-500/10 border-rose-500/30 text-rose-800 dark:text-rose-300',
    slate: 'bg-card border-border text-foreground'
  };

  const textStyles = {
    cyan: 'text-cyan-700 dark:text-cyan-400',
    emerald: 'text-emerald-700 dark:text-emerald-400',
    amber: 'text-amber-700 dark:text-amber-400',
    rose: 'text-rose-700 dark:text-rose-400',
    slate: 'text-foreground'
  };

  return (
    <div className={`p-4 rounded-xl border transition-all ${variantStyles[variant]}`}>
      <span className="text-[11px] font-sans font-semibold tracking-wider uppercase opacity-85 block mb-1">
        {label}
      </span>
      <div className={`text-2xl font-bold font-mono tracking-tight ${textStyles[variant]}`}>
        {value}
      </div>
      {subtext && (
        <span className="text-xs opacity-75 mt-1 block font-sans">
          {subtext}
        </span>
      )}
    </div>
  );
};
