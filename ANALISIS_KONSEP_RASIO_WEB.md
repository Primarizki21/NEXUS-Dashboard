# Analisis Komprehensif Arsitektur Informasi dan Storytelling Data @rasio (GRAIN)
### Adaptasi Konseptual untuk Proyek ACTION 2026: Analisis Pengangguran Terbuka Indonesia
*Dokumentasi Studi Banding Platform: https://rasio-web.vercel.app/*

---

## 1. Eksekutif & Ringkasan Platform @rasio (GRAIN)

Platform **GRAIN** (*Spatial Panel Econometrics & Agrifood Systems Typology in Asia-Pacific*) dikembangkan oleh **TEAM IRIS** untuk ajang **RASIO 10.0 (Padjadjaran Statistics Olympiad / Statistics Day 2026)**. Platform ini bukan sekadar dashboard visualisasi statis, melainkan sebuah **kompanion digital interaktif ilmiah** (*interactive scientific companion*) yang mentransformasikan naskah riset ekonometrika menjadi instrumen eksplorasi data langsung (*live analytical instruments*).

### Filosofi Utama Desain Informasi
1. **"Every Screen Is a Scientific Instrument, Not Static Slides":** Setiap tampilan menyajikan data hidup dengan parameter estimasi, tombol filter, inspeksi selang kepercayaan, dan kemampuan simulasi kebijakan langsung.
2. **Paradoks Empiris Sebagai Pintu Masuk (*The Empirical Hook*):** Membuka narasi bukan dengan definisi umum, melainkan dengan fakta paradoksal yang meruntuhkan asumsi konvensional (mengapa model OLS standar gagal dan mengapa batas teritorial administratif menipu analisis).
3. **Penyematan Bukti Ilmiah Mikro (*Micro-Benchmarking Badges*):** Setiap modul dilengkapi lencana metrik konkret (nilai AIC, Silhouette Score, Moran's I, p-value, nilai MAPE, jumlah observasi) sehingga pembaca langsung mengetahui ketegasan metodologis di balik visual.
4. **Prinsip Parsimoni (*Parsimony Principle*):** Mengutamakan model statistik yang sederhana dan kokoh dibanding model kompleksitas tinggi yang rawan overfitting (*leak-free walk-forward validation*).
5. **Jembatan dari Ekonometrika ke Aksi Nyata (*Policy Translation*):** Koefisien regresi tidak dibiarkan sebagai angka abstrak, melainkan dihubungkan langsung ke simulator mitigasi berbasis tuas kebijakan riil.

---

## 2. Bedah Struktur dan Anatomi Informasi per Halaman / Modul

Website `@rasio` tersusun atas 5 modul analitis utama ditambah satu beranda naratif (*scrollytelling landing page*):

```
┌────────────────────────────────────────────────────────────────────────┐
│                        BERANDA / LANDING PAGE (/)                      │
│   • The Emission Paradox (Hook)   • 4-Phase Spatial Scrollytelling     │
│   • Empirical Evidence Cards      • Modular Architecture Navigation    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────┐
│  MODUL 1: KLUSTER     │ │  MODUL 2: EKONOMETRIKA│ │  MODUL 3: SIMULATOR   │
│     (/clustering)     │ │       (/spasial)      │ │      (/simulator)     │
│ • 44 Negara, 5 Klaster│ │ • Moran's I Trajektori│ │ • 3 Tuas Kebijakan    │
│ • Globe 3D & Peta 2D  │ │ • SDM vs OLS/SAR/SEM  │ │ • Dekomposisi Efek    │
│ • Matriks Emisi       │ │ • LeSage-Pace Multi-  │ │   LeSage-Pace Langsung│
│ • LISA Hotspot 2024   │ │   plier (2,20x N2O)   │ │ • Estimasi Mitigasi   │
└───────────────────────┘ └───────────────────────┘ └───────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│         MODUL 4: FORECASTING          │ │          MODUL 5: METODOLOGI          │
│            (/forecasting)             │ │             (/metodologi)             │
│ • Proyeksi 10 Tahun (2025-2035)       │ │ • Audit Panel Seimbang (2.816 Baris)  │
│ • 2.904 Fold Walk-Forward CV          │ │ • 4 Keputusan Metodologis Utama       │
│ • Fanchart Ketidakpastian 50/80/95%   │ │ • Matriks Bobot Spasial W (k-NN 4)    │
│ • Parsimoni: Drift & ARIMA Ensemble   │ │ • Transparansi Data & Open Science    │
└───────────────────────────────────────┘ └───────────────────────────────────────┘
```

---

### A. Beranda Naratif (`/`): *The Spatial Story & Scrollytelling*
* **Tujuan:** Membangun *cognitive hook*, meruntuhkan batas administratif, dan memandu alur berpikir audiens dari masalah ke solusi.
* **Elemen Informasi Kunci:**
  1. **Hook Paradoks:** Menyoroti angka asimetris: *"ASEAN menyumbang 22,78% emisi perubahan lahan global meski hanya menghasilkan 7,44% total GRK dunia."* Korelasi rank Spearman antara intensitas emisi per kapita dan pangsa emisi global mendekati nol (0,008).
  2. **4 Tahap Narasi Spasial (*Spatial Triage*):**
     - Tahap 1: 44 Negara dalam Isolasi (paradigma kebijakan unilateral yang gagal).
     - Tahap 2: 5 Tipologi Sistem Pangan (identifikasi kelompok struktural).
     - Tahap 3: Pendalaman Klaster Spasial (konsentrasi regional).
     - Tahap 4: Dekomposisi Limpahan Lintas Batas (efek tumpahan ke negara tetangga).
  3. **Pilar Empiris Ringkas (EMP-01 s.d. EMP-05):** Kartu ringkas berisi temuan korelasi, autokorelasi, ekonometrika spasial, klasterisasi, dan peramalan.
  4. **Uji Kelayakan Model Ekonometrika:** Kotak komparasi langsung antara OLS standar (AIC 5.012,3) vs Spatial Durbin Model (AIC 4.752,0) dengan penurunan $\Delta AIC = -260,3$ dan nilai $\rho = +0,516$ ($p < 0,001$).

---

### B. Modul 1: Tipologi Spasial & Kartografi (`/clustering`)
* **Tujuan:** Mengelompokkan wilayah berdasarkan profil multidimensi serta memetakan posisi geografisnya.
* **Elemen Informasi Kunci:**
  1. **Cakupan & Dimensi:** 44 negara Asia-Pasifik (1961–2024), diklasifikasikan berdasarkan 4 dimensi emisi (CO2 lahan, CH4 metana, N2O pupuk, CO2 energi) menggunakan K-Means ($k=5$) dan reduksi dimensi PCA (variansi kumulatif 84,9%).
  2. **Interaktivitas Peta:** Pilihan tampilan Globe 3D Orbital dan Peta Datar 2D dengan layer tematik (5 Klaster, LISA Hotspot 2024, CO2 Lahan, Metana). Garis lengkung (*arcs*) memperlihatkan jalur limpahan spasial antarnegara.
  3. **Temuan Kunci Klaster:** 7 dari 10 negara anggota ASEAN terkunci dalam satu klaster kritis yang sama: *Land Conversion Frontier* (Indonesia, Kamboja, Laos, Malaysia, Myanmar, Thailand, Vietnam).
  4. **Tabel Audit Komparatif:** Seluruh 44 negara dapat disortir dan difilter (khusus ASEAN-10), menampilkan status klaster, kuadran LISA, nilai per kapita per gas, dan populasi.
  5. **Galeri Vektor Metodologi Ilmiah:** Pilihan SVG ilmiah terintegrasi (Scatter PCA, Evaluasi Silhouette 0,534, Dendrogram Ward, Trajektori 64 Tahun) dengan mode Paper/Dark dan pembesaran penuh.

---

### C. Modul 2: Ekonometrika Spasial Lanjut (`/spasial`)
* **Tujuan:** Membuktikan secara statistik adanya ketergantungan geografis dan limpahan lintas batas (*spatial spillovers*).
* **Elemen Informasi Kunci:**
  1. **Trajektori Longitudinal Moran's I (1961–2024):** Menunjukkan autokorelasi spasial global yang menguat drastis dari $+0,255$ (1961) menjadi $+0,729$ (2024), membuktikan ketergantungan geografis meningkat +185%.
  2. **Dekomposisi Efek LeSage-Pace:** Memisahkan dampak langsung domestik (*direct effect*) dengan dampak limpahan ke negara tetangga (*indirect spillover effect*).
     - Temuan Kritis: Efek limpahan pupuk N2O ($+1,1046$) melampaui efek domestik ($+0,5011$) hingga **2,20 kali lipat**. Kebijakan input pertanian di satu negara memicu alih fungsi lahan di negara tetangga.
  3. **Tabel Uji Spesifikasi Model:** Membandingkan OLS, SLX, SAR, SEM, dan SDM. Model SDM dengan Time Fixed Effects terpilih karena meminimalkan AIC (4.752,0) dan menyerap seluruh autokorelasi spasial residual.
  4. **Tabel Estimasi Koefisien:** Menampilkan koefisien domestik ($X$) dan lag spasial ($WX$), nilai t-statistik, p-value, dan interpretasi substantif.

---

### D. Modul 3: Laboratorium Simulator Kebijakan (`/simulator`)
* **Tujuan:** Menyediakan sistem pendukung keputusan (*decision support system*) yang dapat dimanipulasi pengguna untuk melihat dampak kebijakan regional.
* **Elemen Informasi Kunci:**
  1. **Tiga Tuas Kebijakan Terintegrasi:**
     - Tuas 1: Efisiensi & Pengurangan Pupuk N2O Sintetis (0% s.d. 50%).
     - Tuas 2: Moratorium Konversi Hutan Primer & Lahan Gambut (0% s.d. 50%).
     - Tuas 3: Penerapan Pengairan Berselang Padi Sawah / AWD (0% s.d. 50%).
  2. **Kalkulasi Real-Time:** Menghitung estimasi mitigasi regional (dalam Mt CO2eq/tahun) menggunakan koefisien LeSage-Pace secara langsung.
  3. **Rekomendasi Kebijakan Berbasis Bukti:** Tiga poin kebijakan strategis konkret (Rasionalisasi Subsidi Pupuk Regional, Pakta Transboundary Hutan ASEAN, Fasilitas Transisi Hijau Bersama).

---

### E. Modul 4: Peramalan Waktu Runtun Bebas Kebocoran (`/forecasting`)
* **Tujuan:** Memberikan proyeksi 10 tahun ke depan (2025–2035) dengan metodologi validasi yang kokoh dan jujur.
* **Elemen Informasi Kunci:**
  1. **Validasi Silang Multi-Horizon Bebas Bocor:** Evaluasi 2.904 kombinasi model-fold (12 model kandidat x 4 horizon waktu x 2 skema jendela rolling/expanding).
  2. **Prinsip Parsimoni:** Uji Diebold-Mariano membuktikan model kompleks (GBDT, Ridge) tidak mengungguli model sederhana. Model Drift dan ARIMA Ensemble terpilih dengan MAPE 1,34% (h=1) hingga 3,10% (h=10).
  3. **Fanchart Ketidakpastian:** Menampilkan kurva proyeksi historis 1990–2024 dan pita selang kepercayaan 50%, 80%, dan 95% menuju 2035.

---

### F. Modul 5: Audit Metodologi & Transparansi Ilmiah (`/metodologi`)
* **Tujuan:** Menjamin integritas saintifik, mereproduksi hasil, dan menjawab pertanyaan metodologis kritis penguji.
* **Elemen Informasi Kunci:**
  1. **Struktur Panel Seimbang:** 44 negara x 64 tahun = 2.816 baris tanpa missing value dan tanpa imputasi artifisial.
  2. **Empat Keputusan Metodologis Utama:**
     - Mengapa Time-FE (bukan Two-Way FE): Karena dummy negara menyerap 76–93% variansi spasial cross-sectional.
     - Mengapa Sampel 44 Negara: Karena 10 negara ASEAN saja kekurangan kekuatan uji spasial (Moran's I tidak signifikan, p > 0,17).
     - Bukti Invariansi Tipologi ASEAN: Adjusted Rand Index (ARI) bernilai 1,000 antara sampel Asia-44 dan Monsoon Asia-19.
     - Penanganan Outlier: Mendokumentasikan status khusus Brunei sebagai eksportir hidrokarbon.
  3. **Spesifikasi Matriks Bobot W:** Pembobotan k-NN dengan k=4 terstandardisasi baris yang didukung uji rasio kemungkinan (*Likelihood Ratio Test*).

---

## 3. Matriks Komparasi dan Pemetaan Konsep ke Proyek ACTION 2026

Berikut adalah rancangan adaptasi menyeluruh dari konsep `@rasio` (GRAIN) ke dalam proyek analisis ketenagakerjaan kita (ACTION 2026):

| Dimensi Arsitektur | Konsep GRAIN (@rasio) | Penyelarasan untuk ACTION 2026 (Ketenagakerjaan) | Aset Data & Kode yang Tersedia di Proyek Kita |
|---|---|---|---|
| **Subtema & Fokus** | Emisi Agropangan & Perubahan Lahan Asia-Pasifik (RASIO 10.0) | Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja (ACTION 2026) | Dataset Sakernas BPS 2017–2024 terverifikasi 100% |
| **Paradoks / Cognitive Hook** | Emisi lahan tinggi tapi emisi GRK rendah; korelasi Spearman emisi vs per kapita = 0,008 | **Gunung Es Utilisasi Kerja & Paradoks Pengangguran Terdidik:** TPT turun ke 4,91%, tapi Setengah Penganggur naik +23,8% (11,56 juta); TPT SMK 3,5x SD; TPT Pemuda 6,95x Dewasa | `data/clean/indikator_utilisasi_tenaga_kerja_nasional.csv`, `tpt_nasional_pendidikan_detail_2022_2024.csv`, `assets/charts/01`, `02`, `14` |
| **Cakupan Wilayah & Panel** | 44 Negara Asia-Pasifik, 64 Tahun (1961–2024), 2.816 Observasi Seimbang | **34 Provinsi Panel Seimbang (2017–2024 = 272 Baris) + 38 Provinsi Potret Penuh 2024** | `data/clean/panel_tpt_provinsi_2017_2024.csv`, `master_panel_provinsi_2024.csv` |
| **Tipologi & Klasterisasi** | 5 Klaster Tipologi Emisi Agropangan (K-Means, PCA, Silhouette 0,534) | **3 Tipologi Klaster Ketenagakerjaan Provinsi:** Klaster 1: Urban-Industrial Trap (8 prov), Klaster 2: Agraris-Informal Shelter (18 prov), Klaster 3: Transisi Berimbang (12 prov) | `data/clean/hasil_klaster_provinsi.csv`, `grid_konfigurasi_klaster.csv`, `assets/charts/05_profil_tiga_klaster_ketenagakerjaan.svg` |
| **Autokorelasi Spasial** | Moran's I emisi naik dari +0,255 ke +0,729 (p < 0,001), k-NN k=4 | **Moran's I TPT konsisten signifikan (+0,176 s.d. +0,266, 2024: +0,246, p = 0,012), k-NN k=4 Haversine** | `data/clean/moran_lintasan_tahun_tpt.csv`, `lisa_provinsi_2024.csv`, `assets/charts/06`, `10` |
| **Model Ekonometrika Spasial** | Spatial Durbin Model (SDM) Time-FE, Min AIC 4.752,0 | **Spatial Durbin Model (SDM) 38 Provinsi, Min AIC 119,09, R² melonjak ke 0,547 (vs OLS 0,391)** | `data/clean/model_spasial_perbandingan.csv`, `assets/charts/07_model_spasial_dan_spillover_sdm.svg` |
| **Dekomposisi Limpahan (Spillover)** | Multiplier N2O 2,20x: limpahan tetangga (+1,105) melampaui efek domestik (+0,501) | **Limpahan Upah Spasial (+4,43) jauh melampaui efek domestik (+0,38): kenaikan upah memicu tarikan migrasi pencari kerja antarprovinsi** | `data/clean/dekomposisi_efek_sdm_tpt.csv`, `assets/charts/07` |
| **Simulator Keputusan / Kebijakan** | 3 Tuas Emisi (N2O, Moratorium Hutan, Pengairan Padi AWD) -> Kalkulasi Mitigasi Mt CO2eq | **3 Tuas Kebijakan Pasar Kerja:** (1) Link-and-match SMK Vokasi, (2) Formalisasi & Hilirisasi Desa, (3) Inkubasi Pemuda & UMKM -> Target 5,4 Juta Kerja RPJMN 2029 | Diformulasikan pada `data/RINGKASAN_TEMUAN.md` Bab 10, siap diwujudkan sebagai simulasi interaktif |
| **Peramalan Waktu Runtun** | Proyeksi Methane 2025–2035, 2.904 Fold CV, Drift & ARIMA Ensemble, Fanchart 50/80/95% | **Proyeksi TPT 2025–2030, Multi-Horizon CV, Holt Damped Trend (MASE 1,080, MAPE 11,2%), Fanchart 80/95% menuju 4,68%** | `data/clean/proyeksi_tpt_indonesia_2025_2030.csv`, `aturan_per_horizon_tpt.csv`, `assets/charts/08` |
| **Audit Metodologi & Transparansi** | Mengapa Time-FE, Mengapa 44 Negara, Bukti Invariansi ARI 1,000, Brunei Outlier | **Dekomposisi Ragam Panel (79,58% between-province), Uji Stabilitas Klaster (ARI 1,000), Uji Multikolinearitas (VIF < 2,5), k-NN k=4** | `data/clean/dekomposisi_ragam_dan_vif.csv`, `assets/charts/09`, `13` |

---

## 4. Rincian Narasi Data untuk Proyek ACTION 2026 (Meniru Alur Cerita @rasio)

Mengadopsi alur penceritaan data `@rasio`, analisis ketenagakerjaan kita dapat dibagi menjadi 6 babak berurutan yang saling mengunci:

### Babak I: Paradoks Awal & Gunung Es Ketenagakerjaan (The Hook)
* **Pesan Utama:** Angka TPT nasional yang turun ke 4,91% (terendah pasca-pandemi) adalah ilusi semu jika tidak melihat kualitas pekerjaan.
* **Data Pembuktian:**
  - Setengah penganggur melonjak +23,8% mencapai 11,56 juta orang (+2,22 juta orang dalam satu tahun).
  - *Labor Underutilization Rate (LU2)* standar ILO justru memburuk dari 11,64% menjadi 12,51% (19,03 juta orang mengalami defisit jam kerja dan pendapatan).
  - Paradoks Pendidikan: Lulusan SMK (6,81%) dan Universitas (5,33%) mencatat TPT jauh lebih tinggi dibanding lulusan SD ke bawah (1,92%).
  - Krisis Pemuda: TPT pemuda 15–24 tahun mencapai 17,02% (6,95 kali lipat usia dewasa 2,45%), menyumbang 56,70% dari total penganggur nasional.

### Babak II: Tipologi Kartografi 3 Klaster Provinsi (The Regional Landscape)
* **Pesan Utama:** Pasar kerja Indonesia tidak homogen. Kebijakan satu ukuran untuk semua (*one-size-fits-all*) dipastikan gagal.
* **Data Pembuktian:**
  - Evaluasi 216 kombinasi grid search K-Means mengonfirmasi konfigurasi optimal pada $k=3$ (Silhouette 0,441; kestabilan subsampling ARI = 1,000).
  - Tiga klaster struktural:
    1. **Klaster 1 (Urban-Industrial Trap, 8 Provinsi):** TPT tertinggi (6,58%), formalitas tinggi (56,8%), upah tinggi (Rp3,85 juta), namun pengangguran SMK dan sarjana menumpuk akibat mismatch keterampilan dan migrasi masuk.
    2. **Klaster 2 (Agraris-Informal Shelter, 18 Provinsi):** TPT semu sangat rendah (2,82%), namun informalitas ekstrem (75,4%), upah rendah (Rp2,62 juta), didominasi pekerja paruh waktu pertanian subsisten yang tidak mampu menganggur (*too poor to be unemployed*).
    3. **Klaster 3 (Transisi Berimbang, 12 Provinsi):** TPT moderat (4,52%), informalitas seimbang (52,6%), upah moderat (Rp2,88 juta), sektor perdagangan dan jasa mandiri relatif stabil.

### Babak III: Autokorelasi & Limpahan Ekonometrika Spasial (The Spatial Connection)
* **Pesan Utama:** Pengangguran di suatu provinsi tidak berdiri sendiri, melainkan dipengaruhi kuat oleh tarikan spasial wilayah tetangga.
* **Data Pembuktian:**
  - Moran's I global bernilai $+0,246$ ($p = 0,012$), membuktikan pola aglomerasi spasial yang konsisten sepanjang 2017–2024.
  - Model SDM membuktikan keunggulan mutlak atas OLS non-spasial ($R^2$ naik dari 0,391 ke 0,547).
  - Dekomposisi Efek LeSage-Pace membongkar fakta krusial:
    - Koefisien efek limpahan spasial upah buruh ($+4,43$) jauh melampaui efek langsung domestik ($+0,38$). Kenaikan upah di pusat industri perkotaan (seperti DKI Jakarta dan Jawa Barat) menyedot angkatan kerja dari provinsi sekitar, menciptakan antrean pengangguran terbuka yang melimpah antarwilayah.
    - Limpahan rasio mismatch kejuruan antardaerah tercatat $+0,90$.

### Babak IV: Laboratorium Simulasi Kebijakan (The Decision Support Lab)
* **Pesan Utama:** Mengubah wawasan data menjadi peluang intervensi terukur (*Turning Insight into Opportunity*) untuk menutup defisit target RPJMN 2025–2029.
* **Mekanisme Simulasi:**
  - Target RPJMN mematok TPT nasional turun ke kisaran 4,00% – 4,50% pada 2029 (baseline proyeksi 4,74%).
  - Simulasi penciptaan 5,40 juta kesempatan kerja berkualitas melalui 3 tuas:
    1. *Tuas 1: Link-and-Match Vokasi & Magang Bersertifikasi Industri:* Mengurangi mismatch SMK di Klaster 1, menyerap 1,85 juta tenaga kerja muda.
    2. *Tuas 2: Hilirisasi Komoditas Pertanian & Formalisasi UMKM Desa:* Mengentaskan setengah penganggur di Klaster 2, mengonversi 2,10 juta pekerja subsisten menjadi pekerja penuh waktu.
    3. *Tuas 3: Akselerasi Inkubasi Usaha Digital & Pembiayaan Wirausaha:* Mendorong diversifikasi di Klaster 3, menciptakan 1,45 juta lapangan kerja baru.

### Babak V: Proyeksi Jangka Menengah Bebas Kebocoran Menuju 2030 (The Forecast)
* **Pesan Utama:** Lintasan pemulihan pasar kerja menuju 2030 memerlukan penahan tren (*damping*) agar tidak terdistorsi guncangan anomali pandemi.
* **Data Pembuktian:**
  - Pengujian stasioneritas: Deret TPT terintegrasi pada derajat satu ($d=1$) berdasarkan uji ADF ($t = -2,098$) dan KPSS ($0,182$).
  - Validasi silang walk-forward membuktikan keunggulan *Holt Damped Trend* (MASE $h=3$ sebesar 1,080 dan MAPE 11,2%), mengalahkan ARIMA (1,1,0) dan Ridge Regression yang mengalami overfitting.
  - Proyeksi titik melandai secara realistis: 5,05% (2025) $\rightarrow$ 4,96% (2026) $\rightarrow$ 4,88% (2027) $\rightarrow$ 4,80% (2028) $\rightarrow$ 4,74% (2029) $\rightarrow$ **4,68% pada 2030**.
  - Selang prediksi 95% menunjukkan batas volatilitas [1,50% – 8,87%] yang menegaskan perlunya jaring pengaman kerja aktif jika terjadi gejolak makroekonomi global.

### Babak VI: Integritas Metodologis & Open Science (The Scientific Audit)
* **Pesan Utama:** Menjamin bahwa seluruh inferensi dibangun di atas data mentah resmi BPS tanpa fabrikasi atau asumsi rapuh.
* **Data Pembuktian:**
  - Dekomposisi variansi panel membuktikan 79,58% variasi data berada pada tingkat antar-provinsi (*between-province*), memvalidasi secara ilmiah penggunaan model spasial dan klaster wilayah.
  - Uji multikolinearitas memastikan seluruh prediktor bebas redundancy (seluruh nilai VIF < 2,5).
  - Spesifikasi matriks spasial k-NN ($k=4$) berbasis koordinat Haversine terbukti paling efektif menangkap interaksi ketenagakerjaan antarpulau di Indonesia.

---

## 5. Rekomendasi Format Penyajian untuk Tim Desain & Dokumen Laporan

Untuk mengimplementasikan gaya penyampaian `@rasio` ke dalam format poster infografis dan laporan pendukung:

1. **Gunakan Header & Lencana Metrik Bergaya Laboratorium Sains:**
   - Sertakan metadata ringkas pada setiap visual (contoh: `K-Means k=3 · Silhouette 0,441`, `Moran's I +0,246 · p=0,012`, `Holt Damped · MASE 1,080`).
2. **Pisahkan Efek Langsung vs Limpahan Spasial:**
   - Saat menyajikan pengaruh upah dan mismatch, jangan hanya tampilkan koefisien regresi biasa, tapi tampilkan grafik perbandingan *Direct vs Spillover* (Dekomposisi LeSage-Pace).
3. **Sajikan Visual 'Gunung Es' dan 'Tangga Paradoks':**
   - Infografis harus menonjolkan grafik batang bertingkat (*Ladder Chart*) untuk TPT berdasarkan pendidikan (SD 1,92% s.d. SMK 6,81%) dan grafik *Waterfall* untuk utilisasi tenaga kerja (TPT 4,91% $\rightarrow$ Setengah Penganggur 7,99% $\rightarrow$ LU2 12,51%).
4. **Sediakan Kotak 'Temuan Empiris & Interpretasi':**
   - Di bawah setiap grafik utama, sertakan 2–3 kalimat penjelas yang tajam, lugas, dan bebas jargon kosong, langsung menghubungkan temuan statistik dengan implikasi kebijakan.
5. **Jika Dikembangkan Menjadi Web App Interaktif di Masa Depan:**
   - Dapat mengadopsi arsitektur React/Next.js serupa dengan 5 rute: `/` (Overview & Hook), `/klaster` (Peta Spasial Indonesia & 3 Klaster), `/ekonometrika` (SDM & LeSage-Pace Spillovers), `/simulator` (Simulator Kebijakan Penyerapan 5,4 Juta Kerja), dan `/proyeksi` (Fanchart Proyeksi TPT 2025–2030).
