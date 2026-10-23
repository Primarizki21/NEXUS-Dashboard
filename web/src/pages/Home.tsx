import React from 'react';
import { 
  ArrowRight, 
  TrendingDown, 
  GraduationCap, 
  ChevronRight
} from 'lucide-react';
import { LaborDataBundle } from '../types';
import { MetricBadge } from '../components/MetricBadge';

interface HomeProps {
  data: LaborDataBundle;
  onNavigate: (tab: string) => void;
}

export const Home: React.FC<HomeProps> = ({ onNavigate }) => {

  return (
    <div className="space-y-16 animate-fade-in">
      {/* Hero Section */}
      <section className="relative pt-8 pb-12 overflow-hidden border-b border-border">
        <div className="max-w-4xl">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 text-xs font-mono mb-6">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-500 dark:bg-cyan-400"></span>
            <span>ACTION 2026 : ANALISIS EKONOMETRIKA & PASAR KERJA BPS</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-foreground leading-tight mb-6">
            Anatomi Pengangguran Terbuka Indonesia. <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-blue-600 dark:from-cyan-400 dark:to-blue-500">
              Menembus Batas Teritorial.
            </span>
          </h1>

          <p className="text-base sm:text-lg text-muted-foreground leading-relaxed mb-8 max-w-3xl">
            Tingkat Pengangguran Terbuka (TPT) nasional resmi turun ke <strong className="text-foreground font-semibold">4,91%</strong> pada Agustus 2024, telah melampaui level pra-pandemi 2019 (5,23%). Namun di balik penurunan tersebut, angka setengah pengangguran melonjak drastis <strong className="text-amber-500 dark:text-amber-400 font-semibold">+23,8%</strong> mencapai <strong className="text-foreground font-semibold">11,56 juta orang</strong>. Kebijakan ketenagakerjaan tidak dapat lagi bertumpu pada satu angka agregat tunggal.
          </p>

          <div className="flex flex-wrap gap-4">
            <button
              onClick={() => onNavigate('cartography')}
              className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold text-sm transition-all shadow-lg shadow-cyan-500/25 cursor-pointer"
            >
              <span>Eksplorasi Kartografi 3 Klaster</span>
              <ArrowRight className="w-4 h-4" />
            </button>
            <button
              onClick={() => onNavigate('simulator')}
              className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-card hover:bg-muted text-foreground border border-border font-semibold text-sm transition-all cursor-pointer"
            >
              <span>Buka Simulator Kebijakan RPJMN</span>
              <ChevronRight className="w-4 h-4 text-muted-foreground" />
            </button>
          </div>
        </div>
      </section>

      {/* Benchmark Strip */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricBadge
          label="TPT Nasional Ags 2024"
          value="4.91%"
          subtext="Turun 0.41 poin vs 2023 (5.32%)"
          variant="cyan"
        />
        <MetricBadge
          label="Lonjakan Setengah Penganggur"
          value="+23.8%"
          subtext="11.56 Juta Orang (Jam < 35 Jam)"
          variant="amber"
        />
        <MetricBadge
          label="Rasio Kerentanan Usia Muda"
          value="6.95x"
          subtext="Pemuda 17.02% vs Dewasa 2.45%"
          variant="rose"
        />
        <MetricBadge
          label="Limpahan Spasial Upah"
          value="+4.43x"
          subtext="SDM Multiplier (LeSage-Pace)"
          variant="emerald"
        />
      </section>

      {/* Dual Paradox Section */}
      <section className="space-y-6">
        <div className="flex items-center justify-between border-b border-border pb-3">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold text-foreground tracking-tight">
              Dua Sisi Anomali Struktural Ketenagakerjaan
            </h2>
            <p className="text-xs text-muted-foreground">
              Bukti empiris resmi Sakernas membongkar ilusi statistik di tingkat agregat nasional.
            </p>
          </div>
          <span className="hidden sm:inline-block text-xs font-mono px-2.5 py-1 rounded bg-muted/60 border border-border text-cyan-600 dark:text-cyan-400">
            Sakernas 2024
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Card 1: Gunung Es Utilisasi Kerja */}
          <div className="p-6 rounded-2xl bg-card border border-border relative overflow-hidden flex flex-col justify-between shadow-xs">
            <div className="space-y-4">
              <div className="flex items-center space-x-3 text-cyan-600 dark:text-cyan-400">
                <div className="p-2.5 rounded-lg bg-cyan-500/10 border border-cyan-500/20">
                  <TrendingDown className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-lg text-foreground">1. Gunung Es Utilisasi Tenaga Kerja (LU2)</h3>
                  <span className="text-xs text-muted-foreground">Fenomena Too Poor to be Unemployed</span>
                </div>
              </div>

              <p className="text-sm text-muted-foreground leading-relaxed">
                Penurunan pengangguran terbuka (-390 ribu orang) tertelan oleh ledakan pekerja setengah penganggur (+2,22 juta orang). Angkatan kerja yang keluar dari status penganggur terbuka tidak berpindah ke pekerjaan formal yang layak, melainkan terlempar ke sektor informal subsisten dengan upah minim dan jam kerja rendah.
              </p>

              <div className="grid grid-cols-3 gap-3 pt-2">
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-2xs font-mono text-muted-foreground uppercase block">TPT Resmi (LU1)</span>
                  <span className="text-lg font-bold text-emerald-500 dark:text-emerald-400 font-mono">4.91%</span>
                  <span className="text-2xs text-muted-foreground block">7.47 Juta Orang</span>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-2xs font-mono text-muted-foreground uppercase block">Setengah Penganggur</span>
                  <span className="text-lg font-bold text-amber-500 dark:text-amber-400 font-mono">7.99%</span>
                  <span className="text-2xs text-muted-foreground block">11.56 Juta Orang</span>
                </div>
                <div className="p-3 rounded-lg bg-muted/40 border border-border">
                  <span className="text-2xs font-mono text-muted-foreground uppercase block">Total Defisit (LU2)</span>
                  <span className="text-lg font-bold text-rose-500 dark:text-rose-400 font-mono">12.51%</span>
                  <span className="text-2xs text-muted-foreground block">19.03 Juta Orang</span>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-border flex items-center justify-between text-xs text-muted-foreground">
              <span>Defisit jam kerja riil naik +0.87 poin vs 2023</span>
              <button 
                onClick={() => onNavigate('cartography')}
                className="text-cyan-600 dark:text-cyan-400 hover:underline font-medium inline-flex items-center space-x-1"
              >
                <span>Lihat Sebaran Provinsi</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Card 2: Paradoks Pendidikan & Pemuda */}
          <div className="p-6 rounded-2xl bg-card border border-border relative overflow-hidden flex flex-col justify-between shadow-xs">
            <div className="space-y-4">
              <div className="flex items-center space-x-3 text-amber-500 dark:text-amber-400">
                <div className="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/20">
                  <GraduationCap className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-lg text-foreground">2. Paradoks Pengangguran Terdidik & Vokasi</h3>
                  <span className="text-xs text-muted-foreground">Skill Mismatch & Stagnasi Manufaktur</span>
                </div>
              </div>

              <p className="text-sm text-muted-foreground leading-relaxed">
                Semakin tinggi jenjang pendidikan kejuruan, tingkat penganggurannya justru semakin tinggi. Lulusan SMK mencatat TPT tertinggi (6,81%), hampir 3,5 kali lipat dibanding lulusan SD ke bawah (1,92%). Sementara itu, TPT sarjana/universitas justru meningkat dari 4,80% (2022) menjadi 5,33% (2024).
              </p>

              <div className="space-y-2 pt-1">
                <div className="flex items-center justify-between text-xs">
                  <span className="text-foreground">SMK Kejuruan (Tertinggi)</span>
                  <span className="font-mono font-bold text-rose-500 dark:text-rose-400">6.81% (3.55x SD)</span>
                </div>
                <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                  <div className="bg-rose-500 h-full rounded-full" style={{ width: '68.1%' }}></div>
                </div>

                <div className="flex items-center justify-between text-xs pt-1">
                  <span className="text-foreground">Universitas (S1+)</span>
                  <span className="font-mono font-bold text-amber-500 dark:text-amber-400">5.33% (Naik +0.53 poin)</span>
                </div>
                <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                  <div className="bg-amber-500 h-full rounded-full" style={{ width: '53.3%' }}></div>
                </div>

                <div className="flex items-center justify-between text-xs pt-1">
                  <span className="text-foreground">SD ke Bawah (Paling Rendah)</span>
                  <span className="font-mono font-bold text-emerald-500 dark:text-emerald-400">1.92% (Subsisten Tani)</span>
                </div>
                <div className="w-full bg-muted rounded-full h-2 overflow-hidden border border-border">
                  <div className="bg-emerald-500 h-full rounded-full" style={{ width: '19.2%' }}></div>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-border flex items-center justify-between text-xs text-muted-foreground">
              <span>Pemuda 15-24 tahun menyumbang 56.70% total penganggur</span>
              <button 
                onClick={() => onNavigate('spatial')}
                className="text-amber-500 dark:text-amber-400 hover:underline font-medium inline-flex items-center space-x-1"
              >
                <span>Uji Ekonometrika Spasial</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* 4-Phase Spatial Story Section */}
      <section className="p-8 rounded-2xl bg-card border border-border space-y-8 shadow-xs">
        <div>
          <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 tracking-wider uppercase block mb-1">
            Alur Penceritaan Spasial
          </span>
          <h2 className="text-2xl font-bold text-foreground tracking-tight">
            Empat Tahapan Analisis Menuju Solusi Kebijakan Terarah
          </h2>
          <p className="text-sm text-muted-foreground mt-1">
            Mengapa pendekatan teritorial terdesentralisasi mutlak diperlukan untuk menyelesaikan pengangguran di Indonesia.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="p-5 rounded-xl bg-muted/40 border border-border space-y-3">
            <div className="w-7 h-7 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-mono font-bold text-xs">
              1
            </div>
            <h4 className="font-bold text-foreground text-sm">Kegagalan Kebijakan Seragam</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Target nasional mengabaikan jurang 5.11 kali lipat antara provinsi tertinggi (Jawa Barat 6.75%) dengan terendah (Papua Pegunungan 1.32%).
            </p>
          </div>

          <div className="p-5 rounded-xl bg-muted/40 border border-border space-y-3">
            <div className="w-7 h-7 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-mono font-bold text-xs">
              2
            </div>
            <h4 className="font-bold text-foreground text-sm">3 Tipologi Klaster Provinsi</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Klasifikasi 38 provinsi ke dalam 3 profil struktural: Urban-Industrial Trap (8), Agraris-Informal Shelter (18), dan Transisi Berimbang (12).
            </p>
          </div>

          <div className="p-5 rounded-xl bg-muted/40 border border-border space-y-3">
            <div className="w-7 h-7 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-mono font-bold text-xs">
              3
            </div>
            <h4 className="font-bold text-foreground text-sm">Limpahan Spasial Antardaerah</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Uji SDM membuktikan efek limpahan upah ke tetangga (+4.43) melampaui efek domestik (+0.38): upah tinggi memicu migrasi antardaerah.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-muted/40 border border-border space-y-3">
            <div className="w-7 h-7 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-mono font-bold text-xs">
              4
            </div>
            <h4 className="font-bold text-foreground text-sm">Target 5.40 Juta Lapangan Kerja</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Intervensi 3 tuas kebijakan presisi untuk mencapai target RPJMN 2025-2029 (TPT nasional 4.30% dan separasi per klaster).
            </p>
          </div>
        </div>
      </section>

      {/* Empirical Pillars Cards (EMP 01 to 05) */}
      <section className="space-y-6">
        <div>
          <span className="text-xs font-mono text-cyan-600 dark:text-cyan-400 tracking-wider uppercase block mb-1">
            Pilar Pembuktian Empiris
          </span>
          <h2 className="text-2xl font-bold text-foreground tracking-tight">
            Ringkasan Statistik & Ekonometrika Teruji
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-cyan-600 dark:text-cyan-400">EMP-01 : Korelasi</span>
              <span className="text-muted-foreground">r = -0.782</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Ilusi Pengangguran Semu</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Korelasi negatif kuat antara TPT dan proporsi informalitas membuktikan rendahnya pengangguran di wilayah tertentu mencerminkan ketiadaan pilihan kerja formal, bukan kemakmuran.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-emerald-600 dark:text-emerald-400">EMP-02 : Autokorelasi</span>
              <span className="text-muted-foreground">I = +0.246 (p=0.012)</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Aglomerasi Spasial Regional</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Uji Moran's I global membuktikan pengangguran terbuka mengelompok secara geografis sepanjang 2017-2024. Episentrum pengangguran berdekatan di koridor barat Jawa dan Papua.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-amber-600 dark:text-amber-400">EMP-03 : Ekonometrika</span>
              <span className="text-muted-foreground">Multiplier 4.43x</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Dekomposisi LeSage-Pace</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Model Spatial Durbin Model (SDM) membuktikan kenaikan upah buruh di suatu provinsi menciptakan limpahan dorongan pencari kerja lintas teritorial yang sangat signifikan.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-rose-600 dark:text-rose-400">EMP-04 : Dikotomi</span>
              <span className="text-muted-foreground">Kota 1.58x vs Desa 1.74x</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Antrean Kota vs Perangkap Desa</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Kawasan kota didominasi penganggur terbuka berpendidikan (5.79%), sedangkan desa didominasi pekerja setengah penganggur subsisten jam kerja rendah (10.60%).
            </p>
          </div>

          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-cyan-600 dark:text-cyan-400">EMP-05 : Validasi Silang</span>
              <span className="text-muted-foreground">MASE = 0.905</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Prinsip Parsimoni Peramalan</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Evaluasi cross-validation multi-horizon membuktikan model Holt Damped Trend mengungguli model autoregresif kompleks yang rawan overfitting terhadap guncangan COVID 2020.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-card border border-border space-y-2 shadow-xs">
            <div className="flex justify-between items-center text-xs">
              <span className="font-mono text-purple-600 dark:text-purple-400">EMP-06 : Panel Seimbang</span>
              <span className="text-muted-foreground">79.58% Between-Prov</span>
            </div>
            <h4 className="font-bold text-foreground text-sm">Variansi Lintas Wilayah</h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              Dekomposisi variansi panel 34 provinsi (272 baris) membuktikan hampir 80% ragam berada antar-wilayah, memberikan justifikasi mutlak bagi pemodelan klaster dan spasial.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
};
