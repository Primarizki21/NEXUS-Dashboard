import React, { useState, useMemo } from 'react';
import { 
  Search, 
  Layers 
} from 'lucide-react';
import { LaborDataBundle, Province } from '../types';

const ISLAND_PATHS: Record<string, string> = {
  sumatera: "M 40.3 47.0 L 53.7 52.7 L 82.4 69.7 L 105.4 84.8 L 126.5 103.7 L 157.1 143.3 L 187.8 169.8 L 203.1 183.0 L 224.1 196.2 L 241.4 237.8 L 241.4 262.3 L 226.1 264.2 L 216.5 251.0 L 187.8 237.8 L 174.4 224.6 L 155.2 200.0 L 138.0 169.8 L 115.0 137.7 L 103.5 120.7 L 69.0 92.3 L 55.6 73.4 L 40.3 47.0 Z",
  jawa: "M 243.3 266.1 L 260.5 268.0 L 293.1 281.2 L 329.5 283.1 L 373.5 285.0 L 398.4 298.2 L 406.1 307.7 L 398.4 317.1 L 383.1 309.6 L 350.5 307.7 L 302.7 298.2 L 273.9 292.6 L 252.9 285.0 L 243.3 266.1 Z",
  kalimantan: "M 302.7 133.9 L 308.4 118.8 L 337.1 133.9 L 360.1 124.4 L 408.0 124.4 L 436.7 81.0 L 465.4 75.3 L 471.2 96.1 L 465.4 113.1 L 475.0 133.9 L 459.7 171.7 L 436.7 177.3 L 440.5 220.8 L 409.9 218.9 L 379.3 213.2 L 350.5 205.7 L 325.6 205.7 L 319.9 186.8 L 306.5 162.2 L 298.8 152.8 L 302.7 133.9 Z",
  sulawesi: "M 509.5 258.6 L 503.7 209.4 L 490.3 200.0 L 501.8 171.7 L 509.5 152.8 L 528.6 133.9 L 551.6 137.7 L 589.9 133.9 L 609.0 124.4 L 605.2 133.9 L 580.3 143.3 L 551.6 162.2 L 580.3 167.9 L 551.6 181.1 L 536.3 181.1 L 542.0 205.7 L 566.9 224.6 L 570.7 243.4 L 551.6 251.0 L 542.0 237.8 L 522.9 243.4 L 513.3 258.6 L 509.5 258.6 Z",
  bali_nusra: "M 406.1 305.8 L 427.1 305.8 L 427.1 319.0 L 406.1 317.1 L 406.1 305.8 Z",
  lombok: "M 436.7 307.7 L 450.1 307.7 L 448.2 320.9 L 436.7 319.0 L 436.7 307.7 Z",
  sumbawa: "M 453.9 309.6 L 496.1 311.4 L 484.6 320.9 L 455.9 320.9 L 453.9 309.6 Z",
  flores: "M 509.5 311.4 L 570.7 309.6 L 566.9 319.0 L 509.5 319.0 L 509.5 311.4 Z",
  timor: "M 580.3 345.4 L 611.0 322.8 L 609.0 334.1 L 589.9 347.3 L 580.3 345.4 Z",
  maluku_halmahera: "M 655.0 115.0 L 676.1 124.4 L 681.8 137.7 L 666.5 158.4 L 656.9 143.3 L 655.0 115.0 Z",
  maluku_seram: "M 666.5 209.4 L 716.3 213.2 L 708.6 222.7 L 666.5 220.8 L 666.5 209.4 Z",
  papua: "M 723.9 169.8 L 752.7 167.9 L 781.4 167.9 L 819.7 186.8 L 858.0 183.0 L 911.6 200.0 L 915.4 324.7 L 905.9 313.3 L 867.6 256.7 L 829.3 237.8 L 791.0 228.3 L 771.8 218.9 L 743.1 205.7 L 727.8 186.8 L 723.9 169.8 Z",
};

const LATITUDE_GRIDS = [
  { lat: 5.0, y: 58.3, label: '5° LU' },
  { lat: 0.0, y: 152.8, label: 'Khatulistiwa (0°)' },
  { lat: -5.0, y: 247.2, label: '5° LS' },
  { lat: -10.0, y: 341.6, label: '10° LS' },
];

