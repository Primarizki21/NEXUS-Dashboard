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
      <div className="border-b border-slate-800 pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
            <span>MODUL 5 : SCIENTIFIC RIGOR & METHODOLOGY AUDIT</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
            Transparansi Metodologi & Integritas Data
          </h1>
          <p className="text-sm text-slate-400 mt-1 max-w-2xl">
            Seluruh spesifikasi ekonometrika, klasterisasi, dan peramalan dibangun murni dari catatan resmi BPS Sakernas 2017-2024 tanpa imputasi sintetis atau manipulasi artifisial.
          </p>
        </div>

        {/* Micro Benchmarks */}
        <div className="flex flex-wrap gap-2 text-xs font-mono">
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">Panel Seimbang:</span> <strong className="text-cyan-400">272 Observasi</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">Between-Prov:</span> <strong className="text-emerald-400">79.58%</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">VIF Maks:</span> <strong className="text-amber-400">2.14 (&lt; 2.5)</strong>
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
        <div className="border-b border-slate-800 pb-3">
          <span className="text-xs font-mono text-cyan-400 uppercase tracking-wider block mb-1">
            Pertahanan Metodologis Ilmiah
          </span>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Empat Keputusan Metodologis Utama
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Decision 01 */}
          <div className="p-6 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-3">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-400 font-bold uppercase">Keputusan 01</span>
              <span className="px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-slate-400">
                Variansi Lintas Wilayah
              </span>
            </div>
            <h3 className="font-bold text-base text-white">
              Mengapa Pendekatan Teritorial & Klasterisasi Spasial Mutlak Diperlukan?
            </h3>
            <p className="text-xs text-slate-300 leading-relaxed">
              Dekomposisi variansi panel membuktikan bahwa <strong>79,58% variasi data</strong> berada pada tingkat antar-provinsi (*between-province*), sedangkan variasi waktu (*within-province*) hanya mencakup 20,42%. Hal ini memberikan justifikasi ilmiah mutlak bahwa struktur ketenagakerjaan di Indonesia didominasi oleh kesenjangan spasial dan memerlukan intervensi kebijakan berbasis klaster terdesentralisasi, bukan target nasional seragam.
            </p>
          </div>

          {/* Decision 02 */}
          <div className="p-6 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-3">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-400 font-bold uppercase">Keputusan 02</span>
              <span className="px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-slate-400">
                Spesifikasi Model
              </span>
            </div>
            <h3 className="font-bold text-base text-white">
              Mengapa Memilih Spatial Durbin Model (SDM) Dibanding OLS Standar?
            </h3>
            <p className="text-xs text-slate-300 leading-relaxed">
              Model OLS standar menghasilkan bias spesifikasi serius karena mengasumsikan setiap provinsi saling independen ($R^2$ hanya 0,391). Model SDM menangkap lag spasial variabel dependen dan independen secara simultan, melompatkan daya jelas model ke <strong>0,547</strong> dan meminimalkan nilai AIC ke 119,09.
            </p>
          </div>

          {/* Decision 03 */}
          <div className="p-6 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-3">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-400 font-bold uppercase">Keputusan 03</span>
              <span className="px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-slate-400">
                Matriks Bobot W
              </span>
            </div>
            <h3 className="font-bold text-base text-white">
              Mengapa Menggunakan Matriks Pembobot k-NN (k = 4)?
            </h3>
            <p className="text-xs text-slate-300 leading-relaxed">
              Mengingat kondisi geografis Indonesia sebagai negara kepulauan, matriks kontiguitas darat murni (seperti Queen/Rook) akan mengisolasi provinsi-provinsi kepulauan (Maluku, Bali, Nusa Tenggara). Pembobotan <strong>k-Nearest Neighbors dengan k = 4</strong> terstandardisasi baris yang dihitung dari jarak lingkaran besar (Great-Circle Haversine) 38 ibukota provinsi terbukti paling konsisten menangkap interaksi ketenagakerjaan lintas selat.
            </p>
          </div>

          {/* Decision 04 */}
          <div className="p-6 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-3">
            <div className="flex items-center justify-between text-xs font-mono">
              <span className="text-cyan-400 font-bold uppercase">Keputusan 04</span>
              <span className="px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-slate-400">
                Parsimoni & VIF
              </span>
            </div>
            <h3 className="font-bold text-base text-white">
              Uji Multikolinearitas Bersih & Keunggulan Model Sederhana
            </h3>
            <p className="text-xs text-slate-300 leading-relaxed">
              Semua prediktor regresi diuji dengan Variance Inflation Factor (VIF), dan seluruh nilai berada di bawah 2,5 (jauh di bawah batas kritis 10), membuktikan tidak ada multikolinearitas. Pada peramalan deret waktu, prinsip parsimoni terbukti unggul: model Holt Damped Trend mengungguli model kompleks yang cenderung overfitting terhadap anomali lonjakan pandemi 2020.
            </p>
          </div>
        </div>
      </section>

      {/* Multicollinearity VIF Diagnostic Table */}
      <section className="space-y-4">
        <div>
          <h3 className="text-lg font-bold text-white">Tabel Diagnostik Multikolinearitas (Variance Inflation Factor / VIF)</h3>
          <p className="text-xs text-slate-400">Seluruh prediktor memenuhi standar ketat VIF &lt; 5.0 (bebas dari korelasi ganda).</p>
        </div>

        <div className="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/60 max-w-2xl">
          <table className="w-full text-left text-xs text-slate-300 font-mono">
            <thead className="bg-slate-950 text-slate-400 uppercase text-2xs border-b border-slate-800">
              <tr>
                <th className="py-3 px-4 font-sans">Variabel Independen</th>
                <th className="py-3 px-4 text-right">Nilai VIF</th>
                <th className="py-3 px-4 font-sans">Status Diagnostik</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {methodology_vif.map((v) => (
                <tr key={v.variable} className="hover:bg-slate-800/40">
                  <td className="py-3 px-4 font-sans text-white">{v.variable}</td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-400">{v.vif}</td>
                  <td className="py-3 px-4 font-sans">
                    <span className="px-2 py-0.5 rounded text-2xs bg-emerald-950/60 text-emerald-400 border border-emerald-800">
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
