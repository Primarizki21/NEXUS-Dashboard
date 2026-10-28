import React from 'react';
import { Database, ShieldCheck, Cpu } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-border bg-card/60 py-12 px-4 sm:px-6 lg:px-8 mt-20 text-muted-foreground text-xs">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <div className="flex items-center space-x-2 text-foreground font-bold text-sm mb-2">
            <span className="w-2 h-2 rounded-full bg-cyan-500"></span>
            <span>ACTION 2026 : ANALISIS KETENAGAKERJAAN</span>
          </div>
          <p className="text-muted-foreground leading-relaxed">
            Platform kompanion interaktif analisis statistik dan ekonometrika spasial pasar tenaga kerja Indonesia untuk pemerataan kesempatan kerja menuju target RPJMN 2029.
          </p>
        </div>

        <div>
          <h4 className="text-foreground font-semibold text-xs tracking-wider uppercase mb-3 flex items-center space-x-1.5">
            <Database className="w-3.5 h-3.5 text-cyan-600 dark:text-cyan-400" />
            <span>Integritas Sumber Data</span>
          </h4>
          <ul className="space-y-1.5 text-muted-foreground">
            <li>Badan Pusat Statistik (BPS) Republik Indonesia</li>
            <li>Survei Angkatan Kerja Nasional (Sakernas 2017-2024)</li>
            <li>Indikator Pasar Tenaga Kerja Indonesia (Agustus 2024)</li>
            <li>Panel Seimbang 34 Provinsi + Potret Penuh 38 Provinsi</li>
          </ul>
        </div>

        <div>
          <h4 className="text-foreground font-semibold text-xs tracking-wider uppercase mb-3 flex items-center space-x-1.5">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            <span>Metodologi Terverifikasi</span>
          </h4>
          <p className="text-muted-foreground leading-relaxed mb-2">
            Estimasi model Spatial Durbin Model (SDM) dengan pembobotan k-NN (k=4) dan validasi silang walk-forward peramalan bebas bocor.
          </p>
          <div className="inline-flex items-center space-x-1 px-2.5 py-1 rounded bg-muted/60 border border-border text-foreground font-mono text-2xs">
            <Cpu className="w-3 h-3 text-cyan-600 dark:text-cyan-400" />
            <span>Zero Synthetic Imputation : 100% Verified</span>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto border-t border-border mt-8 pt-6 flex flex-col sm:flex-row justify-between items-center text-muted-foreground">
        <p>&copy; 2026 Tim Peneliti Analisis Data ACTION. Hak cipta dilindungi.</p>
        <p className="mt-2 sm:mt-0 font-mono text-2xs text-muted-foreground">
          Subtema: Turning Insight into Opportunity
        </p>
      </div>
    </footer>
  );
};
