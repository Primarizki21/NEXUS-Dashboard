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
  Compass,
  Sparkles
} from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';
import { cn } from '@/lib/utils';

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
    { id: 'innovations', label: 'Inovasi', icon: Sparkles, badge: 'Fitur Kunci' },
    { id: 'forecasting', label: 'Proyeksi', icon: TrendingUp, badge: '2025-2030' },
    { id: 'methodology', label: 'Metodologi', icon: FileText, badge: 'Audit Data' },
  ];

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/80 bg-background/95 backdrop-blur-md transition-colors duration-200">
      {/* Contextual Analytical Strip (Sub-bar) */}
      <div className="border-b border-border/40 bg-muted/40 px-4 py-1 text-xs text-muted-foreground transition-colors">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-2 font-mono text-[11px]">
            <span className="size-2 rounded-full bg-emerald-500 ring-2 ring-emerald-500/20" />
            <span className="font-semibold text-foreground">ACTION 2026 Data Engine</span>
            <span className="text-border">|</span>
            <span>Sakernas BPS 2024 • 38 Provinsi</span>
          </div>
          <div className="hidden md:flex items-center gap-3 font-mono text-[11px]">
            <span>Model: <strong className="text-foreground font-medium">SDM Panel (k=4)</strong></span>
            <span className="text-border">|</span>
            <span>Moran's I: <strong className="text-emerald-500 font-medium">+0.246</strong></span>
            <span className="text-border">|</span>
            <span>Pseudo-R²: <strong className="text-cyan-500 font-medium">0.547</strong></span>
          </div>
        </div>
      </div>

      {/* Main Navigation Bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between gap-4">
          
          {/* Brand Left */}
          <div 
            className="flex items-center gap-3 cursor-pointer select-none group" 
            onClick={() => onTabChange('home')}
          >
            <div className="flex size-9 shrink-0 items-center justify-center rounded-lg bg-primary text-primary-foreground shadow-sm transition-transform group-hover:scale-105">
              <Compass className="size-5" />
            </div>
            <div className="flex flex-col">
              <div className="flex items-center gap-2">
                <span className="font-bold text-base tracking-tight text-foreground sm:text-lg">
                  ACTION 2026
                </span>
                <Badge variant="secondary" className="text-[10px] font-mono px-1.5 py-0">
                  Web Companion
                </Badge>
              </div>
              <p className="text-[11px] text-muted-foreground hidden sm:block truncate max-w-[240px] xl:max-w-none">
                Turning Insight into Opportunity
              </p>
            </div>
          </div>

          {/* Desktop Nav Items */}
          <nav className="hidden lg:flex items-center gap-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = currentTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className={cn(
                    "flex items-center gap-2 px-3.5 py-2 rounded-md text-xs font-medium transition-all",
                    isActive
                      ? "bg-primary/10 text-primary border border-primary/20 shadow-xs font-semibold"
                      : "text-muted-foreground hover:text-foreground hover:bg-muted"
                  )}
                >
                  <Icon className="size-4 shrink-0" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </nav>

          {/* Right Controls */}
          <div className="flex items-center gap-2 shrink-0">
            {/* Theme Toggle */}
            <Button
              variant="outline"
              size="icon"
              onClick={onToggleTheme}
              aria-label="Toggle theme mode"
              className="size-9 rounded-md border-border text-foreground hover:bg-muted"
            >
              {isDark ? (
                <Sun className="size-4 text-amber-400" />
              ) : (
                <Moon className="size-4 text-cyan-600" />
              )}
            </Button>

            {/* Mobile Sheet Menu */}
            <div className="lg:hidden">
              <Sheet open={mobileMenuOpen} onOpenChange={setMobileMenuOpen}>
                <SheetTrigger asChild>
                  <Button
                    variant="outline"
                    size="icon"
                    aria-label="Open mobile menu"
                    className="size-9 rounded-md border-border text-foreground hover:bg-muted"
                  >
                    <Menu className="size-4" />
                  </Button>
                </SheetTrigger>
                <SheetContent side="right" className="w-[300px] sm:w-[360px] p-6 flex flex-col justify-between">
                  <div className="flex flex-col gap-6">
                    <SheetHeader className="text-left">
                      <div className="flex items-center gap-3">
                        <div className="flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                          <Compass className="size-4" />
                        </div>
                        <div>
                          <SheetTitle className="text-base font-bold">ACTION 2026</SheetTitle>
                          <p className="text-xs text-muted-foreground">Turning Insight into Opportunity</p>
                        </div>
                      </div>
                    </SheetHeader>

                    {/* Nav Items in Sheet */}
                    <div className="flex flex-col gap-1.5">
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
                            className={cn(
                              "w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-all",
                              isActive
                                 ? "bg-primary/15 text-primary font-semibold border border-primary/25"
                                 : "text-muted-foreground hover:text-foreground hover:bg-muted font-medium"
                             )}
                           >
                             <div className="flex items-center gap-3">
                               <Icon className="size-4 shrink-0" />
                               <span>{item.label}</span>
                             </div>
                             <span className="text-[11px] px-2 py-0.5 rounded bg-muted text-muted-foreground font-mono">
                               {item.badge}
                             </span>
                           </button>
                         );
                       })}
                     </div>
                   </div>

                   {/* Drawer Footer Info */}
                   <div className="border-t border-border pt-4 text-xs font-mono text-muted-foreground flex flex-col gap-1.5">
                     <div className="flex justify-between items-center">
                       <span>Sumber:</span>
                       <span className="text-foreground">Sakernas BPS 2024</span>
                     </div>
                     <div className="flex justify-between items-center">
                       <span>Metodologi:</span>
                       <span className="text-emerald-500 font-semibold">SDM Panel (k=4)</span>
                     </div>
                     <div className="flex justify-between items-center">
                       <span>Moran's I:</span>
                       <span className="text-emerald-500">+0.246 (p=0.003)</span>
                     </div>
                   </div>
                 </SheetContent>
               </Sheet>
             </div>
           </div>

         </div>
       </div>
     </header>
   );
 };
