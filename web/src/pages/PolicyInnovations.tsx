import React, { useState, useMemo } from 'react';
import { 
  AlertTriangle, 
  GraduationCap, 
  Compass, 
  Search, 
  CheckCircle2, 
  ArrowRight, 
  Building2, 
  ShieldCheck, 
  Factory,
  Sparkles
} from 'lucide-react';
import { LaborDataBundle, KabKotaKerentanan, VocationTrack } from '../types';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';

interface PolicyInnovationsProps {
  data: LaborDataBundle;
}

export const PolicyInnovations: React.FC<PolicyInnovationsProps> = ({ data }) => {
  const { policy_innovations, provinces } = data;
  const { ikkd_early_warning, dual_vocation, job_matching_kur } = policy_innovations;

  // Active Sub-Tab
  const [activeTab, setActiveTab] = useState<'early_warning' | 'dual_vocation' | 'job_matching'>('early_warning');

  // Sub-Tab 1: Early Warning State
  const [scopeFilter, setScopeFilter] = useState<'kabkota' | 'provinsi'>('kabkota');
  const [alertFilter, setAlertFilter] = useState<string>('Semua');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedKabKota, setSelectedKabKota] = useState<KabKotaKerentanan>(
    ikkd_early_warning.kabkota_prioritas[0]
  );

  // Sub-Tab 2: Dual Vocation State
  const [selectedTrack, setSelectedTrack] = useState<VocationTrack>(dual_vocation.tracks[0]);
  const [theoryPct, setTheoryPct] = useState<number>(dual_vocation.default_ratio.theory_pct); // default 50
  const industryPct = 100 - theoryPct;

  // Dynamic calculation for Dual-Vocation
  const { benchmark_impact } = dual_vocation;
  // Progress towards 50:50 ratio or beyond
  const practiceGain = (industryPct - benchmark_impact.status_quo_practice_pct) / 
    (benchmark_impact.status_quo_theory_pct - benchmark_impact.status_quo_practice_pct);
  
  const simulatedReadiness = Math.min(96, Math.max(45, Math.round(
    benchmark_impact.baseline_job_readiness_pct + 
    practiceGain * (benchmark_impact.target_job_readiness_pct - benchmark_impact.baseline_job_readiness_pct)
  )));

  const simulatedWaitMonths = Math.max(1.5, Math.round(
    (benchmark_impact.baseline_waiting_months - 
      practiceGain * (benchmark_impact.baseline_waiting_months - benchmark_impact.target_waiting_months)) * 10
  ) / 10);

  // Sub-Tab 3: Job Matching & KUR State
  const [selectedRadius, setSelectedRadius] = useState<number>(job_matching_kur.radius_options_km[1]); // 25 km
  const [vacancyClusterFilter, setVacancyClusterFilter] = useState<number | 'Semua'>('Semua');
  
  // KUR Simulator sliders
  const [kurBeneficiaries, setKurBeneficiaries] = useState<number>(120); // entrepreneurs
  const [kurLoanAmount, setKurLoanAmount] = useState<number>(job_matching_kur.kur_parameters.default_loan_idr); // Rp 35 Juta
  const [kurTenor, setKurTenor] = useState<number>(24); // months

  const totalCapitalDisbursed = kurBeneficiaries * kurLoanAmount;
  const jobsCreatedEstimate = Math.round(
    (totalCapitalDisbursed / 100000000) * job_matching_kur.kur_parameters.jobs_created_multiplier_per_100m
  );
  const annualInterestSubsidy = Math.round(
    (totalCapitalDisbursed * (job_matching_kur.kur_parameters.subsidy_interest_pct / 100))
  );

  // Filtered Kab/Kota
  const filteredKabKota = useMemo(() => {
    return ikkd_early_warning.kabkota_prioritas.filter((k) => {
      const matchSearch = k.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          k.provinsi.toLowerCase().includes(searchQuery.toLowerCase());
      const matchAlert = alertFilter === 'Semua' || k.alert_level === alertFilter;
      return matchSearch && matchAlert;
    });
  }, [ikkd_early_warning.kabkota_prioritas, searchQuery, alertFilter]);

  // Filtered Provinces for IKKD view
  const filteredProvinces = useMemo(() => {
    return provinces.filter((p) => {
      const matchSearch = p.name.toLowerCase().includes(searchQuery.toLowerCase());
      const pAlert = p.ikkd_score >= 70 ? 'CRITICAL' : p.ikkd_score >= 45 ? 'WARNING' : 'SAFE';
      const matchAlert = alertFilter === 'Semua' || pAlert === alertFilter;
      return matchSearch && matchAlert;
    });
  }, [provinces, searchQuery, alertFilter]);

  // Filtered Vacancies
  const filteredVacancies = useMemo(() => {
    return job_matching_kur.vacancies.filter((v) => {
      const matchRadius = v.radius_km <= selectedRadius;
      const matchCluster = vacancyClusterFilter === 'Semua' || v.cluster_id === vacancyClusterFilter;
      return matchRadius && matchCluster;
    });
  }, [job_matching_kur.vacancies, selectedRadius, vacancyClusterFilter]);

  return (
    <div className="space-y-10 animate-fade-in">
      {/* Header */}
      <div className="border-b border-border pb-6 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 text-xs font-mono text-cyan-600 dark:text-cyan-400 mb-2">
            <Sparkles className="size-3.5" />
            <span className="font-semibold uppercase tracking-wider">MODUL 6 : FITUR KUNCI INOVASI KEBIJAKAN</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-extrabold text-foreground tracking-tight">
            Tiga Solusi Operasional Terintegrasi
          </h1>
          <p className="text-sm text-muted-foreground mt-1 max-w-3xl">
            Pengejawantahan actionable roadmap ACTION 2026: Sistem peringatan dini kerentanan kerja lokal, transformasi kurikulum vokasi berbasis industri 50:50, dan bursa kerja geospasial terintegrasi modal tanpa agunan.
          </p>
        </div>

        {/* Action Pills Navigator */}
        <div className="flex flex-wrap gap-2 p-1.5 rounded-xl bg-muted/60 border border-border">
          <Button
            size="sm"
            variant={activeTab === 'early_warning' ? 'default' : 'ghost'}
            onClick={() => setActiveTab('early_warning')}
            className="text-xs gap-1.5 h-8 font-medium cursor-pointer"
          >
            <AlertTriangle className="size-3.5" />
            <span>1. Early Warning IKKD</span>
          </Button>
          <Button
            size="sm"
            variant={activeTab === 'dual_vocation' ? 'default' : 'ghost'}
            onClick={() => setActiveTab('dual_vocation')}
            className="text-xs gap-1.5 h-8 font-medium cursor-pointer"
          >
            <GraduationCap className="size-3.5" />
            <span>2. Dual-Vocation (50:50)</span>
          </Button>
          <Button
            size="sm"
            variant={activeTab === 'job_matching' ? 'default' : 'ghost'}
            onClick={() => setActiveTab('job_matching')}
            className="text-xs gap-1.5 h-8 font-medium cursor-pointer"
          >
            <Compass className="size-3.5" />
            <span>3. Geo-Matching & KUR</span>
          </Button>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* SUB-MODUL 1: EARLY WARNING DASHBOARD IKKD */}
      {/* ========================================================================= */}
      {activeTab === 'early_warning' && (
        <div className="space-y-8 animate-fade-in">
          {/* Executive KPI Summary */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="p-5 rounded-xl bg-card border border-border shadow-xs space-y-1">
              <span className="text-xs font-mono text-muted-foreground block">Daerah Sangat Rentan</span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl font-extrabold text-red-500 font-mono">
                  {scopeFilter === 'kabkota' 
                    ? ikkd_early_warning.kabkota_summary.critical_count 
                    : ikkd_early_warning.provinces_summary.critical_count}
                </span>
                <span className="text-xs text-muted-foreground">Wilayah (IKKD &ge; 70)</span>
              </div>
              <Badge variant="destructive" className="text-[10px] mt-2">
                Red Alert (Intervensi Cepat)
              </Badge>
            </div>

            <div className="p-5 rounded-xl bg-card border border-border shadow-xs space-y-1">
              <span className="text-xs font-mono text-muted-foreground block">Daerah Waspada</span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl font-extrabold text-amber-500 font-mono">
                  {scopeFilter === 'kabkota' 
                    ? ikkd_early_warning.kabkota_summary.warning_count 
                    : ikkd_early_warning.provinces_summary.warning_count}
                </span>
                <span className="text-xs text-muted-foreground">Wilayah (45-70)</span>
              </div>
              <Badge variant="secondary" className="text-[10px] mt-2 bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/30">
                Amber Alert (Pengawasan)
              </Badge>
            </div>

            <div className="p-5 rounded-xl bg-card border border-border shadow-xs space-y-1">
              <span className="text-xs font-mono text-muted-foreground block">Daerah Resilien</span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl font-extrabold text-emerald-500 font-mono">
                  {scopeFilter === 'kabkota' 
                    ? ikkd_early_warning.kabkota_summary.safe_count 
                    : ikkd_early_warning.provinces_summary.safe_count}
                </span>
                <span className="text-xs text-muted-foreground">Wilayah (&lt; 45)</span>
              </div>
              <Badge variant="secondary" className="text-[10px] mt-2 bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/30">
                Aman & Tangguh
              </Badge>
            </div>

            <div className="p-5 rounded-xl bg-card border border-border shadow-xs space-y-1">
              <span className="text-xs font-mono text-muted-foreground block">Dimensi Utama IKKD</span>
              <div className="text-sm font-semibold text-foreground mt-1">
                4 Pilar Komposit
              </div>
              <span className="text-xs text-muted-foreground block">
                Bobot: Informal (35%), TPT (25%), Upah (20%), Underemp (20%)
              </span>
            </div>
          </div>

          {/* Interactive Inspection Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* List & Filter (2 Cols) */}
            <div className="lg:col-span-2 space-y-4">
              <div className="p-5 rounded-2xl bg-card border border-border space-y-4 shadow-xs">
                {/* Controls Bar */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono text-muted-foreground">Tingkat Wilayah:</span>
                    <div className="inline-flex rounded-lg bg-muted p-1 border border-border">
                      <button
                        onClick={() => setScopeFilter('kabkota')}
                        className={`px-2.5 py-1 text-xs rounded-md font-medium transition-colors ${
                          scopeFilter === 'kabkota' ? 'bg-background text-foreground shadow-xs font-bold' : 'text-muted-foreground hover:text-foreground'
                        }`}
                      >
                        Kab/Kota Prioritas ({ikkd_early_warning.kabkota_prioritas.length})
                      </button>
                      <button
                        onClick={() => setScopeFilter('provinsi')}
                        className={`px-2.5 py-1 text-xs rounded-md font-medium transition-colors ${
                          scopeFilter === 'provinsi' ? 'bg-background text-foreground shadow-xs font-bold' : 'text-muted-foreground hover:text-foreground'
                        }`}
                      >
                        38 Provinsi BPS
                      </button>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono text-muted-foreground">Status:</span>
                    <div className="flex gap-1">
                      {['Semua', 'CRITICAL', 'WARNING', 'SAFE'].map((lvl) => (
                        <button
                          key={lvl}
                          onClick={() => setAlertFilter(lvl)}
                          className={`px-2 py-0.5 rounded text-xs font-mono transition-colors ${
                            alertFilter === lvl 
                              ? 'bg-primary text-primary-foreground font-bold' 
                              : 'bg-muted text-muted-foreground hover:text-foreground'
                          }`}
                        >
                          {lvl === 'CRITICAL' ? 'Bahaya' : lvl === 'WARNING' ? 'Waspada' : lvl === 'SAFE' ? 'Aman' : 'Semua'}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Search Bar */}
                <div className="relative">
                  <Search className="absolute left-3 top-2.5 size-4 text-muted-foreground" />
                  <input
                    type="text"
                    placeholder="Cari kabupaten, kota, atau provinsi..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-9 pr-4 py-2 text-xs rounded-lg bg-muted/50 border border-border focus:outline-hidden focus:ring-1 focus:ring-primary text-foreground placeholder:text-muted-foreground"
                  />
                </div>

                {/* Table View */}
                <div className="max-h-[460px] overflow-y-auto rounded-xl border border-border">
                  <table className="w-full text-xs text-left">
                    <thead className="sticky top-0 bg-muted text-muted-foreground font-mono text-2xs uppercase border-b border-border">
                      <tr>
                        <th className="py-2.5 px-3">Wilayah</th>
                        <th className="py-2.5 px-3">Status</th>
                        <th className="py-2.5 px-3 text-right">Skor IKKD</th>
                        <th className="py-2.5 px-3 text-right">Informal</th>
                        <th className="py-2.5 px-3 text-right">TPT</th>
                        <th className="py-2.5 px-3 text-center">Aksi</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-border font-mono">
                      {scopeFilter === 'kabkota' ? (
                        filteredKabKota.map((k) => {
                          const isSelected = selectedKabKota.name === k.name;
                          return (
                            <tr
                              key={k.name}
                              onClick={() => setSelectedKabKota(k)}
                              className={`cursor-pointer transition-colors ${
                                isSelected ? 'bg-primary/10 font-semibold' : 'hover:bg-muted/40'
                              }`}
                            >
                              <td className="py-2.5 px-3 font-sans">
                                <span className="font-semibold text-foreground block">{k.name}</span>
                                <span className="text-2xs text-muted-foreground font-mono">{k.provinsi} (K{k.cluster_id})</span>
                              </td>
                              <td className="py-2.5 px-3">
                                <Badge
                                  variant="secondary"
                                  className={`text-[10px] px-1.5 py-0 ${
                                    k.alert_level === 'CRITICAL'
                                      ? 'bg-red-500/15 text-red-600 dark:text-red-400 border-red-500/30'
                                      : k.alert_level === 'WARNING'
                                      ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/30'
                                      : 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/30'
                                  }`}
                                >
                                  {k.alert_level === 'CRITICAL' ? 'Bahaya' : k.alert_level === 'WARNING' ? 'Waspada' : 'Aman'}
                                </Badge>
                              </td>
                              <td className="py-2.5 px-3 text-right font-bold text-foreground">
                                {k.ikkd_score.toFixed(1)}
                              </td>
                              <td className="py-2.5 px-3 text-right text-amber-600 dark:text-amber-400">
                                {k.informalitas}%
                              </td>
                              <td className="py-2.5 px-3 text-right text-cyan-600 dark:text-cyan-400">
                                {k.tpt}%
                              </td>
                              <td className="py-2.5 px-3 text-center">
                                <button className="p-1 rounded hover:bg-muted text-muted-foreground hover:text-foreground">
                                  <ArrowRight className="size-3.5" />
                                </button>
                              </td>
                            </tr>
                          );
                        })
                      ) : (
                        filteredProvinces.map((p) => {
                          const pAlert = p.ikkd_score >= 70 ? 'CRITICAL' : p.ikkd_score >= 45 ? 'WARNING' : 'SAFE';
                          return (
                            <tr key={p.name} className="hover:bg-muted/40 transition-colors">
                              <td className="py-2.5 px-3 font-sans">
                                <span className="font-semibold text-foreground block">{p.name}</span>
                                <span className="text-2xs text-muted-foreground font-mono">Pulau {p.pulau} (K{p.cluster_id})</span>
                              </td>
                              <td className="py-2.5 px-3">
                                <Badge
                                  variant="secondary"
                                  className={`text-[10px] px-1.5 py-0 ${
                                    pAlert === 'CRITICAL'
                                      ? 'bg-red-500/15 text-red-600 dark:text-red-400 border-red-500/30'
                                      : pAlert === 'WARNING'
                                      ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/30'
                                      : 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/30'
                                  }`}
                                >
                                  {pAlert === 'CRITICAL' ? 'Bahaya' : pAlert === 'WARNING' ? 'Waspada' : 'Aman'}
                                </Badge>
                              </td>
                              <td className="py-2.5 px-3 text-right font-bold text-foreground">
                                {p.ikkd_score.toFixed(1)}
                              </td>
                              <td className="py-2.5 px-3 text-right text-amber-600 dark:text-amber-400">
                                {p.informal}%
                              </td>
                              <td className="py-2.5 px-3 text-right text-cyan-600 dark:text-cyan-400">
                                {p.tpt}%
                              </td>
                              <td className="py-2.5 px-3 text-center text-muted-foreground text-2xs">
                                38 Prov
                              </td>
                            </tr>
                          );
                        })
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Diagnostic Radar & Action Trigger Card (1 Col) */}
            <div className="p-6 rounded-2xl bg-card border border-border shadow-xs space-y-6 flex flex-col justify-between">
              <div className="space-y-4">
                <div className="border-b border-border pb-3">
                  <div className="flex items-center justify-between">
                    <span className="text-2xs font-mono text-muted-foreground uppercase">Inspeksi Kerentanan</span>
                    <Badge
                      variant="secondary"
                      className={`text-[10px] ${
                        selectedKabKota.alert_level === 'CRITICAL'
                          ? 'bg-red-500/20 text-red-600 dark:text-red-400'
                          : selectedKabKota.alert_level === 'WARNING'
                          ? 'bg-amber-500/20 text-amber-600 dark:text-amber-400'
                          : 'bg-emerald-500/20 text-emerald-600 dark:text-emerald-400'
                      }`}
                    >
                      {selectedKabKota.kategori}
                    </Badge>
                  </div>
                  <h3 className="text-xl font-bold text-foreground mt-1">{selectedKabKota.name}</h3>
                  <span className="text-xs text-muted-foreground">{selectedKabKota.provinsi} • Klaster {selectedKabKota.cluster_id}</span>
                </div>

                {/* Score Dial */}
                <div className="p-4 rounded-xl bg-muted/40 border border-border text-center space-y-1">
                  <span className="text-xs text-muted-foreground font-sans">Skor Indeks IKKD (0-100)</span>
                  <div className="text-4xl font-extrabold font-mono text-foreground">
                    {selectedKabKota.ikkd_score.toFixed(1)}
                  </div>
                  <span className="text-2xs text-muted-foreground block font-mono">
                    {selectedKabKota.alert_level === 'CRITICAL' 
                      ? 'Ambang Bahaya: Ketergantungan Ekstrem Sektor Rentan' 
                      : selectedKabKota.alert_level === 'WARNING'
                      ? 'Ambang Waspada: Transisi Informal & Volatilitas Upah'
                      : 'Kondisi Relatif Resilien & Pasar Kerja Formal Kuat'}
                  </span>
                </div>

                {/* 4 Pillars Progress Bars */}
                <div className="space-y-3 pt-2">
                  <span className="text-xs font-mono text-muted-foreground uppercase block">
                    Anatomi 4 Dimensi Kerentanan:
                  </span>
                  
                  {/* Informalitas */}
                  <div className="space-y-1 text-xs">
                    <div className="flex justify-between font-mono">
                      <span className="text-muted-foreground">Informalitas (Bobot 35%):</span>
                      <span className="font-bold text-amber-600 dark:text-amber-400">{selectedKabKota.informalitas}%</span>
                    </div>
                    <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                      <div className="bg-amber-500 h-full rounded-full" style={{ width: `${selectedKabKota.informalitas}%` }} />
                    </div>
                  </div>

                  {/* TPT */}
                  <div className="space-y-1 text-xs">
                    <div className="flex justify-between font-mono">
                      <span className="text-muted-foreground">TPT Terbuka (Bobot 25%):</span>
                      <span className="font-bold text-cyan-600 dark:text-cyan-400">{selectedKabKota.tpt}%</span>
                    </div>
                    <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                      <div className="bg-cyan-500 h-full rounded-full" style={{ width: `${Math.min(100, selectedKabKota.tpt * 8)}%` }} />
                    </div>
                  </div>

                  {/* Defisit Upah */}
                  <div className="space-y-1 text-xs">
                    <div className="flex justify-between font-mono">
                      <span className="text-muted-foreground">Defisit Upah Riil (Bobot 20%):</span>
                      <span className="font-bold text-red-500">{selectedKabKota.defisit_upah_pct}%</span>
                    </div>
                    <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                      <div className="bg-red-500 h-full rounded-full" style={{ width: `${Math.min(100, selectedKabKota.defisit_upah_pct * 1.3)}%` }} />
                    </div>
                  </div>

                  {/* Underemployment */}
                  <div className="space-y-1 text-xs">
                    <div className="flex justify-between font-mono">
                      <span className="text-muted-foreground">Setengah Penganggur (Bobot 20%):</span>
                      <span className="font-bold text-foreground">{selectedKabKota.underemployment}%</span>
                    </div>
                    <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                      <div className="bg-foreground/60 h-full rounded-full" style={{ width: `${selectedKabKota.underemployment}%` }} />
                    </div>
                  </div>
                </div>
              </div>

              {/* Rapid Action Trigger Box */}
              <div className="p-4 rounded-xl bg-primary/10 border border-primary/20 space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold text-primary">
                  <ShieldCheck className="size-4" />
                  <span>Rekomendasi Intervensi Cepat:</span>
                </div>
                <p className="text-xs text-foreground/90 leading-relaxed font-sans">
                  {selectedKabKota.rekomendasi}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* SUB-MODUL 2: DUAL-VOCATION CREDIT SYSTEM */}
      {/* ========================================================================= */}
      {activeTab === 'dual_vocation' && (
        <div className="space-y-8 animate-fade-in">
          {/* Header Banner */}
          <div className="p-6 rounded-2xl bg-card border border-border shadow-xs flex flex-col lg:flex-row lg:items-center justify-between gap-6">
            <div className="space-y-2 max-w-2xl">
              <Badge variant="outline" className="text-xs font-mono text-cyan-600 dark:text-cyan-400 border-cyan-500/30">
                Pilar 2 : Kurikulum Modular & Akreditasi Industri
              </Badge>
              <h2 className="text-xl sm:text-2xl font-bold text-foreground">
                Dual-Vocation Credit System (50:50)
              </h2>
              <p className="text-xs sm:text-sm text-muted-foreground leading-relaxed">
                Mendekonstruksi kurikulum vokasi SMK dan politeknik dari dominasi teori kelas menjadi 50% teori terapan dan 50% praktik terakreditasi langsung di lini produksi industri mitra, didukung insentif super-tax deduction 200%.
              </p>
            </div>

            {/* Standard accreditation badge */}
            <div className="p-4 rounded-xl bg-muted/40 border border-border text-xs space-y-1.5 font-mono">
              <span className="text-muted-foreground block text-2xs uppercase">Standar Akreditasi:</span>
              <span className="font-bold text-foreground block text-xs">{dual_vocation.accreditation_standard}</span>
              <span className="text-emerald-500 text-2xs flex items-center gap-1">
                <CheckCircle2 className="size-3" /> Insentif Pajak Super-Deduction 200% (PMK 128/2019)
              </span>
            </div>
          </div>

          {/* Interactive Simulation Dashboard (Ratio Slider) */}
          <div className="p-6 rounded-2xl bg-muted/30 border border-border shadow-xs space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block">
                  Simulator Proporsi Pembelajaran Modular:
                </span>
                <h3 className="text-lg font-bold text-foreground">
                  Uji Dampak Kesiapan Kerja & Durasi Tunggu Lulusan
                </h3>
              </div>

              <div className="flex items-center gap-2">
                <Button
                  size="sm"
                  variant="outline"
                  onClick={() => setTheoryPct(70)}
                  className="text-2xs font-mono h-7"
                >
                  Status Quo (70:30)
                </Button>
                <Button
                  size="sm"
                  variant="default"
                  onClick={() => setTheoryPct(50)}
                  className="text-2xs font-mono h-7"
                >
                  Standar Dual (50:50)
                </Button>
              </div>
            </div>

            {/* Sliders Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
              <div className="lg:col-span-2 space-y-4">
                <div className="space-y-2">
                  <div className="flex justify-between text-xs font-mono">
                    <span className="text-foreground font-semibold">
                      Teori Kelas / Kampus: <strong className="text-cyan-600 dark:text-cyan-400">{theoryPct}%</strong>
                    </span>
                    <span className="text-foreground font-semibold">
                      Praktik Industri Mitra: <strong className="text-emerald-600 dark:text-emerald-400">{industryPct}%</strong>
                    </span>
                  </div>

                  <input
                    type="range"
                    min="30"
                    max="70"
                    step="5"
                    value={theoryPct}
                    onChange={(e) => setTheoryPct(parseInt(e.target.value))}
                    className="w-full h-2.5 bg-muted rounded-lg appearance-none cursor-pointer accent-cyan-500 border border-border"
                  />

                  <div className="flex justify-between text-2xs font-mono text-muted-foreground">
                    <span>30% Teori (70% Industri)</span>
                    <span className="font-bold text-primary">50% : 50% (Rekomendasi Optimal)</span>
                    <span>70% Teori (Status Quo)</span>
                  </div>
                </div>

                <div className="p-3 rounded-lg bg-card border border-border text-xs text-muted-foreground leading-relaxed">
                  Formula simulasi menghubungkan rasio jam praktik industri riil dengan peningkatan skor kecakapan SKKNI dan penurunan durasi friksi pencarian kerja (*job-search spell*).
                </div>
              </div>

              {/* Real-Time Impact Metric Cards */}
              <div className="grid grid-cols-2 gap-3">
                <div className="p-4 rounded-xl bg-card border border-border text-center space-y-1">
                  <span className="text-2xs font-mono text-muted-foreground block">Indeks Kesiapan Kerja</span>
                  <div className="text-3xl font-extrabold font-mono text-emerald-500">
                    {simulatedReadiness}%
                  </div>
                  <span className="text-[10px] text-muted-foreground block font-mono">
                    Baseline: {benchmark_impact.baseline_job_readiness_pct}% (+{(simulatedReadiness - benchmark_impact.baseline_job_readiness_pct).toFixed(1)}%)
                  </span>
                </div>

                <div className="p-4 rounded-xl bg-card border border-border text-center space-y-1">
                  <span className="text-2xs font-mono text-muted-foreground block">Rata Waktu Tunggu</span>
                  <div className="text-3xl font-extrabold font-mono text-cyan-600 dark:text-cyan-400">
                    {simulatedWaitMonths} Bln
                  </div>
                  <span className="text-[10px] text-muted-foreground block font-mono">
                    Baseline: {benchmark_impact.baseline_waiting_months} Bln (-{(benchmark_impact.baseline_waiting_months - simulatedWaitMonths).toFixed(1)} bln)
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* 4 Tracks Navigation */}
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <span className="text-xs font-mono text-muted-foreground uppercase block">
                  Pilihan Jalur Spesialisasi Modular:
                </span>
                <h3 className="text-lg font-bold text-foreground">
                  Struktur Kurikulum Modular Terverifikasi Industri
                </h3>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              {dual_vocation.tracks.map((t) => {
                const isSelected = selectedTrack.id === t.id;
                return (
                  <button
                    key={t.id}
                    onClick={() => setSelectedTrack(t)}
                    className={`p-4 rounded-xl text-left border transition-all cursor-pointer ${
                      isSelected
                        ? 'bg-card border-primary ring-1 ring-primary shadow-xs'
                        : 'bg-card/50 border-border hover:bg-card hover:border-muted-foreground/30'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <Factory className={`size-4 ${isSelected ? 'text-primary' : 'text-muted-foreground'}`} />
                      {isSelected && <Badge className="text-[10px] py-0">Aktif</Badge>}
                    </div>
                    <span className="font-bold text-sm text-foreground block">{t.name}</span>
                    <span className="text-2xs text-muted-foreground line-clamp-1 mt-1 font-mono">{t.focus_cluster}</span>
                  </button>
                );
              })}
            </div>

            {/* Selected Track Modules Breakdown */}
            <div className="p-6 rounded-2xl bg-card border border-border shadow-xs space-y-6">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-border pb-4">
                <div>
                  <h4 className="text-lg font-bold text-foreground">{selectedTrack.name}</h4>
                  <span className="text-xs text-muted-foreground font-mono">{selectedTrack.focus_cluster}</span>
                </div>
                <div className="text-xs font-mono text-muted-foreground">
                  Alokasi: <strong className="text-cyan-600 dark:text-cyan-400">{theoryPct}% Teori Terapan</strong> • <strong className="text-emerald-600 dark:text-emerald-400">{industryPct}% Praktik Industri</strong>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* 50% Theory Modules */}
                <div className="space-y-3">
                  <div className="flex items-center gap-2">
                    <div className="size-2 rounded-full bg-cyan-500" />
                    <span className="font-bold text-xs uppercase tracking-wider font-mono text-foreground">
                      Blok Modul Teori Terapan (Kampus/SMK)
                    </span>
                  </div>
                  <div className="space-y-2">
                    {selectedTrack.theory_modules.map((m, idx) => (
                      <div key={idx} className="p-3 rounded-lg bg-muted/40 border border-border text-xs flex items-start gap-2.5">
                        <span className="font-mono text-2xs font-bold text-cyan-600 dark:text-cyan-400 mt-0.5">M{idx+1}</span>
                        <div className="space-y-0.5">
                          <span className="font-semibold text-foreground block">{m}</span>
                          <span className="text-2xs text-muted-foreground font-mono">Evaluasi Berbasis Portofolio & Ujian Kompetensi Teori</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* 50% Industry Modules */}
                <div className="space-y-3">
                  <div className="flex items-center gap-2">
                    <div className="size-2 rounded-full bg-emerald-500" />
                    <span className="font-bold text-xs uppercase tracking-wider font-mono text-foreground">
                      Blok Modul Praktik Industri Terakreditasi
                    </span>
                  </div>
                  <div className="space-y-2">
                    {selectedTrack.industry_modules.map((m, idx) => (
                      <div key={idx} className="p-3 rounded-lg bg-muted/40 border border-border text-xs flex items-start gap-2.5">
                        <span className="font-mono text-2xs font-bold text-emerald-600 dark:text-emerald-400 mt-0.5">P{idx+1}</span>
                        <div className="space-y-0.5">
                          <span className="font-semibold text-foreground block">{m}</span>
                          <span className="text-2xs text-muted-foreground font-mono">Verifikasi On-Site oleh Supervisor Pabrik / Konsorsium</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Industry Partners */}
              <div className="pt-2 border-t border-border flex flex-wrap items-center gap-2">
                <span className="text-xs font-mono text-muted-foreground">Konsorsium Industri Terkait:</span>
                {selectedTrack.industry_partners.map((p, idx) => (
                  <Badge key={idx} variant="secondary" className="text-xs font-mono font-normal">
                    <Building2 className="size-3 mr-1 text-muted-foreground" />
                    {p}
                  </Badge>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* SUB-MODUL 3: GEO-SPATIAL JOB MATCHING & KUR KLASTER */}
      {/* ========================================================================= */}
      {activeTab === 'job_matching' && (
        <div className="space-y-8 animate-fade-in">
          {/* Header Banner */}
          <div className="p-6 rounded-2xl bg-card border border-border shadow-xs flex flex-col lg:flex-row lg:items-center justify-between gap-6">
            <div className="space-y-2 max-w-2xl">
              <Badge variant="outline" className="text-xs font-mono text-emerald-600 dark:text-emerald-400 border-emerald-500/30">
                Pilar 3 : Bursa Tenaga Kerja Lokal & Permodalan Mikro
              </Badge>
              <h2 className="text-xl sm:text-2xl font-bold text-foreground">
                Geo-Spatial Job Matching & KUR Klaster
              </h2>
              <p className="text-xs sm:text-sm text-muted-foreground leading-relaxed">
                Melokalisasi ekosistem bursa kerja pemuda berbasis radius geospasial guna mereduksi biaya transportasi pekerja, diintegrasikan langsung dengan pembiayaan Kredit Usaha Rakyat (KUR) Klaster tanpa agunan bagi wirausaha muda terdidik.
              </p>
            </div>

            {/* Quick Metrics */}
            <div className="p-4 rounded-xl bg-muted/40 border border-border text-xs space-y-1 font-mono">
              <span className="text-muted-foreground block text-2xs uppercase">Skema Pembiayaan Mikro:</span>
              <span className="font-bold text-foreground block text-xs">KUR Klaster Produktif 0% Agunan Fisik</span>
              <span className="text-cyan-500 text-2xs block">
                Subsidi Bunga Pemerintah 6% • Plafon s.d. Rp 100 Juta
              </span>
            </div>
          </div>

          {/* Two-Column Working Surface */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Column 1: Localized Geo-Spatial Vacancies */}
            <div className="space-y-5">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 uppercase tracking-wider block">
                    Bursa Kerja Pemuda Terlokalisasi:
                  </span>
                  <h3 className="text-base font-bold text-foreground">
                    Lowongan Industri dalam Radius Terdekat
                  </h3>
                </div>

                {/* Radius Filter */}
                <div className="flex items-center gap-1.5">
                  <span className="text-xs font-mono text-muted-foreground">Radius:</span>
                  {job_matching_kur.radius_options_km.map((rad) => (
                    <button
                      key={rad}
                      onClick={() => setSelectedRadius(rad)}
                      className={`px-2.5 py-1 text-xs rounded-lg font-mono transition-colors ${
                        selectedRadius === rad
                          ? 'bg-primary text-primary-foreground font-bold'
                          : 'bg-muted text-muted-foreground hover:text-foreground'
                      }`}
                    >
                      &le; {rad} km
                    </button>
                  ))}
                </div>
              </div>

              {/* Vacancy Cluster Filters */}
              <div className="flex gap-1.5 flex-wrap">
                <button
                  onClick={() => setVacancyClusterFilter('Semua')}
                  className={`px-2.5 py-1 text-2xs rounded-md font-mono ${
                    vacancyClusterFilter === 'Semua' ? 'bg-foreground text-background font-bold' : 'bg-muted text-muted-foreground'
                  }`}
                >
                  Semua Klaster ({job_matching_kur.vacancies.length})
                </button>
                <button
                  onClick={() => setVacancyClusterFilter(1)}
                  className={`px-2.5 py-1 text-2xs rounded-md font-mono ${
                    vacancyClusterFilter === 1 ? 'bg-red-500 text-white font-bold' : 'bg-muted text-muted-foreground'
                  }`}
                >
                  Klaster 1 Urban
                </button>
                <button
                  onClick={() => setVacancyClusterFilter(2)}
                  className={`px-2.5 py-1 text-2xs rounded-md font-mono ${
                    vacancyClusterFilter === 2 ? 'bg-amber-500 text-white font-bold' : 'bg-muted text-muted-foreground'
                  }`}
                >
                  Klaster 2 Agraris
                </button>
                <button
                  onClick={() => setVacancyClusterFilter(3)}
                  className={`px-2.5 py-1 text-2xs rounded-md font-mono ${
                    vacancyClusterFilter === 3 ? 'bg-emerald-500 text-white font-bold' : 'bg-muted text-muted-foreground'
                  }`}
                >
                  Klaster 3 Transisi
                </button>
              </div>

              {/* Vacancy Card List */}
              <div className="space-y-3 max-h-[500px] overflow-y-auto pr-1">
                {filteredVacancies.map((v) => (
                  <div
                    key={v.id}
                    className="p-4 rounded-xl bg-card border border-border shadow-xs hover:border-muted-foreground/30 transition-all space-y-2.5"
                  >
                    <div className="flex items-start justify-between gap-2">
                      <div>
                        <span className="font-bold text-sm text-foreground block">{v.title}</span>
                        <span className="text-xs text-muted-foreground font-sans">{v.company}</span>
                      </div>
                      <Badge
                        variant="secondary"
                        className={`text-[10px] font-mono shrink-0 ${
                          v.cluster_id === 1 ? 'border-red-500/30 text-red-500' :
                          v.cluster_id === 2 ? 'border-amber-500/30 text-amber-500' :
                          'border-emerald-500/30 text-emerald-500'
                        }`}
                      >
                        Radius {v.radius_km} km
                      </Badge>
                    </div>

                    <div className="flex flex-wrap items-center gap-3 text-xs text-muted-foreground font-mono">
                      <span>{v.location}</span>
                      <span>•</span>
                      <strong className="text-foreground">{v.salary_range}</strong>
                      <span>•</span>
                      <span className="text-cyan-600 dark:text-cyan-400 font-semibold">Kuota: {v.quota} orang</span>
                    </div>

                    <div className="pt-2 border-t border-border flex items-center justify-between text-2xs">
                      <span className="text-muted-foreground font-sans">
                        Kebutuhan: <strong className="text-foreground">{v.required_skill}</strong>
                      </span>
                      <span className="font-mono text-emerald-600 dark:text-emerald-400 font-bold">
                        {v.matched_candidates} Kandidat Terhubung
                      </span>
                    </div>
                  </div>
                ))}

                {filteredVacancies.length === 0 && (
                  <div className="p-8 text-center text-xs text-muted-foreground border border-dashed border-border rounded-xl">
                    Tidak ada lowongan pada radius dan klaster yang dipilih. Perlebar radius pencarian.
                  </div>
                )}
              </div>
            </div>

            {/* Column 2: Interactive KUR Klaster Simulator */}
            <div className="p-6 rounded-2xl bg-card border border-border shadow-xs space-y-6 flex flex-col justify-between">
              <div className="space-y-5">
                <div className="border-b border-border pb-3">
                  <span className="text-xs font-mono text-emerald-600 dark:text-emerald-400 uppercase tracking-wider block">
                    Kalkulator Pembiayaan Mikro:
                  </span>
                  <h3 className="text-lg font-bold text-foreground">
                    Simulasi Penyaluran KUR Klaster Produktif
                  </h3>
                  <p className="text-xs text-muted-foreground mt-1">
                    Hitung proyeksi penciptaan lapangan kerja pemuda dan kebutuhan fiskal subsidi bunga tanpa jaminan fisik.
                  </p>
                </div>

                {/* Sliders */}
                <div className="space-y-4">
                  {/* Beneficiaries Slider */}
                  <div className="space-y-1.5">
                    <div className="flex justify-between text-xs font-mono">
                      <span className="text-muted-foreground">Jumlah Debitur Wirausaha Pemuda:</span>
                      <span className="font-bold text-foreground">{kurBeneficiaries} Wirausaha</span>
                    </div>
                    <input
                      type="range"
                      min="20"
                      max="500"
                      step="10"
                      value={kurBeneficiaries}
                      onChange={(e) => setKurBeneficiaries(parseInt(e.target.value))}
                      className="w-full h-2 bg-muted rounded-lg appearance-none cursor-pointer accent-emerald-500 border border-border"
                    />
                    <div className="flex justify-between text-2xs font-mono text-muted-foreground">
                      <span>20</span>
                      <span>250</span>
                      <span>500 Orang</span>
                    </div>
                  </div>

                  {/* Loan Amount Slider */}
                  <div className="space-y-1.5">
                    <div className="flex justify-between text-xs font-mono">
                      <span className="text-muted-foreground">Rata-rata Plafon Modal Kerja:</span>
                      <span className="font-bold text-foreground">Rp {(kurLoanAmount / 1000000).toFixed(0)} Juta</span>
                    </div>
                    <input
                      type="range"
                      min="10000000"
                      max="100000000"
                      step="5000000"
                      value={kurLoanAmount}
                      onChange={(e) => setKurLoanAmount(parseInt(e.target.value))}
                      className="w-full h-2 bg-muted rounded-lg appearance-none cursor-pointer accent-emerald-500 border border-border"
                    />
                    <div className="flex justify-between text-2xs font-mono text-muted-foreground">
                      <span>Rp 10 Juta</span>
                      <span>Rp 50 Juta</span>
                      <span>Rp 100 Juta</span>
                    </div>
                  </div>

                  {/* Tenor Options */}
                  <div className="flex items-center justify-between text-xs pt-1">
                    <span className="text-muted-foreground font-mono">Tenor Pinjaman:</span>
                    <div className="flex gap-1.5">
                      {[12, 24, 36].map((t) => (
                        <button
                          key={t}
                          onClick={() => setKurTenor(t)}
                          className={`px-2.5 py-1 text-xs rounded-md font-mono transition-colors ${
                            kurTenor === t 
                              ? 'bg-primary text-primary-foreground font-bold' 
                              : 'bg-muted text-muted-foreground hover:text-foreground'
                          }`}
                        >
                          {t} Bulan
                        </button>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Real-time Calculation Card */}
                <div className="grid grid-cols-2 gap-3 pt-2">
                  <div className="p-3.5 rounded-xl bg-muted/40 border border-border text-center space-y-1">
                    <span className="text-2xs font-mono text-muted-foreground block">Total Modal Bergulir</span>
                    <div className="text-2xl font-bold font-mono text-foreground">
                      Rp {(totalCapitalDisbursed / 1000000000).toFixed(2)} M
                    </div>
                    <span className="text-[10px] text-muted-foreground block font-mono">Disalurkan Bank Himbara</span>
                  </div>

                  <div className="p-3.5 rounded-xl bg-muted/40 border border-border text-center space-y-1">
                    <span className="text-2xs font-mono text-muted-foreground block">Lapangan Kerja Tercipta</span>
                    <div className="text-2xl font-bold font-mono text-emerald-500">
                      +{jobsCreatedEstimate} Orang
                    </div>
                    <span className="text-[10px] text-muted-foreground block font-mono">Multiplier: 2.4 / 100 Jt</span>
                  </div>

                  <div className="p-3.5 rounded-xl bg-muted/40 border border-border text-center space-y-1">
                    <span className="text-2xs font-mono text-muted-foreground block">Beban Subsidi Bunga</span>
                    <div className="text-xl font-bold font-mono text-amber-500">
                      Rp {(annualInterestSubsidy / 1000000).toFixed(0)} Jt/thn
                    </div>
                    <span className="text-[10px] text-muted-foreground block font-mono">Subsidi APBN 6% p.a.</span>
                  </div>

                  <div className="p-3.5 rounded-xl bg-muted/40 border border-border text-center space-y-1">
                    <span className="text-2xs font-mono text-muted-foreground block">Target NPL Kredit</span>
                    <div className="text-xl font-bold font-mono text-cyan-500">
                      &lt; {job_matching_kur.kur_parameters.target_npl_max_pct}%
                    </div>
                    <span className="text-[10px] text-muted-foreground block font-mono">Mitra Penjaminan Daerah</span>
                  </div>
                </div>
              </div>

              {/* KUR Cluster Examples */}
              <div className="space-y-2 pt-3 border-t border-border">
                <span className="text-2xs font-mono text-muted-foreground uppercase block">
                  3 Klaster Wirausaha Pemuda Terbina:
                </span>
                <div className="space-y-1.5">
                  {job_matching_kur.kur_clusters.map((kc) => (
                    <div key={kc.id} className="p-2.5 rounded-lg bg-muted/30 border border-border text-xs flex justify-between items-center">
                      <div>
                        <span className="font-semibold text-foreground block">{kc.name}</span>
                        <span className="text-2xs text-muted-foreground font-mono">{kc.cluster_target} • Rata Pinjaman: {kc.avg_loan}</span>
                      </div>
                      <Badge variant="outline" className="text-[10px] font-mono shrink-0">
                        +{kc.expected_jobs} Pekerja
                      </Badge>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
