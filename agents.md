# Multi-Agent Architecture & Workflow: ACTION 2026 Infografis
*Subtema: “Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*
*Penyelenggara: HMP Sains Data UNESA*

---

## 1. Filosofi Analisis: Mengambil Intisari Terbaik dari `@rasio/` (Tanpa Menjiplak Mentah-Mentah)

Studi kasus `@rasio/` menunjukkan standar juara nasional, namun **metode spesifiknya (panel 64 tahun, ekonometrika spasial pertanian) TIDAK BOLEH ditiru secara membabi buta**. Kita harus bersikap jujur secara ilmiah (*data-driven & data-first*):

### Yang DIADOPSI dari `@rasio/` (Prinsip Unggulan):
1. **Eksplorasi Data Berbasis Fakta (*Data-First Discovery*):**
   - Jangan berasumsi atau memaksakan model sebelum melihat dataset riil BPS dan `data.go.id`.
   - Biarkan ketersediaan dan granulasi data (apakah level Provinsi 34/38 atau Kabupaten/Kota 514, apakah deret waktu 5 atau 10 tahun) yang menentukan pertanyaan riset dan teknik pemodelan yang relevan.
2. **Ketelitian Metodologis (*Methodological Rigor*):**
   - Menghindari angka tanpa sumber atau klaim tanpa verifikasi.
   - Jika melakukan klasterisasi atau regresi, sertakan uji validitas/stabilitas yang masuk akal, bukan sekadar menampilkan grafik bawaan library.
3. **Struktur Jurnalisme Data (*Compelling Storytelling Arc*):**
   - **Hook Paradoks:** Menemukan satu anomali atau kontras tajam di awal (misal: paradoks pengangguran terdidik SMK/Sarjana vs SD, atau ketimpangan penyerapan kerja pemuda).
   - **Anatomi Masalah:** Menelusuri faktor struktural (*mismatch*, upah, investasi, sektor informal).
   - **Proyeksi & Dampak:** Apa yang terjadi jika pola ini berlanjut tanpa intervensi.
   - **Solusi Terarah (*Actionable Opportunities*):** Rekomendasi kebijakan yang realistis dan terukur.
4. **Alur Kerja Artefak Terisolasi:**
   - Pemisahan yang rapi: Data mentah $\rightarrow$ Script analisis $\rightarrow$ Ringkasan metrik terverifikasi (`RINGKASAN_*.md`) $\rightarrow$ Visualisasi SVG $\rightarrow$ Pengisian template dokumen.

### Yang DIHINDARI:
- **Jangan memaksakan model rumit yang tidak didukung data:** Jangan memaksakan analisis spasial global atau forecasting 30 tahun jika rentang data BPS tidak valid untuk itu.
- **Jangan mengorbankan keterbacaan publik:** Infografis ditujukan untuk masyarakat umum dan juri sains data. Visual harus tajam, elegan, dan langsung dipahami dalam 30 detik pertama.

---

## 2. Aturan Wajib Alur Kerja Agen (Mandatory Workflow Protocol)

Setiap agen atau kontributor yang mengeksekusi tugas dalam proyek ini **WAJIB** mengikuti siklus kerja berikut secara berurutan:

```
[1. Load Skills] ──> [2. To-Do List] ──> [3. Surgical Work] ──> [4. Verification] ──> [5. Atomic Commit]
  • antislop           • Breakdown        • Minimum code       • Smoke test        • 1 logical change
  • j-space              terukur          • Simplicity first   • Inspect output    • Descriptive msg
  • karpathy           • Success criteria • No speculative     • Zero hallucination
```

### Tahap 1: Pembacaan Skills & Prinsip Dasar
Sebelum mengetik kode atau menyusun teks:
* **Wajib baca `/skill:antislop`:** Pastikan tidak ada teks klise AI (*buzzwords*, em dash `—`, klaim palsu, data fiktif), penuhi rasio kontras WCAG, palet warna terkontrol (2–3 warna utama + 1 aksen), dan jangan gunakan template generik.
* **Wajib baca `/skill:j-space`:** Aktifkan ruang penalaran mendalam (*inner workspace*), evaluasi asumsi, dan pertahankan invariant proyek di setiap *seam*.
* **Wajib ikuti `karpathy-guidelines`:** Utamakan kesederhanaan (*Simplicity First*), jangan membuat abstraksi berlebihan untuk kode sekali pakai, dan lakukan perubahan secara bedah (*Surgical Changes*).

### Tahap 2: Penyusunan To-Do List
* Buat daftar tugas eksplisit dengan kriteria sukses (*success criteria*) yang terukur sebelum mengeksekusi pekerjaan.

### Tahap 3: Eksekusi Ramping & Nyata (Surgical Execution)
* Tulis kode seminimal mungkin yang menyelesaikan masalah (*Minimum Viable Code*).
* Gunakan data nyata dari BPS atau `data.go.id`. Dilarang keras mengarang angka dummy sebagai data final.

### Tahap 4: Verifikasi & Uji Hasil
* Jalankan script secara langsung. Periksa output tabel/grafik.
* Pastikan tidak ada nilai rumpang, kesalahan kalkulasi, atau distorsi visual.

