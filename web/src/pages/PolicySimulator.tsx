import React, { useState } from 'react';
import { 
  RotateCcw,
  Building,
  Tractor,
  Laptop
} from 'lucide-react';
import { LaborDataBundle } from '../types';

interface PolicySimulatorProps {
  data: LaborDataBundle;
}

export const PolicySimulator: React.FC<PolicySimulatorProps> = ({ data }) => {
  const { national_summary } = data;

  // 3 Policy Slider states (0% to 100%)
  const [vokasiLevel, setVokasiLevel] = useState<number>(50); // Klaster 1: Urban Trap
  const [hilirisasiLevel, setHilirisasiLevel] = useState<number>(45); // Klaster 2: Agrarian Shelter
  const [digitalLevel, setDigitalLevel] = useState<number>(40); // Klaster 3: Transisi

  // Job capacities per cluster (Sum = 5.40 Juta target RPJMN)
  const cap1 = 1850000; // Klaster 1 max jobs
  const cap2 = 2100000; // Klaster 2 max jobs
  const cap3 = 1450000; // Klaster 3 max jobs
  const targetTotal = national_summary.total_job_target; // 5,400,000

  // Real-time calculations
  const jobs1 = Math.round((vokasiLevel / 100) * cap1);
  const jobs2 = Math.round((hilirisasiLevel / 100) * cap2);
  const jobs3 = Math.round((digitalLevel / 100) * cap3);
  const totalJobsCreated = jobs1 + jobs2 + jobs3;
  const progressPct = Math.min(100, Math.round((totalJobsCreated / targetTotal) * 100));

  // TPT reduction estimate: 5.4M jobs reduces national TPT by ~0.61 poin (from baseline 4.91% to ~4.30%)
  const baselineTPT = 4.91;
  const maxTPTReduction = 0.65; // poin
  const currentReduction = (totalJobsCreated / targetTotal) * maxTPTReduction;
  const simulatedTPT = Math.max(3.80, Math.round((baselineTPT - currentReduction) * 100) / 100);

  // Underemployment reduction: mainly driven by lever 2 (Hilirisasi)
  const baselineUnderemp = national_summary.underemployed_2024_juta; // 11.56 Juta
  const underempReduction = Math.round((jobs2 / 1000000) * 0.85 * 100) / 100;
  const simulatedUnderemp = Math.max(7.0, Math.round((baselineUnderemp - underempReduction) * 100) / 100);

  const handleReset = () => {
    setVokasiLevel(50);
    setHilirisasiLevel(45);
    setDigitalLevel(40);
  };

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Header */}
      <div className="border-b border-slate-800 pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
            <span>MODUL 3 : DECISION SUPPORT SYSTEM & POLICY LAB</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
            Simulator Kebijakan Ketenagakerjaan RPJMN
          </h1>
          <p className="text-sm text-slate-400 mt-1 max-w-2xl">
            Simulasikan 3 tuas intervensi berbasis klaster wilayah untuk menguji pencapaian target penyerapan 5,40 juta kesempatan kerja berkualitas dan penurunan TPT menuju 4,30% pada 2029.
          </p>
        </div>

        <button
          onClick={handleReset}
          className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono text-slate-300 hover:text-white hover:bg-slate-850 cursor-pointer transition-colors"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Reset Tuas Kebijakan</span>
        </button>
      </div>

      {/* Aggregate Real-Time Simulator Dashboard */}
      <section className="p-8 rounded-2xl bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 border border-slate-800 relative overflow-hidden">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 items-center">
          <div className="lg:col-span-2 space-y-3">
            <span className="text-xs font-mono text-cyan-400 uppercase tracking-wider block">
              Total Akumulasi Kesempatan Kerja Tercipta:
            </span>
            <div className="flex items-baseline space-x-3">
              <span className="text-4xl sm:text-5xl font-black font-mono tracking-tight text-white">
                {(totalJobsCreated / 1000000).toFixed(2)} Juta
              </span>
              <span className="text-sm font-mono text-slate-400">
                / 5.40 Juta Target RPJMN
              </span>
            </div>

            {/* Progress Bar */}
            <div className="space-y-1 pt-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-slate-400">Pencapaian Target Nasional:</span>
                <span className="font-bold text-cyan-400">{progressPct}%</span>
              </div>
              <div className="w-full bg-slate-950 rounded-full h-3 overflow-hidden border border-slate-800">
                <div
                  className="bg-gradient-to-r from-cyan-500 to-emerald-400 h-full rounded-full transition-all duration-300"
                  style={{ width: `${progressPct}%` }}
                ></div>
              </div>
            </div>
          </div>

          {/* Outcome 1: TPT Impact */}
          <div className="p-4 rounded-xl bg-slate-950/90 border border-slate-800 text-center font-mono">
            <span className="text-xs text-slate-400 block font-sans">Proyeksi TPT Nasional</span>
            <span className="text-3xl font-extrabold text-emerald-400 my-1 block">
              {simulatedTPT}%
            </span>
            <span className="text-2xs text-slate-400">
              Baseline 2024: 4.91% (-{(baselineTPT - simulatedTPT).toFixed(2)} poin)
            </span>
          </div>

          {/* Outcome 2: Underemployment Impact */}
          <div className="p-4 rounded-xl bg-slate-950/90 border border-slate-800 text-center font-mono">
            <span className="text-xs text-slate-400 block font-sans">Setengah Penganggur</span>
            <span className="text-3xl font-extrabold text-amber-400 my-1 block">
              {simulatedUnderemp} Jt
            </span>
            <span className="text-2xs text-slate-400">
              Tereduksi -{underempReduction} Juta Orang
            </span>
          </div>
        </div>
      </section>

      {/* 3 Interactive Sliders */}
      <section className="space-y-6">
        <div>
          <span className="text-xs font-mono text-cyan-400 uppercase tracking-wider block mb-1">
            Tuas Intervensi Terarah per Klaster Wilayah
          </span>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Sesuaikan Intensitas Kebijakan di Setiap Klaster
          </h2>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Lever 1: Klaster 1 Urban Trap */}
          <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-6">
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <div className="p-2.5 rounded-lg bg-red-950/60 border border-red-800 text-red-400">
                  <Building className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-sm text-white">1. Link-and-Match Vokasi & Magang Industri</h3>
                  <span className="text-xs text-slate-400 font-mono">Fokus Klaster 1 : Urban-Industrial Trap</span>
                </div>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed">
                Standardisasi kurikulum SMK bersama konsorsium industri manufaktur, insentif superdeduction tax 200%, dan standardisasi upah magang formal di 8 provinsi urban.
              </p>

              {/* Slider Input */}
              <div className="space-y-2 pt-2">
                <div className="flex justify-between items-center text-xs font-mono">
                  <span className="text-slate-400">Tingkat Penetrasi:</span>
                  <span className="text-base font-bold text-red-400">{vokasiLevel}%</span>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  step="5"
                  value={vokasiLevel}
                  onChange={(e) => setVokasiLevel(parseInt(e.target.value))}
                  className="w-full h-2 bg-slate-950 rounded-lg appearance-none cursor-pointer accent-red-500 border border-slate-800"
                />
                <div className="flex justify-between text-3xs font-mono text-slate-400">
                  <span>0% (Status Quo)</span>
                  <span>50% (Moderat)</span>
                  <span>100% (Maksimal)</span>
                </div>
              </div>
            </div>

            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-xs font-mono flex items-center justify-between">
              <span className="text-slate-400">Serapan Lapangan Kerja:</span>
              <span className="text-white font-bold text-sm">{(jobs1 / 1000000).toFixed(2)} Juta</span>
            </div>
          </div>

          {/* Lever 2: Klaster 2 Agrarian Shelter */}
          <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-6">
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <div className="p-2.5 rounded-lg bg-amber-950/60 border border-amber-800 text-amber-400">
                  <Tractor className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-sm text-white">2. Hilirisasi Pertanian & Formalisasi Desa</h3>
                  <span className="text-xs text-slate-400 font-mono">Fokus Klaster 2 : Agraris-Informal Shelter</span>
                </div>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed">
                Pembangunan unit pengolahan komoditas lokal, korporatisasi petani, jaminan sosial ketenagakerjaan, dan transisi pekerja paruh waktu menjadi pekerja penuh waktu di 18 provinsi.
              </p>

              {/* Slider Input */}
              <div className="space-y-2 pt-2">
                <div className="flex justify-between items-center text-xs font-mono">
                  <span className="text-slate-400">Tingkat Penetrasi:</span>
                  <span className="text-base font-bold text-amber-400">{hilirisasiLevel}%</span>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  step="5"
                  value={hilirisasiLevel}
                  onChange={(e) => setHilirisasiLevel(parseInt(e.target.value))}
                  className="w-full h-2 bg-slate-950 rounded-lg appearance-none cursor-pointer accent-amber-500 border border-slate-800"
                />
                <div className="flex justify-between text-3xs font-mono text-slate-400">
                  <span>0% (Status Quo)</span>
                  <span>50% (Moderat)</span>
                  <span>100% (Maksimal)</span>
                </div>
              </div>
            </div>

            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-xs font-mono flex items-center justify-between">
              <span className="text-slate-400">Serapan Lapangan Kerja:</span>
              <span className="text-white font-bold text-sm">{(jobs2 / 1000000).toFixed(2)} Juta</span>
            </div>
          </div>

          {/* Lever 3: Klaster 3 Transisi Berimbang */}
          <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-6">
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <div className="p-2.5 rounded-lg bg-emerald-950/60 border border-emerald-800 text-emerald-400">
                  <Laptop className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-sm text-white">3. Inkubasi Wirausaha & Ekonomi Kreatif</h3>
                  <span className="text-xs text-slate-400 font-mono">Fokus Klaster 3 : Transisi Berimbang</span>
                </div>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed">
                Pembiayaan modal kerja padat karya, inkubasi bisnis startup pemuda, pendampingan digitalisasi UMKM perdagangan, dan jasa mandiri di 12 provinsi penyangga.
              </p>

              {/* Slider Input */}
              <div className="space-y-2 pt-2">
                <div className="flex justify-between items-center text-xs font-mono">
                  <span className="text-slate-400">Tingkat Penetrasi:</span>
                  <span className="text-base font-bold text-emerald-400">{digitalLevel}%</span>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  step="5"
                  value={digitalLevel}
                  onChange={(e) => setDigitalLevel(parseInt(e.target.value))}
                  className="w-full h-2 bg-slate-950 rounded-lg appearance-none cursor-pointer accent-emerald-500 border border-slate-800"
                />
                <div className="flex justify-between text-3xs font-mono text-slate-400">
                  <span>0% (Status Quo)</span>
                  <span>50% (Moderat)</span>
                  <span>100% (Maksimal)</span>
                </div>
              </div>
            </div>

            <div className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-xs font-mono flex items-center justify-between">
              <span className="text-slate-400">Serapan Lapangan Kerja:</span>
              <span className="text-white font-bold text-sm">{(jobs3 / 1000000).toFixed(2)} Juta</span>
            </div>
          </div>
        </div>
      </section>

      {/* Matriks Kebijakan RPJMN 2025-2029 */}
      <section className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
        <h3 className="text-lg font-bold text-white">Rencana Aksi Kebijakan Terarah Menuju 2029</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs text-slate-300 leading-relaxed">
          <div className="p-4 rounded-xl bg-slate-950 border border-slate-850 space-y-2">
            <h4 className="font-bold text-red-400">Klaster 1 : Target TPT &lt; 5.20%</h4>
            <p>
              Mengatasi kemacetan lulusan SMK dan sarjana dengan integrasi kurikulum magang terakreditasi dan bursa kerja nasional terpadu untuk mereduksi durasi tunggu pencari kerja muda.
            </p>
          </div>
          <div className="p-4 rounded-xl bg-slate-950 border border-slate-850 space-y-2">
            <h4 className="font-bold text-amber-400">Klaster 2 : Setengah Penganggur &lt; 7.0%</h4>
            <p>
              Mengentaskan perangkap desa melalui pembiayaan kredit alsintan modern, hilirisasi agro-maritim perdesaan, serta integrasi jaminan BPJS Ketenagakerjaan bagi petani gurem.
            </p>
          </div>
          <div className="p-4 rounded-xl bg-slate-950 border border-slate-850 space-y-2">
            <h4 className="font-bold text-emerald-400">Klaster 3 : Target TPT &lt; 3.80%</h4>
            <p>
              Mendorong diversifikasi industri kreatif dan digitalisasi rantai pasok logistik, memastikan pemuda di Jawa Tengah, Jawa Timur, dan Bali memiliki opsi karir mandiri berkualitas.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
};
