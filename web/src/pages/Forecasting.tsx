import React, { useState } from 'react';
import { LaborDataBundle } from '../types';
import { MetricBadge } from '../components/MetricBadge';

interface ForecastingProps {
  data: LaborDataBundle;
}

export const Forecasting: React.FC<ForecastingProps> = ({ data }) => {
  const { historical_trajectory, forecast_trajectory } = data;
  const [show80CI, setShow80CI] = useState(true);
  const [show95CI, setShow95CI] = useState(true);
  const [selectedYear, setSelectedYear] = useState<number>(2030);

  // Combine historical and forecast points
  const allPoints = [
    ...historical_trajectory.map(p => ({ ...p, lower_80: p.tpt, upper_80: p.tpt, lower_95: p.tpt, upper_95: p.tpt })),
    ...forecast_trajectory
  ];

  // Selected year data point
  const currentPoint = allPoints.find(p => p.year === selectedYear) || allPoints[allPoints.length - 1];

  // SVG Chart Projection Dimensions: Year 2017 to 2030 (X: 50 to 850), TPT 1.0% to 9.0% (Y: 280 to 30)
  const mapX = (year: number) => {
    return 60 + ((year - 2017) / (2030 - 2017)) * 780;
  };

  const mapY = (tpt: number) => {
    const minY = 1.0;
    const maxY = 9.5;
    return 290 - ((tpt - minY) / (maxY - minY)) * 260;
  };

  // Generate Path Strings
  const histPath = historical_trajectory.map((p, i) => `${i === 0 ? 'M' : 'L'} ${mapX(p.year)} ${mapY(p.tpt)}`).join(' ');
  const fcPath = [historical_trajectory[historical_trajectory.length - 1], ...forecast_trajectory]
    .map((p, i) => `${i === 0 ? 'M' : 'L'} ${mapX(p.year)} ${mapY(p.tpt)}`).join(' ');

  // 95% Confidence Area
  const area95Path = [
    `M ${mapX(2024)} ${mapY(4.91)}`,
    ...forecast_trajectory.map(p => `L ${mapX(p.year)} ${mapY(p.upper_95)}`),
    ...[...forecast_trajectory].reverse().map(p => `L ${mapX(p.year)} ${mapY(p.lower_95)}`),
    'Z'
  ].join(' ');

  // 80% Confidence Area
  const area80Path = [
    `M ${mapX(2024)} ${mapY(4.91)}`,
    ...forecast_trajectory.map(p => `L ${mapX(p.year)} ${mapY(p.upper_80)}`),
    ...[...forecast_trajectory].reverse().map(p => `L ${mapX(p.year)} ${mapY(p.lower_80)}`),
    'Z'
  ].join(' ');

  const modelsRanking = [
    { rank: 1, name: 'Holt Damped Trend', mase1: '0.905', mase3: '1.080', mape: '11.2%', status: 'Juara 1 (Terpilih)' },
    { rank: 2, name: 'Naive (Baseline Tanpa Parameter)', mase1: '0.885', mase3: '1.180', mape: '11.4%', status: 'Runner-Up' },
    { rank: 3, name: 'Holt Exponential Smoothing', mase1: '0.912', mase3: '1.120', mape: '11.8%', status: 'Ensemble' },
    { rank: 4, name: 'Rata-Rata Bergerak (MA-3)', mase1: '1.020', mase3: '1.059', mape: '12.0%', status: 'Benchmark' },
    { rank: 5, name: 'ARIMA (1,1,0) Orde AICc', mase1: '0.940', mase3: '1.140', mape: '12.1%', status: 'Overfitting' },
    { rank: 6, name: 'Drift (Tren Deterministik)', mase1: '1.050', mase3: '1.210', mape: '12.9%', status: 'Ensemble' },
    { rank: 7, name: 'Ridge Regression (Lag-2)', mase1: '1.120', mase3: '1.310', mape: '14.0%', status: 'Kompleks' },
  ];

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Header */}
      <div className="border-b border-slate-800 pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
            <span>MODUL 4 : LEAK-FREE TIME-SERIES CROSS-VALIDATION</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
            Peramalan Waktu Runtun TPT Indonesia Menuju 2030
          </h1>
          <p className="text-sm text-slate-400 mt-1 max-w-2xl">
            Proyeksi jangka menengah menggunakan validasi silang multi-horizon bebas bocor (walk-forward CV) dengan kuantisasi selang ketidakpastian 80% dan 95%.
          </p>
        </div>

        {/* Micro Benchmarks */}
        <div className="flex flex-wrap gap-2 text-xs font-mono">
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">Model Terpilih:</span> <strong className="text-cyan-400">Holt Damped Trend</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">MASE h=1:</span> <strong className="text-emerald-400">0.905</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
            <span className="text-slate-400">Target 2030:</span> <strong className="text-amber-400">4.68%</strong>
          </div>
        </div>
      </div>

      {/* Top Benchmark Strip */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricBadge
          label="Titik Proyeksi 2025"
          value="5.05%"
          subtext="Penyesuaian transisi pasca-pemilu"
          variant="cyan"
        />
        <MetricBadge
          label="Target Akhir RPJMN 2029"
          value="4.74%"
          subtext="Koridor target RPJMN 4.00% - 4.50%"
          variant="emerald"
        />
        <MetricBadge
          label="Titik Proyeksi 2030"
          value="4.68%"
          subtext="Level terendah pasca-pemulihan"
          variant="amber"
        />
        <MetricBadge
          label="Uji Stasioneritas"
          value="d = 1"
          subtext="ADF -2.098 & KPSS 0.182"
          variant="slate"
        />
      </div>

      {/* Fanchart Interactive Visualization */}
      <section className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-6">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-slate-800 pb-4">
          <div>
            <span className="text-xs font-mono text-cyan-400 uppercase tracking-wider block mb-1">
              Fanchart Ketidakpastian Multi-Horizon
            </span>
            <h3 className="text-lg font-bold text-white">Lintasan Historis (2017-2024) dan Proyeksi (2025-2030)</h3>
          </div>

          <div className="flex items-center space-x-2">
            <button
              onClick={() => setShow80CI(!show80CI)}
              className={`px-3 py-1 rounded-lg text-xs font-mono transition-all ${
                show80CI ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/40' : 'bg-slate-950 text-slate-400 border border-slate-800'
              }`}
            >
              Selang 80% {show80CI ? 'Aktif' : 'Nonaktif'}
            </button>
            <button
              onClick={() => setShow95CI(!show95CI)}
              className={`px-3 py-1 rounded-lg text-xs font-mono transition-all ${
                show95CI ? 'bg-indigo-500/20 text-indigo-400 border border-indigo-500/40' : 'bg-slate-950 text-slate-400 border border-slate-800'
              }`}
            >
              Selang 95% {show95CI ? 'Aktif' : 'Nonaktif'}
            </button>
          </div>
        </div>

        {/* SVG Fanchart Canvas */}
        <div className="relative w-full bg-slate-950 rounded-xl border border-slate-800 p-4 overflow-hidden">
          <svg viewBox="0 0 900 320" className="w-full h-auto select-none">
            {/* Horizontal Gridlines */}
            {[2.0, 4.0, 6.0, 8.0].map((val) => (
              <g key={val}>
                <line x1="50" y1={mapY(val)} x2="860" y2={mapY(val)} stroke="#1e293b" strokeDasharray="3 3" />
                <text x="35" y={mapY(val) + 4} fill="#64748b" fontSize="10" fontFamily="monospace" textAnchor="end">{val}%</text>
              </g>
            ))}

            {/* Vertical Separator for 2024 */}
            <line x1={mapX(2024)} y1="30" x2={mapX(2024)} y2="290" stroke="#475569" strokeDasharray="4 4" strokeWidth="1.2" />
            <text x={mapX(2024)} y="24" fill="#94a3b8" fontSize="10" fontFamily="monospace" textAnchor="middle">2024 (Aktual)</text>

            {/* 95% Confidence Band */}
            {show95CI && (
              <path d={area95Path} fill="rgba(99, 102, 241, 0.12)" stroke="rgba(99, 102, 241, 0.3)" strokeDasharray="2 2" />
            )}

            {/* 80% Confidence Band */}
            {show80CI && (
              <path d={area80Path} fill="rgba(6, 182, 212, 0.2)" stroke="rgba(6, 182, 212, 0.5)" strokeDasharray="3 3" />
            )}

            {/* Historical Line */}
            <path d={histPath} fill="none" stroke="#38bdf8" strokeWidth="2.5" />

            {/* Forecast Line */}
            <path d={fcPath} fill="none" stroke="#10b981" strokeWidth="2.5" strokeDasharray="4 2" />

            {/* Year Points */}
            {allPoints.map((p) => {
              const cx = mapX(p.year);
              const cy = mapY(p.tpt);
              const isSelected = selectedYear === p.year;
              const isForecast = p.type === 'forecast';

              return (
                <g key={p.year} className="cursor-pointer" onClick={() => setSelectedYear(p.year)}>
                  {isSelected && (
                    <circle cx={cx} cy={cy} r="9" fill="none" stroke={isForecast ? '#10b981' : '#38bdf8'} strokeWidth="2" opacity="0.6" className="animate-ping" />
                  )}
                  <circle
                    cx={cx}
                    cy={cy}
                    r={isSelected ? 6 : 4.5}
                    fill={isForecast ? '#10b981' : '#38bdf8'}
                    stroke="#0f172a"
                    strokeWidth="1.5"
                  />
                  <text
                    x={cx}
                    y={cy - 10}
                    textAnchor="middle"
                    fill={isSelected ? '#ffffff' : '#94a3b8'}
                    fontSize={isSelected ? '11' : '9'}
                    fontWeight={isSelected ? 'bold' : 'normal'}
                    fontFamily="monospace"
                  >
                    {p.tpt.toFixed(2)}%
                  </text>
                  <text
                    x={cx}
                    y="308"
                    textAnchor="middle"
                    fill="#64748b"
                    fontSize="10"
                    fontFamily="monospace"
                  >
                    {p.year}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Selected Year Inspector Card */}
        <div className="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 text-xs font-mono">
          <div>
            <span className="text-slate-400 block font-sans">Tahun Terpilih : <strong>{currentPoint.year}</strong> ({currentPoint.type === 'forecast' ? 'Proyeksi' : 'Historis'})</span>
            <span className="text-xl font-bold text-white font-mono mt-0.5 block">
              Titik Estimasi TPT : {currentPoint.tpt.toFixed(2)}%
            </span>
          </div>

          {currentPoint.type === 'forecast' && (
            <div className="flex flex-wrap gap-4 text-slate-300">
              <div className="p-2 rounded bg-slate-900 border border-slate-800">
                <span className="text-2xs text-slate-400 block font-sans">Selang 80% CI</span>
                <span className="font-bold text-cyan-400">[{currentPoint.lower_80}% - {currentPoint.upper_80}%]</span>
              </div>
              <div className="p-2 rounded bg-slate-900 border border-slate-800">
                <span className="text-2xs text-slate-400 block font-sans">Selang 95% CI</span>
                <span className="font-bold text-indigo-400">[{currentPoint.lower_95}% - {currentPoint.upper_95}%]</span>
              </div>
            </div>
          )}
        </div>
      </section>

      {/* Model Benchmark Ranking Matrix (Walk-Forward CV) */}
      <section className="space-y-4">
        <div>
          <h3 className="text-lg font-bold text-white">Matriks Evaluasi Kinerja Model Peramalan (Walk-Forward CV)</h3>
          <p className="text-xs text-slate-400">
            Prinsip Parsimoni : Model sederhana dengan penahan tren terbukti mengungguli model kompleks yang overfitting terhadap guncangan COVID 2020.
          </p>
        </div>

        <div className="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/60">
          <table className="w-full text-left text-xs text-slate-300 font-mono">
            <thead className="bg-slate-950 text-slate-400 uppercase text-2xs border-b border-slate-800">
              <tr>
                <th className="py-3 px-3">Peringkat</th>
                <th className="py-3 px-4 font-sans">Model Peramalan</th>
                <th className="py-3 px-3 text-right">MASE (h=1)</th>
                <th className="py-3 px-3 text-right">MASE (h=3)</th>
                <th className="py-3 px-3 text-right">Rata-Rata MAPE</th>
                <th className="py-3 px-4 font-sans">Status Seleksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {modelsRanking.map((m) => {
                const isWinner = m.rank === 1;
                return (
                  <tr
                    key={m.name}
                    className={isWinner ? 'bg-cyan-950/30 text-cyan-300 font-semibold' : 'hover:bg-slate-800/40'}
                  >
                    <td className="py-3 px-3 font-bold text-center">{m.rank}</td>
                    <td className="py-3 px-4 font-sans text-white">{m.name}</td>
                    <td className="py-3 px-3 text-right">{m.mase1}</td>
                    <td className="py-3 px-3 text-right font-bold text-white">{m.mase3}</td>
                    <td className="py-3 px-3 text-right text-emerald-400">{m.mape}</td>
                    <td className="py-3 px-4 font-sans">
                      <span className={`px-2 py-0.5 rounded text-2xs ${
                        isWinner 
                          ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/40 font-bold' 
                          : 'bg-slate-950 text-slate-400 border border-slate-800'
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
    </div>
  );
};
