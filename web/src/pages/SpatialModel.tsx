import React from 'react';
import { 
  CheckCircle2, 
  Activity
} from 'lucide-react';
import { LaborDataBundle } from '../types';
import { MetricBadge } from '../components/MetricBadge';

interface SpatialModelProps {
  data: LaborDataBundle;
}

export const SpatialModel: React.FC<SpatialModelProps> = ({ data }) => {
  const { spatial_models, lesage_pace, moran_trajectory } = data;

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Header */}
      <div className="border-b border-border pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-600 dark:text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-600 dark:bg-cyan-400"></span>
            <span>MODUL 2 : ADVANCED SPATIAL ECONOMETRICS</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-foreground tracking-tight">
            Ekonometrika Spasial & Limpahan Antardaerah
          </h1>
          <p className="text-sm text-muted-foreground mt-1 max-w-2xl">
            Spatial Durbin Model (SDM) membuktikan bahwa tingkat pengangguran suatu provinsi tidak berdiri sendiri, melainkan dipengaruhi kuat oleh tarikan upah dan limpahan pencari kerja dari provinsi tetangga.
          </p>
        </div>

        {/* Micro Benchmarks */}
        <div className="flex flex-wrap gap-2 text-xs font-mono">
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Model:</span> <strong className="text-cyan-600 dark:text-cyan-400">SDM Panel (k=4)</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Pseudo-R²:</span> <strong className="text-emerald-600 dark:text-emerald-400">0.547 (+15.6%)</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Moran's I 2024:</span> <strong className="text-amber-600 dark:text-amber-400">+0.246 (p=0.012)</strong>
          </div>
        </div>
      </div>

      {/* Top Benchmark Callout Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricBadge
          label="Moran's I Autokorelasi"
          value="+0.2457"
          subtext="E(I) = -0.0303 (Signifikan, p=0.012)"
          variant="cyan"
        />
        <MetricBadge
          label="Lonjakan R² Model SDM"
          value="0.547"
          subtext="Meningkat tajam dari OLS (0.391)"
          variant="emerald"
        />
        <MetricBadge
          label="Limpahan Spasial Upah"
          value="+4.4313"
          subtext="Efek tumpahan ke tetangga (LeSage-Pace)"
          variant="amber"
        />
        <MetricBadge
          label="Limpahan Rasio Mismatch"
          value="+0.9019"
          subtext="Mobilitas tenaga kerja vokasi & sarjana"
          variant="rose"
        />
      </div>

      {/* LeSage-Pace Effect Decomposition Section */}
      <section className="p-6 rounded-2xl bg-card border border-border space-y-6 shadow-xs">
        <div className="border-b border-border pb-4">
          <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block mb-1">
            Dekomposisi Efek LeSage-Pace (Spatial Durbin Model)
          </span>
          <h2 className="text-xl font-bold text-foreground tracking-tight">
            Pemisahan Dampak Domestik Langsung vs Limpahan Spasial Antarwilayah
          </h2>
          <p className="text-xs text-muted-foreground mt-1">
            Persamaan: $S_r(W) = (I_N - \rho W)^{'{'}-1{'}'} (\beta_r I_N + \theta_r W)$. Mengukur seberapa besar kebijakan di satu provinsi berdampak ke provinsi sekitarnya.
          </p>
        </div>

        {/* Visual Bar Breakdown */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {lesage_pace.map((item) => {
            const isWage = item.variable.includes('Upah');
            return (
              <div
                key={item.variable}
                className={`p-5 rounded-xl border relative overflow-hidden flex flex-col justify-between ${
                  isWage
                    ? 'bg-cyan-500/10 border-cyan-500/50 ring-1 ring-cyan-500/30'
                    : 'bg-muted/30 border-border'
                }`}
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-bold text-sm text-foreground">{item.variable}</span>
                    {isWage && (
                      <span className="px-2 py-0.5 rounded text-2xs bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 font-mono font-bold">
                        Episentrum Limpahan
                      </span>
                    )}
                  </div>

                  <div className="space-y-3 pt-2 text-xs font-mono">
                    <div className="flex justify-between items-center">
                      <span className="text-muted-foreground">Efek Langsung (Domestik):</span>
                      <strong className="text-foreground">
                        {item.direct_effect > 0 ? `+${item.direct_effect}` : item.direct_effect}
                      </strong>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-muted-foreground">Efek Limpahan (Spasial):</span>
                      <strong className={isWage ? 'text-cyan-600 dark:text-cyan-400 font-bold text-sm' : 'text-amber-500 dark:text-amber-400'}>
                        {item.spillover_effect > 0 ? `+${item.spillover_effect}` : item.spillover_effect}
                      </strong>
                    </div>
                    <div className="flex justify-between items-center pt-2 border-t border-border">
                      <span className="text-muted-foreground font-bold">Efek Total:</span>
                      <strong className="text-emerald-500 dark:text-emerald-400 font-bold text-sm">
                        {item.total_effect > 0 ? `+${item.total_effect}` : item.total_effect}
                      </strong>
                    </div>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-border text-2xs text-muted-foreground flex items-center justify-between">
                  <span>Rasio Multiplier:</span>
                  <span className="font-mono font-bold text-foreground">{item.multiplier}x efek domestik</span>
                </div>
              </div>
            );
          })}
        </div>

        {/* Empirical Interpretation Card */}
        <div className="p-4 rounded-xl bg-muted/40 border border-border text-xs leading-relaxed text-muted-foreground space-y-2">
          <div className="flex items-center space-x-2 text-cyan-600 dark:text-cyan-400 font-bold font-mono">
            <Activity className="w-4 h-4" />
            <span>Temuan Empiris Kunci : Efek Limpahan Upah (+4.4313) Melampaui Efek Domestik (+0.3791)</span>
          </div>
          <p>
            Koefisien limpahan spasial logaritma upah buruh bernilai <strong className="text-foreground">+4,4313</strong> (lebih dari 11 kali lipat efek domestiknya). Hal ini membuktikan mekanisme ekonomi nyata: ketika suatu provinsi pusat industri (seperti Jawa Barat atau DKI Jakarta) menaikkan standar upah buruh, hal tersebut memicu arus migrasi pencari kerja masif dari provinsi-provinsi tetangga. Karena kapasitas serap pabrik terbatas, para pendatang yang belum terserap menumpuk sebagai penganggur terbuka regional.
          </p>
        </div>
      </section>

      {/* Model Comparison Table (OLS vs SLX vs SAR vs SEM vs SDM) */}
      <section className="space-y-4">
        <div className="flex justify-between items-end">
          <div>
            <h3 className="text-lg font-bold text-foreground">Evaluasi Spesifikasi Model Ekonometrika Spasial</h3>
            <p className="text-xs text-muted-foreground">
              Uji perbandingan 5 spesifikasi model pada 38 provinsi di Indonesia (Agustus 2024).
            </p>
          </div>
          <span className="text-2xs font-mono text-emerald-600 dark:text-emerald-400 px-2 py-1 rounded bg-emerald-500/10 border border-emerald-500/30">
            Model Terbaik: Spatial Durbin Model (SDM)
          </span>
        </div>

        <div className="overflow-x-auto rounded-xl border border-border bg-card shadow-xs">
          <table className="w-full text-left text-xs text-foreground font-mono">
            <thead className="bg-muted/50 text-muted-foreground uppercase text-2xs border-b border-border">
              <tr>
                <th className="py-3 px-4 font-sans">Spesifikasi Model</th>
                <th className="py-3 px-3 text-right">Parameter</th>
                <th className="py-3 px-3 text-right">Log-Likelihood</th>
                <th className="py-3 px-3 text-right">Nilai AIC</th>
                <th className="py-3 px-3 text-right">Spatial Lag (ρ / λ)</th>
                <th className="py-3 px-3 text-right">Pseudo-R²</th>
                <th className="py-3 px-4 font-sans">Status Seleksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/60">
              {spatial_models.map((m) => {
                const isSDM = m.model.includes('SDM');
                return (
                  <tr
                    key={m.model}
                    className={isSDM ? 'bg-primary/10 text-primary font-semibold' : 'hover:bg-muted/50'}
                  >
                    <td className="py-3 px-4 font-sans text-foreground flex items-center space-x-2">
                      {isSDM && <CheckCircle2 className="w-3.5 h-3.5 text-cyan-500 dark:text-cyan-400" />}
                      <span>{m.model}</span>
                    </td>
                    <td className="py-3 px-3 text-right">{m.params}</td>
                    <td className="py-3 px-3 text-right">{m.loglik}</td>
                    <td className="py-3 px-3 text-right font-bold text-foreground">{m.aic}</td>
                    <td className="py-3 px-3 text-right text-muted-foreground">{m.spatial_lag}</td>
                    <td className="py-3 px-3 text-right font-bold text-emerald-500 dark:text-emerald-400">{(m.r2 * 100).toFixed(1)}%</td>
                    <td className="py-3 px-4 font-sans">
                      <span className={`px-2 py-0.5 rounded text-2xs ${
                        isSDM 
                          ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-semibold' 
                          : 'bg-muted border border-border text-muted-foreground'
                      }`}>
                        {m.status}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>

      {/* Longitudinal Moran's I Trajectory (2017 to 2024) */}
      <section className="p-6 rounded-2xl bg-card border border-border space-y-6 shadow-xs">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-border pb-4">
          <div>
            <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block mb-1">
              Stabilitas Longitudinal (2017-2024)
            </span>
            <h3 className="text-lg font-bold text-foreground">Trajektori Autokorelasi Spasial Global (Moran's I)</h3>
          </div>
          <span className="text-xs font-mono text-muted-foreground">
            Nilai Harapan E(I) = -0.0303
          </span>
        </div>

        {/* Trajectory Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
          {moran_trajectory.map((m) => {
            const is2024 = m.year === 2024;
            return (
              <div
                key={m.year}
                className={`p-3 rounded-xl border text-center font-mono ${
                  is2024
                    ? 'bg-cyan-500/10 border-cyan-500/60 text-cyan-700 dark:text-cyan-300 ring-1 ring-cyan-500/30 font-bold'
                    : 'bg-muted/30 border-border text-foreground'
                }`}
              >
                <span className="text-2xs text-muted-foreground block font-sans">{m.year}</span>
                <span className={`text-base font-bold block my-1 ${is2024 ? 'text-cyan-600 dark:text-cyan-400' : 'text-foreground'}`}>
                  +{m.moran_i.toFixed(3)}
                </span>
                <span className="text-3xs text-emerald-600 dark:text-emerald-400 block font-semibold">
                  p = {m.p_value.toFixed(3)}
                </span>
              </div>
            );
          })}
        </div>

        <p className="text-xs text-muted-foreground leading-relaxed font-sans pt-1">
          Pola ketergantungan spasial pengangguran terbuka di Indonesia terbukti stabil dan mengelompok secara signifikan ($p &lt; 0,05$) sepanjang 8 tahun pengamatan, membantah asumsi bahwa pasar kerja antardaerah bersifat independen.
        </p>
      </section>
    </div>
  );
};