const LONGITUDE_GRIDS = [
  { lon: 95.0, x: 34.6, label: '95° BT' },
  { lon: 100.0, x: 130.3, label: '100° BT' },
  { lon: 105.0, x: 226.0, label: '105° BT' },
  { lon: 110.0, x: 321.8, label: '110° BT' },
  { lon: 115.0, x: 417.5, label: '115° BT' },
  { lon: 120.0, x: 513.3, label: '120° BT' },
  { lon: 125.0, x: 609.0, label: '125° BT' },
  { lon: 130.0, x: 704.8, label: '130° BT' },
  { lon: 135.0, x: 800.5, label: '135° BT' },
  { lon: 140.0, x: 896.3, label: '140° BT' },
];

interface CartographyProps {
  data: LaborDataBundle;
}

export const Cartography: React.FC<CartographyProps> = ({ data }) => {
  const { provinces, clusters } = data;
  const [selectedLayer, setSelectedLayer] = useState<'cluster' | 'lisa' | 'tpt' | 'informal' | 'ikkd'>('cluster');
  const [selectedProvince, setSelectedProvince] = useState<Province>(provinces[0]);
  const [searchQuery, setSearchQuery] = useState('');
  const [islandFilter, setIslandFilter] = useState('Semua');
  const [clusterFilter, setClusterFilter] = useState<number | 'Semua'>('Semua');

  // Island options
  const islands = ['Semua', 'Sumatera', 'Jawa', 'Bali & Nusa Tenggara', 'Kalimantan', 'Sulawesi', 'Maluku', 'Papua'];

  // Filter provinces for table
  const filteredProvinces = useMemo(() => {
    return provinces.filter((p) => {
      const matchSearch = p.name.toLowerCase().includes(searchQuery.toLowerCase());
      const matchIsland = islandFilter === 'Semua' || p.pulau === islandFilter;
      const matchCluster = clusterFilter === 'Semua' || p.cluster_id === clusterFilter;
      return matchSearch && matchIsland && matchCluster;
    });
  }, [provinces, searchQuery, islandFilter, clusterFilter]);

  // Coordinate projection helper: lon (95 to 141), lat (-11 to 6) -> SVG viewBox 0 0 950 400
  const projectCoords = (lon: number, lat: number) => {
    const minLon = 94.5;
    const maxLon = 141.5;
    const minLat = -11.5;
    const maxLat = 6.5;

    const x = ((lon - minLon) / (maxLon - minLon)) * 900 + 25;
    const y = ((maxLat - lat) / (maxLat - minLat)) * 340 + 30;
    return { x, y };
  };

  const getMarkerColor = (p: Province) => {
    if (selectedLayer === 'cluster') {
      if (p.cluster_id === 1) return '#ef4444'; // Red
      if (p.cluster_id === 2) return '#f59e0b'; // Amber
      return '#10b981'; // Emerald
    }
    if (selectedLayer === 'lisa') {
      if (p.lisa_quad.includes('High-High')) return '#ef4444';
      if (p.lisa_quad.includes('Low-Low')) return '#3b82f6';
      if (p.lisa_quad.includes('Low-High')) return '#10b981';
      return '#64748b';
    }
    if (selectedLayer === 'tpt') {
      if (p.tpt >= 6.0) return '#ef4444';
      if (p.tpt >= 4.5) return '#f59e0b';
      return '#10b981';
    }
    if (selectedLayer === 'informal') {
      if (p.informal >= 70.0) return '#f59e0b';
      if (p.informal >= 50.0) return '#3b82f6';
      return '#10b981';
    }
    if (selectedLayer === 'ikkd') {
      if (p.ikkd_score >= 70.0) return '#ef4444'; // Red: Sangat Rentan / Critical
      if (p.ikkd_score >= 45.0) return '#f59e0b'; // Amber: Rentan / Warning
      if (p.ikkd_score >= 25.0) return '#3b82f6'; // Blue: Moderat
      return '#10b981'; // Green: Resilien
    }
    return '#06b6d4';
  };

  const getNodeLabel = (p: Province) => {
    const shortName = p.name.replace('Kepulauan', 'Kep.').replace('Nusa Tenggara', 'NT');
    if (selectedLayer === 'cluster') return `${shortName} (K${p.cluster_id})`;
    if (selectedLayer === 'lisa') return `${shortName} (${p.lisa_quad.split(' ')[0]})`;
    if (selectedLayer === 'tpt') return `${shortName} (${p.tpt.toFixed(2)}%)`;
    if (selectedLayer === 'informal') return `${shortName} (${p.informal.toFixed(1)}%)`;
    if (selectedLayer === 'ikkd') return `${shortName} (${p.ikkd_score.toFixed(1)})`;
    return `${shortName} (${p.tpt.toFixed(2)}%)`;
  };

  const getLayerBadge = (p: Province) => {
    if (selectedLayer === 'cluster') {
      return {
        label: `Klaster ${p.cluster_id}`,
        sub: p.cluster_id === 1 ? 'Urban-Industrial Trap' : p.cluster_id === 2 ? 'Agraris-Informal Shelter' : 'Transisi Berimbang',
        color: getMarkerColor(p),
      };
    }
    if (selectedLayer === 'lisa') {
      return {
        label: p.lisa_quad,
        sub: p.lisa_sig ? 'Signifikan Spasial' : 'Non-Signifikan',
        color: getMarkerColor(p),
      };
    }
    if (selectedLayer === 'tpt') {
      return {
        label: `TPT ${p.tpt}%`,
        sub: p.tpt >= 6.0 ? 'Kategori Tinggi' : p.tpt >= 4.5 ? 'Kategori Sedang' : 'Terkendali',
        color: getMarkerColor(p),
      };
    }
    if (selectedLayer === 'informal') {
      return {
        label: `Informal ${p.informal}%`,
        sub: p.informal >= 70.0 ? 'Informalitas Ekstrem' : p.informal >= 50.0 ? 'Informal Menengah' : 'Formal Dominan',
        color: getMarkerColor(p),
      };
    }
    if (selectedLayer === 'ikkd') {
      return {
        label: `IKKD ${p.ikkd_score}`,
        sub: p.ikkd_score >= 70.0 ? 'Sangat Rentan (Red Alert)' : p.ikkd_score >= 45.0 ? 'Waspada (Amber)' : p.ikkd_score >= 25.0 ? 'Moderat' : 'Resilien (Aman)',
        color: getMarkerColor(p),
      };
    }
    return { label: `Klaster ${p.cluster_id}`, sub: '', color: getMarkerColor(p) };
  };

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Header */}
      <div className="border-b border-border pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-cyan-600 dark:text-cyan-400 mb-2">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-600 dark:bg-cyan-400"></span>
            <span>MODUL 1 : CARTOGRAPHY & REGIONAL TYPOLOGY</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-foreground tracking-tight">
            Tipologi Kartografi & Disparitas Spasial
          </h1>
          <p className="text-sm text-muted-foreground mt-1 max-w-2xl">
            Klasifikasi 38 provinsi ke dalam 3 tipologi pasar kerja objektif berdasarkan 4 dimensi: TPT Total, Rasio Mismatch Vokasi, Informalitas, dan Upah Rata-rata.
          </p>
        </div>

        {/* Micro Benchmarks */}
        <div className="flex flex-wrap gap-2 text-xs font-mono">
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Algoritma:</span> <strong className="text-cyan-600 dark:text-cyan-400">K-Means (k=3)</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Silhouette:</span> <strong className="text-emerald-600 dark:text-emerald-400">0.441</strong>
          </div>
          <div className="px-3 py-1.5 rounded-lg bg-card border border-border text-foreground">
            <span className="text-muted-foreground">Bootstrap ARI:</span> <strong className="text-amber-600 dark:text-amber-400">1.000 (Stabil)</strong>
          </div>
        </div>
      </div>

      {/* 3 Cluster Banner Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {clusters.map((c) => {

          return (
            <div
              key={c.id}
              onClick={() => setClusterFilter(clusterFilter === c.id ? 'Semua' : c.id)}
              className={`p-5 rounded-2xl border transition-all cursor-pointer relative overflow-hidden ${
                clusterFilter === c.id
                  ? 'bg-card border-cyan-500/80 shadow-md shadow-cyan-500/10 ring-1 ring-cyan-500/50'
                  : 'bg-card border-border hover:border-border/80'
              }`}
            >
              <div className="flex items-center justify-between mb-3">
                <span
                  className="w-3 h-3 rounded-full"
                  style={{ backgroundColor: c.color }}
                ></span>
                <span className="text-xs font-mono text-muted-foreground px-2 py-0.5 rounded bg-muted/60 border border-border">
                  {c.provinces.length} Provinsi
                </span>
              </div>

              <h3 className="font-bold text-foreground text-base mb-1">{c.name}</h3>
              <span className="text-xs font-mono text-muted-foreground block mb-3">{c.tagline}</span>
              <p className="text-xs text-muted-foreground leading-relaxed line-clamp-3 mb-4">
                {c.desc}
              </p>

              <div className="grid grid-cols-3 gap-2 pt-3 border-t border-border text-center">
                <div>
                  <span className="text-[11px] font-sans font-medium text-muted-foreground block">Rata TPT</span>
                  <span className="text-xs font-bold text-foreground font-mono">{c.tpt_mean}%</span>
                </div>
                <div>
                  <span className="text-[11px] font-sans font-medium text-muted-foreground block">Formal</span>
                  <span className="text-xs font-bold text-foreground font-mono">{c.formal_mean}%</span>
                </div>
                <div>
                  <span className="text-[11px] font-sans font-medium text-muted-foreground block">Rata Upah</span>
                  <span className="text-xs font-bold text-foreground font-mono">{(c.upah_mean / 1000000).toFixed(2)} jt</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Interactive Archipelago Map Canvas & Inspector */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Map View */}
        <div className="lg:col-span-2 p-6 rounded-2xl bg-card border border-border space-y-4 flex flex-col justify-between shadow-xs">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center space-x-2">
              <Layers className="w-4 h-4 text-cyan-400" />
              <span className="text-xs font-mono text-foreground uppercase">Pilih Layer Tematik:</span>
            </div>
            <div className="flex flex-wrap gap-1.5">
              <button
                onClick={() => setSelectedLayer('cluster')}
                className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                  selectedLayer === 'cluster'
                    ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-bold'
                    : 'bg-muted/50 text-muted-foreground border border-border hover:bg-muted'
                }`}
              >
                3 Klaster Pasar Kerja
              </button>
              <button
                onClick={() => setSelectedLayer('lisa')}
                className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                  selectedLayer === 'lisa'
                    ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-bold'
                    : 'bg-muted/50 text-muted-foreground border border-border hover:bg-muted'
                }`}
              >
                LISA 2024 (Hotspots)
              </button>
              <button
                onClick={() => setSelectedLayer('tpt')}
                className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                  selectedLayer === 'tpt'
                    ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-bold'
                    : 'bg-muted/50 text-muted-foreground border border-border hover:bg-muted'
                }`}
              >
                Tingkat TPT (%)
              </button>
              <button
                onClick={() => setSelectedLayer('informal')}
                className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                  selectedLayer === 'informal'
                    ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-bold'
                    : 'bg-muted/50 text-muted-foreground border border-border hover:bg-muted'
                }`}
              >
                Pangsa Informal (%)
              </button>
              <button
                onClick={() => setSelectedLayer('ikkd')}
                className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                  selectedLayer === 'ikkd'
                    ? 'bg-cyan-500/20 text-cyan-600 dark:text-cyan-400 border border-cyan-500/40 font-bold'
                    : 'bg-muted/50 text-muted-foreground border border-border hover:bg-muted'
                }`}
              >
                IKKD (Early Warning)
              </button>
            </div>
          </div>

          {/* SVG Canvas Map */}
          <div className="relative w-full bg-slate-100/70 dark:bg-slate-950/90 rounded-xl border border-border p-4 overflow-hidden shadow-xs">
            <svg
              viewBox="0 0 950 400"
              className="w-full h-auto max-h-[420px] select-none"
            >
              {/* Graticule Latitude lines */}
              {LATITUDE_GRIDS.map((g) => (
                <g key={g.label}>
                  <line
                    x1="20"
                    y1={g.y}
                    x2="930"
                    y2={g.y}
                    stroke="currentColor"
                    className="text-slate-300 dark:text-slate-800"
                    strokeDasharray={g.lat === 0 ? "none" : "3 3"}
                    strokeWidth={g.lat === 0 ? "1.5" : "0.75"}
                    opacity={g.lat === 0 ? "0.8" : "0.5"}
                  />
                  <text
                    x="25"
                    y={g.y - 4}
                    fill="currentColor"
                    className="text-slate-400 dark:text-slate-500 text-[9px] font-mono select-none"
                  >
                    {g.label}
                  </text>
                </g>
              ))}

              {/* Graticule Longitude lines */}
              {LONGITUDE_GRIDS.map((g) => (
                <g key={g.label}>
                  <line
                    x1={g.x}
                    y1="30"
                    x2={g.x}
                    y2="370"
                    stroke="currentColor"
                    className="text-slate-300 dark:text-slate-800"
                    strokeDasharray="3 3"
                    strokeWidth="0.75"
                    opacity="0.4"
                  />
                  <text
                    x={g.x}
                    y="386"
                    textAnchor="middle"
                    fill="currentColor"
                    className="text-slate-400 dark:text-slate-500 text-[8.5px] font-mono select-none"
                  >
                    {g.label}
                  </text>
                </g>
              ))}

              {/* Basemap: Indonesian Archipelago Silhouettes */}
              <g className="transition-colors duration-200">
                {Object.entries(ISLAND_PATHS).map(([islandName, pathD]) => (
                  <path
                    key={islandName}
                    d={pathD}
                    className="fill-slate-200/90 dark:fill-slate-800/60 stroke-slate-300/80 dark:stroke-slate-700/60 transition-colors"
                    strokeWidth="1"
                    strokeLinejoin="round"
                  />
                ))}
              </g>

              {/* Spatial Connections / Flow Arcs */}
              <path
                d="M 230 250 Q 280 200 310 270"
                fill="none"
                stroke="rgba(6, 182, 212, 0.45)"
                strokeWidth="1.5"
                strokeDasharray="3 3"
              />
              <path
                d="M 310 270 Q 500 180 840 220"
                fill="none"
                stroke="rgba(6, 182, 212, 0.35)"
                strokeWidth="1.2"
                strokeDasharray="4 4"
              />

              {/* Province Nodes */}
              {provinces.map((p) => {
                const { x, y } = projectCoords(p.lon, p.lat);
                const isCurrent = selectedProvince.name === p.name;
                const markerColor = getMarkerColor(p);
                const radius = isCurrent ? 8 : (p.tpt >= 6.0 ? 6.5 : 5);

                return (
                  <g
                    key={p.name}
                    className="cursor-pointer transition-transform duration-200"
                    onClick={() => setSelectedProvince(p)}
                  >
                    {/* Pulsing halo for active selection */}
                    {isCurrent && (
                      <circle
                        cx={x}
                        cy={y}
                        r={radius + 6}
                        fill="none"
                        stroke={markerColor}
                        strokeWidth="1.5"
                        opacity="0.6"
                        className="animate-ping"
                      />
                    )}

                    {/* Point Circle */}
                    <circle
                      cx={x}
                      cy={y}
                      r={radius}
                      fill={markerColor}
                      stroke={isCurrent ? '#ffffff' : '#0f172a'}
                      strokeWidth={isCurrent ? 2.2 : 1.2}
                      opacity={isCurrent ? 1 : 0.9}
                    />

                    {/* Dynamic Label for prominent or selected provinces */}
                    {(isCurrent || p.tpt >= 6.5 || ['DKI Jakarta', 'Jawa Barat', 'Bali', 'Papua Pegunungan'].includes(p.name)) && (
                      <text
                        x={x}
                        y={y - 9}
                        textAnchor="middle"
                        fill="currentColor"
                        className={`pointer-events-none drop-shadow text-[9px] font-sans ${
                          isCurrent 
                            ? 'font-bold text-cyan-600 dark:text-cyan-300' 
                            : 'font-medium text-slate-700 dark:text-slate-300'
                        }`}
                      >
                        {getNodeLabel(p)}
                      </text>
                    )}
                  </g>
                );
              })}
            </svg>
          </div>
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs text-muted-foreground pt-1 border-t border-border/60">
            <span className="font-mono text-2xs">
              Klik salah satu titik provinsi untuk inspeksi metrik. Layer aktif: <strong className="text-foreground uppercase">{selectedLayer}</strong>
            </span>
            <div className="flex flex-wrap items-center gap-3 text-2xs font-mono">
              {selectedLayer === 'cluster' && (
                <>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-red-500 inline-block"></span>
                    <span>Klaster 1 (Urban Trap)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                    <span>Klaster 2 (Agraris Shelter)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                    <span>Klaster 3 (Transisi Berimbang)</span>
                  </span>
                </>
              )}
              {selectedLayer === 'lisa' && (
                <>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-red-500 inline-block"></span>
                    <span>High-High (Hotspot)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-blue-500 inline-block"></span>
                    <span>Low-Low (Coldspot)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                    <span>Low-High (Outlier)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-slate-500 inline-block"></span>
                    <span>Non-Signifikan</span>
                  </span>
                </>
              )}
              {selectedLayer === 'tpt' && (
                <>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-red-500 inline-block"></span>
                    <span>Tinggi (≥ 6.0%)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                    <span>Sedang (4.5% - 6.0%)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                    <span>Terkendali (&lt; 4.5%)</span>
                  </span>
                </>
              )}
              {selectedLayer === 'informal' && (
                <>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                    <span>Dominan Informal (≥ 70%)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-blue-500 inline-block"></span>
                    <span>Menengah (50% - 70%)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                    <span>Formal Maju (&lt; 50%)</span>
                  </span>
                </>
              )}
              {selectedLayer === 'ikkd' && (
                <>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-red-500 inline-block"></span>
                    <span>Sangat Rentan (≥ 70)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span>
                    <span>Rentan (45 - 70)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-blue-500 inline-block"></span>
                    <span>Moderat (25 - 45)</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                    <span>Resilien (&lt; 25)</span>
                  </span>
                </>
              )}
            </div>
          </div>
        </div>

        {/* Selected Province Inspector Card */}
        <div className="p-6 rounded-2xl bg-card border border-border flex flex-col justify-between space-y-6 shadow-xs">
          <div>
            <div className="flex items-center justify-between border-b border-border pb-4 mb-4">
              <div>
                <span className="text-xs font-mono text-muted-foreground block uppercase">Inspeksi Wilayah Terpilih</span>
                <h3 className="text-xl font-extrabold text-foreground">{selectedProvince.name}</h3>
                <span className="text-xs text-muted-foreground">Pulau {selectedProvince.pulau}</span>
              </div>
              <div className="text-right">
                <span
                  className="px-2.5 py-1 rounded-full text-xs font-mono font-bold inline-block"
                  style={{
                    backgroundColor: `${getMarkerColor(selectedProvince)}20`,
                    color: getMarkerColor(selectedProvince),
                    border: `1px solid ${getMarkerColor(selectedProvince)}50`
                  }}
                >
                  {getLayerBadge(selectedProvince).label}
                </span>
                {getLayerBadge(selectedProvince).sub && (
                  <span className="text-[10px] text-muted-foreground block font-mono mt-0.5">
                    {getLayerBadge(selectedProvince).sub}
                  </span>
                )}
              </div>
            </div>

            <div className="space-y-4">
              {/* Active Layer Dynamic Interpretation Callout */}
              <div className="p-3 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-between">
                <div>
                  <span className="text-2xs font-mono uppercase text-cyan-600 dark:text-cyan-400 block font-bold">
                    Metrik Kunci Layer {selectedLayer.toUpperCase()}
                  </span>
                  <span className="text-xs font-semibold text-foreground mt-0.5 block">
                    {selectedLayer === 'cluster' && `Klaster ${selectedProvince.cluster_id}: ${clusters.find(c => c.id === selectedProvince.cluster_id)?.name}`}
                    {selectedLayer === 'lisa' && `Status Spasial: ${selectedProvince.lisa_quad} (${selectedProvince.lisa_sig ? 'Signifikan p < 0.05' : 'Non-Signifikan'})`}
                    {selectedLayer === 'tpt' && `Tingkat Pengangguran: ${selectedProvince.tpt.toFixed(2)}% (Peringkat Provinsi)`}
                    {selectedLayer === 'informal' && `Proporsi Sektor Informal: ${selectedProvince.informal.toFixed(2)}%`}
                    {selectedLayer === 'ikkd' && `Skor Kerentanan IKKD: ${selectedProvince.ikkd_score.toFixed(1)} / 100`}
                  </span>
                </div>
              </div>
              {/* TPT Big Callout */}
              <div className="p-4 rounded-xl bg-muted/40 border border-border flex items-center justify-between">
                <div>
                  <span className="text-xs text-muted-foreground block font-mono">Tingkat Pengangguran Terbuka</span>
                  <span className="text-2xl font-bold font-mono text-cyan-600 dark:text-cyan-400">{selectedProvince.tpt}%</span>
                </div>
                <div className="text-right">
                  <span className="text-xs text-muted-foreground block font-mono">Status LISA 2024</span>
                  <span className={`text-xs font-mono font-semibold ${selectedProvince.lisa_sig ? 'text-amber-500 dark:text-amber-400' : 'text-muted-foreground'}`}>
                    {selectedProvince.lisa_quad}
                  </span>
                </div>
              </div>

              {/* Metrics Grid */}
              <div className="grid grid-cols-2 gap-3 text-xs">
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-muted-foreground block">Pekerja Informal</span>
                  <strong className="text-amber-600 dark:text-amber-400 font-mono text-sm">{selectedProvince.informal}%</strong>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-muted-foreground block">Pekerja Formal</span>
                  <strong className="text-emerald-600 dark:text-emerald-400 font-mono text-sm">{selectedProvince.formal}%</strong>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-muted-foreground block">Rata-rata Upah</span>
                  <strong className="text-foreground font-mono text-sm">Rp{selectedProvince.upah.toLocaleString('id-ID')}</strong>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-muted-foreground block">Mismatch Terdidik</span>
                  <strong className="text-cyan-600 dark:text-cyan-400 font-mono text-sm">{selectedProvince.mismatch}x</strong>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-muted-foreground block">Indeks IKKD (Kerentanan)</span>
                  <div className="flex items-baseline space-x-1.5">
                    <strong className="text-foreground font-mono text-sm">{selectedProvince.ikkd_score}</strong>
                    <span className={`text-[10px] font-mono font-bold ${
                      selectedProvince.ikkd_score >= 70 ? 'text-red-500' :
                      selectedProvince.ikkd_score >= 45 ? 'text-amber-500' :
                      selectedProvince.ikkd_score >= 25 ? 'text-blue-500' : 'text-emerald-500'
                    }`}>
                      ({selectedProvince.ikkd_score >= 70 ? 'Sangat Rentan' :
                        selectedProvince.ikkd_score >= 45 ? 'Rentan' :
                        selectedProvince.ikkd_score >= 25 ? 'Moderat' : 'Resilien'})
                    </span>
                  </div>
                </div>
              </div>
              {/* Gender Gap Detail */}
              <div className="p-3 rounded-lg bg-muted/40 border border-border text-xs space-y-1.5">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">TPT Perempuan vs Laki-Laki</span>
                  <span className="font-mono text-foreground">
                    {selectedProvince.tpt_puan}% vs {selectedProvince.tpt_laki}%
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Selisih Gender Gap</span>
                  <span className={`font-mono font-semibold ${selectedProvince.gender_gap > 0 ? 'text-rose-500 dark:text-rose-400' : 'text-emerald-500 dark:text-emerald-400'}`}>
                    {selectedProvince.gender_gap > 0 ? `+${selectedProvince.gender_gap}` : selectedProvince.gender_gap} poin
                  </span>
                </div>
              </div>

              {/* Policy Recommendation Box */}
              <div className="p-3 rounded-lg bg-muted/30 border border-border text-xs space-y-1">
                <span className="font-bold text-foreground block">Prioritas Rekomendasi Kebijakan:</span>
                <p className="text-muted-foreground leading-relaxed font-sans">
                  {clusters.find(c => c.id === selectedProvince.cluster_id)?.policy}
                </p>
              </div>
            </div>
          </div>

          <div className="pt-2 text-[11px] text-muted-foreground text-center font-mono">
            Koordinat: {selectedProvince.lat.toFixed(2)}° LS, {selectedProvince.lon.toFixed(2)}° BT
          </div>
        </div>

      </div>

      {/* 38-Province Interactive Data Table */}
      <section className="space-y-4">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h3 className="text-lg font-bold text-foreground">Tabel Komparasi Seluruh 38 Provinsi</h3>
            <p className="text-xs text-muted-foreground">Data resmi BPS Sakernas Agustus 2024 lengkap tanpa nilai rumpang.</p>
          </div>

          {/* Filter Controls */}
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative">
              <Search className="w-4 h-4 text-muted-foreground absolute left-3 top-2.5" />
              <input
                type="text"
                placeholder="Cari provinsi..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-9 pr-3 py-1.5 rounded-lg bg-card border border-border text-xs text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-cyan-500"
              />
            </div>

            <select
              value={islandFilter}
              onChange={(e) => setIslandFilter(e.target.value)}
              className="px-3 py-1.5 rounded-lg bg-card border border-border text-xs text-foreground focus:outline-none focus:border-cyan-500"
            >
              {islands.map((isl) => (
                <option key={isl} value={isl}>{isl}</option>
              ))}
            </select>
          </div>
        </div>

        <div className="overflow-x-auto rounded-xl border border-border bg-card shadow-xs">
          <table className="w-full text-left text-xs text-foreground">
            <thead className="bg-muted/50 text-muted-foreground uppercase font-mono text-2xs border-b border-border">
              <tr>
                <th className="py-3 px-4">Provinsi</th>
                <th className="py-3 px-3">Pulau</th>
                <th className={`py-3 px-3 text-right ${selectedLayer === 'tpt' ? 'text-primary font-bold bg-primary/10' : ''}`}>TPT (%)</th>
                <th className={`py-3 px-3 text-right ${selectedLayer === 'informal' ? 'text-primary font-bold bg-primary/10' : ''}`}>Informal (%)</th>
                <th className="py-3 px-3 text-right">Upah (Rp)</th>
                <th className="py-3 px-3 text-right">Mismatch</th>
                <th className={`py-3 px-3 text-right ${selectedLayer === 'ikkd' ? 'text-primary font-bold bg-primary/10' : ''}`}>IKKD</th>
                <th className={`py-3 px-3 ${selectedLayer === 'cluster' ? 'text-primary font-bold bg-primary/10' : ''}`}>Klaster</th>
                <th className={`py-3 px-3 ${selectedLayer === 'lisa' ? 'text-primary font-bold bg-primary/10' : ''}`}>Status LISA</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/60 font-mono">
              {filteredProvinces.map((p) => {
                const isSelected = selectedProvince.name === p.name;
                return (
                  <tr
                    key={p.name}
                    onClick={() => setSelectedProvince(p)}
                    className={`cursor-pointer transition-colors ${
                      isSelected
                        ? 'bg-primary/10 text-primary font-semibold'
                        : 'hover:bg-muted/50'
                    }`}
                  >
                    <td className="py-2.5 px-4 font-sans font-medium text-foreground flex items-center space-x-2">
                      <span
                        className="w-2 h-2 rounded-full inline-block"
                        style={{ backgroundColor: getMarkerColor(p) }}
                      ></span>
                      <span>{p.name}</span>
                    </td>
                    <td className="py-2.5 px-3 font-sans text-muted-foreground">{p.pulau}</td>
                    <td className={`py-2.5 px-3 text-right font-bold ${selectedLayer === 'tpt' ? 'bg-primary/10 text-primary' : 'text-cyan-600 dark:text-cyan-400'}`}>{p.tpt.toFixed(2)}%</td>
                    <td className={`py-2.5 px-3 text-right ${selectedLayer === 'informal' ? 'bg-primary/10 font-bold text-primary' : 'text-amber-600 dark:text-amber-400'}`}>{p.informal.toFixed(2)}%</td>
                    <td className="py-2.5 px-3 text-right text-foreground">Rp{p.upah.toLocaleString('id-ID')}</td>
                    <td className="py-2.5 px-3 text-right text-muted-foreground">{p.mismatch.toFixed(2)}x</td>
                    <td className={`py-2.5 px-3 text-right font-mono ${selectedLayer === 'ikkd' ? 'bg-primary/10 font-bold text-primary' : 'text-foreground'}`}>{p.ikkd_score.toFixed(1)}</td>
                    <td className={`py-2.5 px-3 font-sans ${selectedLayer === 'cluster' ? 'bg-primary/10' : ''}`}>
                      <span className="px-2 py-0.5 rounded text-2xs bg-muted border border-border text-foreground">
                        Klaster {p.cluster_id}
                      </span>
                    </td>
                    <td className={`py-2.5 px-3 font-sans text-2xs ${selectedLayer === 'lisa' ? 'bg-primary/10 font-bold text-foreground' : 'text-muted-foreground'}`}>{p.lisa_quad}</td>
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
