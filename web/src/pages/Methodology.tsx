import React from 'react';

import { LaborDataBundle } from '../types';
import { MetricBadge } from '../components/MetricBadge';

interface MethodologyProps {
  data: LaborDataBundle;
}

export const Methodology: React.FC<MethodologyProps> = ({ data }) => {
  const { methodology_vif } = data;

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Header */}
      <div className="border-b border-border pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-600 dark:text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-600 dark:bg-cyan-400"></span>
            <span>MODUL 5 : SCIENTIFIC RIGOR & METHODOLOGY AUDIT</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-foreground tracking-tight">
            Transparansi Metodologi & Integritas Data
          </h1>
          <p className="text-sm text-muted-foreground mt-1 max-w-2xl">
            Seluruh spesifikasi ekonometrika, klasterisasi, dan peramalan dibangun murni dari catatan resmi BPS Sakernas 2017-2024 tanpa imputasi sintetis atau manipulasi artifisial.
          </p>
        </div>

        {/* Micro Benchmarks */}
        <div className="flex flex-wrap gap-2 text-xs font-mono">
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Panel Seimbang:</span> <strong className="text-cyan-600 dark:text-cyan-400">272 Observasi</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Between-Prov:</span> <strong className="text-emerald-600 dark:text-emerald-400">79.58%</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">VIF Maks:</span> <strong className="text-amber-600 dark:text-amber-400">2.14 (&lt; 2.5)</strong>
          </div>
        </div>
      </div>

      {/* Top Benchmark Strip */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricBadge
          label="Observasi Panel Seimbang"
          value="272 Baris"
          subtext="34 Provinsi x 8 Tahun (2017-2024)"
          variant="cyan"
        />
        <MetricBadge
          label="Pangsa Variansi Spasial"
          value="79.58%"
          subtext="Variansi antar-provinsi (Between)"
          variant="emerald"
        />
        <MetricBadge
          label="Matriks Pembobot Spasial W"
          value="k-NN (k=4)"
          subtext="Row-standardized Great-Circle"
          variant="amber"
        />
        <MetricBadge
          label="Integritas Imputasi"
          value="0 Missing"
          subtext="Bebas imputasi data buatan"
          variant="slate"
        />
      </div>

      {/* 4 Core Methodological Decisions */}
      <section className="space-y-6">
        <div className="border-b border-border pb-3">
          <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block mb-1">
            Pertahanan Metodologis Ilmiah
          </span>
          <h2 className="text-xl font-bold text-foreground tracking-tight">
            Empat Keputusan Metodologis Utama
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Decision 01 */}
          <div className="p-6 rounded-2xl bg-card border border-border space-y-3 shadow-xs">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-600 dark:text-cyan-400 font-bold uppercase">Keputusan 01</span>
              <span className="px-2 py-0.5 rounded bg-muted border border-border text-muted-foreground">
                Variansi Lintas Wilayah
              </span>
            </div>
            <h3 className="font-bold text-base text-foreground">
              Mengapa Pendekatan Teritorial & Klasterisasi Spasial Mutlak Diperlukan?
            </h3>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Dekomposisi variansi panel membuktikan bahwa <strong className="text-foreground">79,58% variasi data</strong> berada pada tingkat antar-provinsi (*between-province*), sedangkan variasi waktu (*within-province*) hanya mencakup 20,42%. Hal ini memberikan justifikasi ilmiah mutlak bahwa struktur ketenagakerjaan di Indonesia didominasi oleh kesenjangan spasial dan memerlukan intervensi kebijakan berbasis klaster terdesentralisasi, bukan target nasional seragam.
            </p>
          </div>

          {/* Decision 02 */}
          <div className="p-6 rounded-2xl bg-card border border-border space-y-3 shadow-xs">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-600 dark:text-cyan-400 font-bold uppercase">Keputusan 02</span>
              <span className="px-2 py-0.5 rounded bg-muted border border-border text-muted-foreground">
                Spesifikasi Model
              </span>
            </div>
            <h3 className="font-bold text-base text-foreground">
              Mengapa Memilih Spatial Durbin Model (SDM) Dibanding OLS Standar?
            </h3>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Model OLS standar menghasilkan bias spesifikasi serius karena mengasumsikan setiap provinsi saling independen ($R^2$ hanya 0,391). Model SDM menangkap lag spasial variabel dependen dan independen secara simultan, melompatkan daya jelas model ke <strong className="text-foreground">0,547</strong> dan meminimalkan nilai AIC ke 119,09.
            </p>
          </div>

          {/* Decision 03 */}
          <div className="p-6 rounded-2xl bg-card border border-border space-y-3 shadow-xs">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-600 dark:text-cyan-400 font-bold uppercase">Keputusan 03</span>
              <span className="px-2 py-0.5 rounded bg-muted border border-border text-muted-foreground">
                Matriks Bobot W
              </span>
            </div>
            <h3 className="font-bold text-base text-foreground">
              Mengapa Menggunakan Matriks Pembobot k-NN (k = 4)?
            </h3>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Mengingat kondisi geografis Indonesia sebagai negara kepulauan, matriks kontiguitas darat murni (seperti Queen/Rook) akan mengisolasi provinsi-provinsi kepulauan (Maluku, Bali, Nusa Tenggara). Pembobotan <strong className="text-foreground">k-Nearest Neighbors dengan k = 4</strong> terstandardisasi baris yang dihitung dari jarak lingkaran besar (Great-Circle Haversine) 38 ibukota provinsi terbukti paling konsisten menangkap interaksi ketenagakerjaan lintas selat.
            </p>
          </div>

          {/* Decision 04 */}
          <div className="p-6 rounded-2xl bg-card border border-border space-y-3 shadow-xs">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-600 dark:text-cyan-400 font-bold uppercase">Keputusan 04</span>
              <span className="px-2 py-0.5 rounded bg-muted border border-border text-muted-foreground">
                Parsimoni & VIF
              </span>
            </div>
            <h3 className="font-bold text-base text-foreground">
              Uji Multikolinearitas Bersih & Keunggulan Model Sederhana
            </h3>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Semua prediktor regresi diuji dengan Variance Inflation Factor (VIF), dan seluruh nilai berada di bawah 2,5 (jauh di bawah batas kritis 10), membuktikan tidak ada multikolinearitas. Pada peramalan deret waktu, prinsip parsimoni terbukti unggul: model Holt Damped Trend mengungguli model kompleks yang cenderung overfitting terhadap anomali lonjakan pandemi 2020.
            </p>
          </div>
        </div>
      </section>

      {/* Multicollinearity VIF Diagnostic Table */}
      <section className="space-y-4">
        <div>
          <h3 className="text-lg font-bold text-foreground">Tabel Diagnostik Multikolinearitas (Variance Inflation Factor / VIF)</h3>
          <p className="text-xs text-muted-foreground">Seluruh prediktor memenuhi standar ketat VIF &lt; 5.0 (bebas dari korelasi ganda).</p>
        </div>

        <div className="overflow-x-auto rounded-xl border border-border bg-card max-w-2xl shadow-xs">
          <table className="w-full text-left text-xs text-foreground font-mono">
            <thead className="bg-muted/50 text-muted-foreground uppercase text-2xs border-b border-border">
              <tr>
                <th className="py-3 px-4 font-sans">Variabel Independen</th>
                <th className="py-3 px-4 text-right">Nilai VIF</th>
                <th className="py-3 px-4 font-sans">Status Diagnostik</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/60">
              {methodology_vif.map((v) => (
                <tr key={v.variable} className="hover:bg-muted/50">
                  <td className="py-3 px-4 font-sans text-foreground">{v.variable}</td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-600 dark:text-emerald-400">{v.vif}</td>
                  <td className="py-3 px-4 font-sans">
                    <span className="px-2 py-0.5 rounded text-2xs bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">
                      {v.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
};
