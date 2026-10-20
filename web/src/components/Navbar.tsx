import React, { useState } from 'react';
import { 
  BarChart3, 
  Map, 
  GitFork, 
  Sliders, 
  TrendingUp, 
  FileText, 
  Sun, 
  Moon, 
  Menu, 
  X,
  Compass
} from 'lucide-react';

interface NavbarProps {
  currentTab: string;
  onTabChange: (tab: string) => void;
  isDark: boolean;
  onToggleTheme: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentTab,
  onTabChange,
  isDark,
  onToggleTheme,
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { id: 'home', label: 'Beranda', icon: BarChart3, badge: 'Paradoks' },
    { id: 'cartography', label: 'Kartografi', icon: Map, badge: '3 Klaster' },
    { id: 'spatial', label: 'Ekonometrika', icon: GitFork, badge: 'LeSage-Pace' },
    { id: 'simulator', label: 'Simulator', icon: Sliders, badge: 'RPJMN 2029' },
    { id: 'forecasting', label: 'Proyeksi', icon: TrendingUp, badge: '2025-2030' },
    { id: 'methodology', label: 'Metodologi', icon: FileText, badge: 'Audit' },
  ];

  return (
    <header className="sticky top-0 z-50 backdrop-blur-md bg-slate-950/80 border-b border-slate-800 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Subtitle */}
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => onTabChange('home')}>
            <div className="w-9 h-9 rounded-lg bg-gradient-to-tr from-cyan-600 to-blue-500 flex items-center justify-center text-white shadow-lg shadow-cyan-500/20">
              <Compass className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-bold text-lg tracking-tight text-white">ACTION 2026</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-cyan-950/80 text-cyan-400 border border-cyan-800 font-mono">
                  GRAIN-Adapted
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                Turning Insight into Opportunity : Sakernas BPS
              </p>
            </div>
          </div>

          {/* Model Telemetry Pill (Desktop) */}
          <div className="hidden xl:flex items-center space-x-2 px-3 py-1 rounded-full bg-slate-900 border border-slate-800 text-xs font-mono text-slate-300">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span className="text-slate-400">Model:</span>
            <span className="text-cyan-400 font-semibold">SDM Panel</span>
            <span className="text-slate-600">|</span>
            <span className="text-slate-400">Moran:</span>
            <span className="text-emerald-400">+0.246</span>
            <span className="text-slate-600">|</span>
            <span className="text-slate-400">Pseudo-R²:</span>
            <span className="text-amber-400">0.547</span>
          </div>

          {/* Desktop Nav Items */}
          <nav className="hidden md:flex items-center space-x-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = currentTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className={`flex items-center space-x-1.5 px-3 py-2 rounded-lg text-xs font-medium transition-all ${
                    isActive
                      ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 shadow-sm'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </nav>

          {/* Right Controls */}
          <div className="flex items-center space-x-2">
            <button
              onClick={onToggleTheme}
              aria-label="Toggle theme mode"
              className="p-2 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-900 border border-slate-800 transition-colors"
            >
              {isDark ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-cyan-400" />}
            </button>

            {/* Mobile menu trigger */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-label="Open mobile menu"
              className="md:hidden p-2 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-900 border border-slate-800"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-slate-800 bg-slate-950/95 px-4 pt-2 pb-4 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = currentTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => {
                  onTabChange(item.id);
                  setMobileMenuOpen(false);
                }}
                className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
                }`}
              >
                <div className="flex items-center space-x-3">
                  <Icon className="w-4 h-4" />
                  <span>{item.label}</span>
                </div>
                <span className="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400 font-mono">
                  {item.badge}
                </span>
              </button>
            );
          })}
        </div>
      )}
    </header>
  );
};