### Tahap 5: Atomic Git Commit
* Lakukan *git commit* atomik untuk setiap unit kerja yang telah lolos verifikasi:
  - Satu commit untuk satu tujuan logis.
  - Pesan commit jelas, ringkas, dan merefleksikan perubahan nyata (contoh: `feat(data): harvest bps provincial unemployment 2015-2024`).

---

## 3. Pembagian Peran Agen

```
                          ┌─────────────────────────────┐
                          │   Orchestrator / Human PM   │
                          └──────────────┬──────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│  @data-scout     │           │  @narrative-     │           │  @qa-specialist  │
│  (Survey, Harvest│           │   strategist     │           │  (Compliance,    │
│   & Clean BPS)   │           │  (Template &     │           │   Report & PPT)  │
└────────┬─────────┘           │   Storyline)     │           └──────────────────┘
         │                     └────────▲─────────┘
         ▼                              │
┌──────────────────┐                    │ (Angka siap pakai & insight terverifikasi)
│ @data-analyst    ├────────────────────┤
│ (Explorasi,      │                    │
│  Model Sesuai    │                    │
│  Temuan Data)    │                    │
└────────┬─────────┘                    │
         │                              │
         ▼ (Spesifikasi visual & angka) │
┌──────────────────┐                    │
│ @visual-         ├────────────────────┘
│  architect       │
│ (A3 Layout,      │
│  SVG Charts)     │
└──────────────────┘
```

### Agen 1: Data Scout & Curator (`@data-scout`)
* **Misi:** Mensurvei portal BPS (`bps.go.id`, API Web BPS) dan Satu Data Indonesia (`data.go.id`) untuk subtema *Pengangguran Terbuka*.
* **Tugas:**
  1. Mengidentifikasi tabel data ketenagakerjaan yang tersedia secara lengkap dan mutakhir (misal: Sakernas Agustus/Februari 2015–2024).
  2. Mengumpulkan variabel: TPT provinsi/kabupaten, TPT menurut tingkat pendidikan (SD s.d. Perguruan Tinggi), kelompok umur (youth unemployment & NEET), serta indikator pasar kerja pelengkap (informalitas, setengah penganggur, upah, pertumbuhan ekonomi).
  3. Memvalidasi kelengkapan, mengatasi diskontinuitas kode provinsi/kabupaten, dan menyimpan data bersih ke folder `data/clean/`.

### Agen 2: Data & Statistical Analyst (`@data-analyst`)
* **Misi:** Melakukan analisis statistik yang jujur, tajam, dan proporsional sesuai karakteristik data yang ditemukan.
* **Tugas:**
  1. Eksplorasi Data Analitik (EDA): distribusi, disparitas wilayah, divergensi antar-tingkat pendidikan.
  2. Menerapkan pemodelan statistik yang *didukung oleh data*, seperti:
     - Tipologi/Klasterisasi wilayah yang stabil.
     - Analisis autokorelasi spasial (jika variasi geografis signifikan).
     - Analisis tren dan dekomposisi struktural (misal dampak post-COVID 2020 terhadap kesempatan kerja muda).
  3. Menyusun dokumen ringkasan metrik terverifikasi: `data/RINGKASAN_TEMUAN.md`.

### Agen 3: Storyline & Narrative Strategist (`@narrative-strategist`)
* **Misi:** Merangkai temuan data ke dalam alur jurnalisme data yang kuat sesuai template `template_masalah.docx`.
* **Tugas:**
  1. Merumuskan 4 *Research Questions* kritis.
  2. Mengisi kerangka babak (Prelude, Data, Link Sumber, Visualisasi).
  3. Menghubungkan *insight* analitis menjadi *opportunity* (rekomendasi kebijakan konkret yang berdaya guna).

### Agen 4: Visual Architect (`@visual-architect`)
* **Misi:** Mendesain infografis A3 Portrait yang estetis, informatif, dan memenuhi regulasi lomba.
* **Tugas:**
  1. Menerapkan aturan `antislop` untuk estetika visual (hierarki visual jelas, tipografi terbaca, warna harmonis).
  2. Menghasilkan grafik SVG vektor presisi tinggi dari data olahan (`assets/charts/*.svg`).
  3. Memastikan kepatuhan teknis A3 Portrait, 300 dpi, 3 logo wajib di atas, watermark nama tim di bawah.

### Agen 5: QA, Compliance & Final Documentation (`@qa-specialist`)
* **Misi:** Menjamin 100% kepatuhan terhadap Buku Panduan ACTION 2026.
* **Tugas:**
  1. Memverifikasi tidak adanya elemen AI generatif pada desain final.
  2. Menyusun draf Laporan Resmi 7 bab sesuai format panduan.
  3. Menyiapkan surat orisinalitas bermaterai dan persiapan materi final (10 slide PPT).

---

## 4. Format Laporan Git Commit Atomik
Setiap agen wajib melakukan commit menggunakan konvensi terstandarisasi:
* `docs(guide): ...` — pembaruan panduan atau dokumentasi.
* `data(harvest): ...` — penambahan atau kurasi dataset mentah.
* `feat(analysis): ...` — kode analisis statistik atau notebook.
* `viz(svg): ...` — penambahan aset visualisasi grafik.
* `chore(env): ...` — konfigurasi environment, uv, dan dependensi.
