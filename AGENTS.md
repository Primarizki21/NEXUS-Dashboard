# Multi-Agent Architecture & Workflow: Analisis Data Ketenagakerjaan ACTION 2026
*Subtema: “Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*
*Fokus & Batasan Proyek: **Hanya Analisis Data** (Data Harvester, Ekonometrika/Statistika, Sintesis Insight, & Pengisian Template Masalah untuk Tim Desain)*

---

## 1. Batasan Ruang Lingkup (Scope Boundary)

Proyek ini difokuskan **sepenuhnya pada analisis data** dan **tidak mencakup pembuatan grafis infografis**. 
Tujuan akhir adalah menghasilkan:
1. Dataset terkurasi dan bersih dari sumber resmi (BPS & `data.go.id`).
2. Kode analisis statistik yang teruji, reproduktif, dan sederhana (*reproducible & simple*).
3. Ringkasan temuan siap pakai (*ready-to-use metrics & insights*) yang terdokumentasi dalam `RINGKASAN_TEMUAN.md`.
4. Kerangka narasi dan data terisi lengkap pada `template_masalah.docx` (memuat *Research Questions*, *Prelude*, data kalkulasi, tautan sumber, dan spesifikasi visual untuk tim desain infografis).
5. Draf metodologi dan pengolahan data untuk Laporan Resmi bab (c) & (d).

---

## 2. Prinsip Kerja: Mengambil Aspek Terbaik `@rasio/` (Secara Proporsional)

Mengadopsi prinsip keunggulan `@rasio/` tanpa memaksakan metode yang tidak sesuai data:
* **Data-First Discovery:** Identifikasi ketersediaan dan granulasi data nyata di BPS/data.go.id terlebih dahulu sebelum menentukan model statistik.
* **Metodologi Jujur & Teruji:** Setiap metrik diverifikasi dari data mentah resmi (tidak ada angka fiktif/asumsi tak berdasar).
* **Storytelling Data:** Menyajikan data dengan struktur narasi tajam (*hook paradoks* $\rightarrow$ anatomi ketimpangan $\rightarrow$ faktor struktural $\rightarrow$ proyeksi $\rightarrow$ rekomendasi kebijakan).
* **Spesifikasi Visual Jelas:** Memberikan rekomendasi visualisasi konkret (tipe grafik, variabel sumbu X/Y, warna sorotan) yang mempermudah tim desain nantinya.

---

## 3. Aturan Wajib Alur Kerja Agen (Mandatory Workflow Protocol)

Setiap agen/kontributor wajib mengikuti protokol 5 langkah:

```
[1. Load Skills] ──> [2. To-Do List] ──> [3. Surgical Work] ──> [4. Verification] ──> [5. Atomic Commit]
  • antislop           • Breakdown        • Minimum code       • Run scripts       • 1 logical change
  • j-space              terukur          • Simplicity first   • Inspect data      • Descriptive msg
  • karpathy           • Success criteria • No speculative     • Zero hallucination
```

1. **Load Skills & Constraints:**
   * `/skill:antislop`: Teks bebas *buzzwords*, bebas klaim palsu, data 100% berbasis sumber resmi, tanpa em dash (`—`).
   * `/skill:j-space`: Jaga invariant logika, evaluasi asumsi data, dan fokus terarah.
   * `karpathy-guidelines`: *Simplicity first*, kode seringkas mungkin, tanpa abstraksi berlebihan.
2. **To-Do List:** Tetapkan daftar tugas dengan kriteria keberhasilan yang dapat diverifikasi.
3. **Surgical Execution:** Tulis script seminimal mungkin yang menyelesaikan tugas pengolahan/analisis data.
4. **Verification:** Eksekusi script secara langsung, cek konsistensi angka dan ketiadaan nilai hilang tak terduga.
5. **Atomic Commit:** Lakukan commit git terpisah untuk setiap capaian logis yang telah diverifikasi.
6. **Feature Branch Only:** Dilarang commit atau push langsung ke `main`. Setiap perubahan wajib dibuat di branch terpisah (`feat/*`, `fix/*`) dan melalui Pull Request.

---

## 4. Struktur Tim Agen (Khusus Analisis Data)

```
                          ┌─────────────────────────────┐
                          │   Orchestrator / Human PM   │
                          └──────────────┬──────────────┘
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
┌───────────────────────────┐                         ┌───────────────────────────┐
│       @data-scout         │                         │   @narrative-synthesizer  │
│  • Survei BPS & data.go.id│                         │  • Adapter template_      │
│  • Harvesting Sakernas    │                         │    masalah.docx           │
│  • Kurasi dataset bersih  │                         │  • Research questions     │
└─────────────┬─────────────┘                         │  • Policy recommendations │
              │                                       └─────────────▲─────────────┘
              ▼                                                     │
┌───────────────────────────┐                                       │
│       @data-analyst       │                                       │
│  • EDA & Variansi Data    ├───────────────────────────────────────┘
│  • Model Statistik Sesuai │ (Angka siap pakai, tabel ringkasan,
│    Karakteristik Data     │  rekomendasi tipe plot untuk desainer)
│  • RINGKASAN_TEMUAN.md    │
└───────────────────────────┘
```

### Agen 1: Data Scout & Curator (`@data-scout`)
* **Tanggung Jawab:**
  * Menelusuri portal resmi BPS (`bps.go.id`, API Web BPS, publikasi Sakernas) dan Satu Data Indonesia (`data.go.id`).
  * Mengunduh dan membersihkan tabel data ketenagakerjaan:
    1. TPT menurut provinsi / kabupaten-kota (deret waktu mutakhir).
    2. TPT menurut tingkat pendidikan tertinggi yang ditamatkan.
    3. TPT kelompok umur muda (15–24 tahun) & status NEET.
    4. Indikator pendukung pasar kerja: informalitas, setengah penganggur, upah minimum, PDRB per kapita, IPM.
  * Menghasilkan dataset bersih terstruktur di folder `data/clean/`.

### Agen 2: Data & Statistical Analyst (`@data-analyst`)
* **Tanggung Jawab:**
  * Menjalankan analisis eksploratif data (EDA) untuk menemukan pola dan disparitas utama.
  * Memilih dan mengeksekusi metode analisis yang benar-benar didukung data (misal: klasterisasi tipologi provinsi/daerah, evaluasi autokorelasi spasial jika ada dependensi geografis, atau dekomposisi tren/struktural).
  * Menghasilkan tabel metrik terverifikasi dan mengekspor ringkasan ke `data/RINGKASAN_TEMUAN.md`.
  * Merumuskan spesifikasi data visualisasi untuk tim infografis (tipe grafik yang disarankan, variabel yang diplot, data agregat yang siap dimasukkan ke software desain).

### Agen 3: Narrative & Template Synthesizer (`@narrative-synthesizer`)
* **Tanggung Jawab:**
  * Mengisi struktur dokumen `template_masalah.docx`:
    - Judul yang memikat (*data journalism angle*).
    - 4 *Research Questions* berbasis temuan data riil.
    - Rincian Babak I s.d. Babak V (Prelude, Data hasil kalkulasi, Tautan sumber data resmi, dan Rekomendasi visualisasi).
    - Matriks Solusi / Kebijakan (*Turning Insight into Opportunity*).
  * Menyusun draf teks Laporan Resmi bab Pengolahan Data dan Deskripsi Data.
