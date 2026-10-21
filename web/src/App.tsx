import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { Home } from './pages/Home';
import { Cartography } from './pages/Cartography';
import { SpatialModel } from './pages/SpatialModel';
import { PolicySimulator } from './pages/PolicySimulator';
import { Forecasting } from './pages/Forecasting';
import { Methodology } from './pages/Methodology';
import rawData from './data/labor_data.json';
import { LaborDataBundle } from './types';

export const App: React.FC = () => {
  const data = rawData as unknown as LaborDataBundle;
  const [currentTab, setCurrentTab] = useState<string>('home');
  const [isDark, setIsDark] = useState<boolean>(true);

  // Sync tab with URL hash if present
  useEffect(() => {
    const handleHash = () => {
      const hash = window.location.hash.replace('#', '');
      if (['home', 'cartography', 'spatial', 'simulator', 'forecasting', 'methodology'].includes(hash)) {
        setCurrentTab(hash);
      }
    };
    handleHash();
    window.addEventListener('hashchange', handleHash);
    return () => window.removeEventListener('hashchange', handleHash);
  }, []);

  const handleTabChange = (tab: string) => {
    setCurrentTab(tab);
    window.location.hash = tab;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    document.documentElement.classList.toggle('dark', isDark);
  }, [isDark]);

  const handleToggleTheme = () => {
    setIsDark((prev) => !prev);
  };

  return (
    <div className={`min-h-screen ${isDark ? 'dark bg-slate-950 text-slate-100' : 'bg-slate-50 text-slate-900'} transition-colors duration-200 flex flex-col justify-between`}>
      <div>
        <Navbar
          currentTab={currentTab}
          onTabChange={handleTabChange}
          isDark={isDark}
          onToggleTheme={handleToggleTheme}
        />

        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-16">
          {currentTab === 'home' && <Home data={data} onNavigate={handleTabChange} />}
          {currentTab === 'cartography' && <Cartography data={data} />}
          {currentTab === 'spatial' && <SpatialModel data={data} />}
          {currentTab === 'simulator' && <PolicySimulator data={data} />}
          {currentTab === 'forecasting' && <Forecasting data={data} />}
          {currentTab === 'methodology' && <Methodology data={data} />}
        </main>
      </div>

      <Footer />
    </div>
  );
};

export default App;
