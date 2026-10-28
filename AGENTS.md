# Multi-Agent Architecture & Workflow: Analisis Data Ketenagakerjaan ACTION 2026
*Subtema: “Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*
*Fokus & Batasan Proyek: **Analisis Data Komprehensif & Interactive Web Companion** (Data Harvester, Ekonometrika/Statistika, Sintesis Insight, Template Masalah Docx, & Web Dashboard)*

---

## 1. Batasan Ruang Lingkup (Scope Boundary)

Proyek ini difokuskan pada **analisis data ketenagakerjaan berbasis data resmi BPS** serta penyajian **Interactive Web Companion** (tidak mencakup pembuatan grafis infografis statis di Adobe Illustrator/Canva).
Tujuan akhir adalah menghasilkan:
1. Dataset terkurasi dan bersih dari sumber resmi (BPS & `data.go.id`).
2. Kode analisis statistik yang teruji, reproduktif, dan sederhana (*reproducible & simple*).
3. Ringkasan temuan siap pakai (*ready-to-use metrics & insights*) yang terdokumentasi dalam `RINGKASAN_TEMUAN.md`.
4. Kerangka narasi dan data terisi lengkap pada `template_masalah_terisi.docx` untuk tim desain infografis.
5. Draf metodologi dan pengolahan data untuk Laporan Resmi bab (c) & (d).
6. Aplikasi Web Pendamping Interaktif (`web/`) berbasis Vite + React + Tailwind + Shadcn UI yang memuat simulator kebijakan RPJMN 2029, peta klaster 38 provinsi, dekomposisi efek spasial, proyeksi TPT, serta 3 Fitur Kunci Inovasi Kebijakan (Early Warning IKKD, Dual-Vocation Credit System 50:50, dan Geo-Spatial Job Matching & KUR Klaster).
---

## 2. Prinsip Kerja & Filosofi Analisis Data

Menegakkan standar analisis data ketenagakerjaan yang kredibel, objektif, dan teruji:
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
4. **Verification (Multi-Environment & Browser-Driven Web Testing):**
   * **Analisis Data & Script:** Eksekusi script secara langsung, cek konsistensi angka dan ketiadaan nilai hilang tak terduga. Untuk file notebook (.ipynb) atau modul interaktif, verifikasi wajib dijalankan sukses dari dua working directory: root repositori (`.`) dan folder `notebooks/`.
   * **Pipeline Data Web:** Eksekusi `python scripts/export_web_data.py` wajib memastikan seluruh *self-verifying assertions* lolos (`PASSED`) tanpa nilai `NaN` atau data terpotong.
   * **Kompilasi & Tipe Data Web:** Jalankan `cd web && bun run build` (atau `npm run build`), memastikan 0 error TypeScript (`tsc`) dan 0 error bundling Vite.
   * **Pengujian Nyata dengan Browser Tools (Wajib Sebelum Commit):**
     - Jalankan preview/dev server web lokal.
     - Gunakan modul browser otomatis (`eval` dengan global `browser` object) untuk:
       1. Membuka tab peramban headless (`await browser.open({ url: ... })`).
       2. Menjalankan *smoke test* navigasi ke seluruh tab (Beranda, Kartografi, Ekonometrika, Simulator, Proyeksi, Metodologi, dan Inovasi Kebijakan).
       3. Menguji interaktivitas dinamis (slider kurikulum 50:50, filter radius Job Matching, kalkulator KUR Klaster, dan layer IKKD).
       4. Menginspeksi error console peramban (`tab.errors()`) dan memastikan tidak ada uncaught exception (`TypeError`, `undefined`, crash rendering React).
       5. Mengambil tangkapan layar observasi visual untuk memvalidasi tata letak responsif dan tema Dark/Light.
5. **Atomic Commit:** Lakukan commit git terpisah untuk setiap capaian logis yang telah diverifikasi.
6. **Feature Branch Only:** Dilarang commit atau push langsung ke `main`. Setiap perubahan wajib dibuat di branch terpisah (`feat/*`, `fix/*`) dan melalui Pull Request.
7. **Environment-Agnostic Execution:** Dilarang mengasumsikan satu *working directory* tunggal atau menggunakan *hardcoded relative path* yang rapuh terhadap konteks eksekusi (IDE vs terminal vs runner otomatis).
8. **Self-Verifying Outputs:** Setiap tahap persiapan atau pemuatan data wajib menghasilkan diagnostik atau validasi konkret (inspeksi dimensi, kelengkapan, atau uji asumsi awal), bukan hanya mencetak teks status tanpa bukti eksekusi.

---

## 4. Struktur Tim Agen (Analisis Data & Web Companion)

```
                          ┌─────────────────────────────┐
                          │   Orchestrator / Human PM   │
                          └──────────────┬──────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│       @data-scout         │  │       @data-analyst       │  │   @narrative-synthesizer  │
│  • Survei BPS & data.go.id│  │  • Model Spasial & Panel  │  │  • Template docx          │
│  • Harvesting Sakernas    │  │  • Klasterisasi & Forecast│  │  • Bab Metodologi         │
│  • data/clean/*.csv       │  │  • RINGKASAN_TEMUAN.md    │  │  • Matriks Kebijakan      │
└─────────────┬─────────────┘  └─────────────┬─────────────┘  └───────────────────────────┘
              │                              │
              └──────────────┬───────────────┘
                             ▼
              ┌─────────────────────────────┐
              │      @web-synthesizer       │
              │  • Pipeline export_web_data │
              │  • React + Shadcn UI        │
              │  • Simulator & Interaktivitas│
              └─────────────────────────────┘
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
  * Memilih dan mengeksekusi metode analisis yang didukung data (klasterisasi tipologi provinsi, autokorelasi spasial Moran/LISA, model Spatial Durbin Model panel, dan evaluasi multi-model forecasting).
  * Menghasilkan tabel metrik terverifikasi dan mengekspor ringkasan ke `data/RINGKASAN_TEMUAN.md`.
  * Merumuskan spesifikasi data visualisasi untuk tim infografis dan artefak charting resolusi tinggi di `assets/charts/`.

### Agen 3: Narrative & Template Synthesizer (`@narrative-synthesizer`)
* **Tanggung Jawab:**
  * Mengisi struktur dokumen `template_masalah.docx`:
    - Judul yang memikat (*data journalism angle*).
    - 4 *Research Questions* berbasis temuan data riil.
    - Rincian Babak I s.d. Babak V (Prelude, Data hasil kalkulasi, Tautan sumber data resmi, dan Rekomendasi visualisasi).
    - Matriks Solusi / Kebijakan (*Turning Insight into Opportunity*).
  * Menyusun draf teks Laporan Resmi bab Pengolahan Data dan Deskripsi Data.

### Agen 4: Web & Interactive Developer (`@web-synthesizer`)
* **Tanggung Jawab:**
  * Mengelola single pipeline sinkronisasi data analitik ke web melalui `scripts/export_web_data.py` menuju `web/src/data/labor_data.json` (bebas hardcoding angka di UI).
  * Mengembangkan dan memelihara dashboard web interaktif (`web/`) berbasis Vite, React, Tailwind CSS, dan Shadcn UI.
  * Mengimplementasikan modul interaktif: Simulator Kebijakan RPJMN 2029, Peta Kartografi 3 Klaster, visualisasi Ekonometrika Spasial LeSage-Pace, Proyeksi TPT 2025–2030, dan Modul Inovasi Kebijakan (Early Warning IKKD, Dual-Vocation 50:50, Geo-Spatial Matching & KUR Klaster).
  * Menegakkan standar visual antislop: layout lega, responsivitas multi-breakpoint via Radix Sheet, bebas warna gelap statis (dukungan penuh dark/light mode), dan komponen UI yang aksesibel.
  * Menjalankan protokol pengujian antarmuka otomatis berbasis Browser Tools sebelum setiap commit git.
---

## 5. Rekam Jejak Kesalahan & Invariant Teknis (Lessons Learned)

### Prinsip 1: Ketahanan Jalur dan Konteks Eksekusi (Context-Agnostic Paths)
* **Pola Kesalahan:**
  Mengasumsikan *working directory* selalu berada di lokasi tertentu (misal: subfolder tempat file berada), sehingga pemanggilan file data atau modul eksternal menggunakan jalur relatif statis. Ketika pengguna menjalankan kode melalui IDE (seperti VS Code atau JupyterLab) yang menetapkan *working directory* di root proyek, eksekusi gagal dengan `FileNotFoundError` dan alur analisis terputus.
* **Standar Pencegahan:**
  * Seluruh modul, skrip, dan notebook wajib menerapkan resolusi jalur adaptif:
    ```python
    from pathlib import Path

    DATA_DIR = Path("../data/clean") if (Path("../data/clean")).exists() else Path("data/clean")
    CHARTS_DIR = Path("../assets/charts") if (Path("../assets/charts")).exists() else Path("assets/charts")
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    ```
  * Generator otomatis yang memproduksi artefak kode wajib menyematkan logika resolusi adaptif ini secara konsisten.

### Prinsip 2: Keterlihatan dan Validasi Mandiri Eksekusi (Self-Verifying Execution)
* **Pola Kesalahan:**
  Cell awal hanya memuat *import* atau mencetak teks deklaratif (misal: "setup selesai") tanpa memvalidasi objek data atau asumsi dasar. Jika cell berikutnya gagal, pengguna kesulitan membedakan apakah lingkungan belum siap, data gagal dimuat, atau eksekusi tidak berjalan.
* **Standar Pencegahan:**
  * Setiap tahapan inisialisasi dan pemuatan data wajib bersifat *self-verifying*:
    1. Mengonfirmasi keberadaan dan dimensi data yang dimuat.
    2. Menjalankan pemeriksaan awal relevan (misal: uji stasioneritas/asumsi sebelum pemodelan, pengecekan nilai hilang).
    3. Menampilkan ringkasan ringkas yang membuktikan bahwa proses komputasi di cell tersebut benar-benar berhasil dijalankan.

### Prinsip 3: Integritas Dokumen OOXML & Skrip Pembangun Terpusat (Docx/OOXML Integrity)
* **Pola Kesalahan:**
  1. Melakukan manipulasi raw XML ad-hoc pada dokumen Word (.docx) menggunakan fungsi seperti `xml.etree.ElementTree.SubElement`. Pemanggilan ini menempelkan properti `<w:pPr>` dan `<w:rPr>` di akhir elemen anak (setelah teks atau run), yang melanggar urutan baku skema OOXML ECMA-376 dan merusak deklarasi namespace `mc:Ignorable`, sehingga Microsoft Word memunculkan pesan "unreadable contents".
  2. Melakukan patching langsung pada berkas biner `.docx` alih-alih memperbaiki skrip pembuat dokumen (`scripts/populate_template_masalah.py`), merusak prinsip *single source of truth*.
  3. Menyisipkan angka penomoran manual ("1. ", "2. ") pada paragraf yang sudah memiliki definisi penomoran Word (`w:numPr`), menyebabkan penomoran ganda ("1. 1. "), serta membiarkan placeholder kosong membentuk nomor hantu.
* **Standar Pencegahan:**
  * **Single Source of Truth:** Seluruh perubahan teks, struktur, font, dan tabel dokumen wajib dikelola melalui generator Python terpusat (`scripts/populate_template_masalah.py`). Dilarang memodifikasi ZIP/XML berkas `.docx` secara ad-hoc tanpa generator reproduktif.
  * **Patuhi Skema Elemen OOXML:** Gunakan API resmi `python-docx`. Jika memodifikasi oxml, pastikan urutan elemen skema dipatuhi (`<w:pPr>` selalu elemen pertama `<w:p>`, `<w:rPr>` selalu mendahului `<w:t>`, dan `<w:tblBorders>` diletakkan sebelum `<w:tblLook>`).
  * **Hormati Penomoran Otomatis:** Jangan menambahkan angka manual pada paragraf yang memiliki list styling. Hapus elemen placeholder berlebih langsung dari parent XML.
  * **Harmonisasi Font Penuh:** Setel font `Lexend 12pt` hitam pada style dokumen (`doc.styles['normal']`) serta atribut run (`w:ascii`, `w:hAnsi`, `w:eastAsia`, `w:cs`).
  * **Validasi Skema Wajib:** Setiap regenerasi `.docx` wajib diverifikasi menggunakan inspeksi XML internal atau script assertion Python (`python scripts/populate_template_masalah.py`), memastikan integritas elemen OOXML tanpa memunculkan peringatan unreadable content saat dibuka.

### Prinsip 4: Arsitektur Ekspor Data Terpusat Web (Single Data Pipeline for Web)
* **Pola Kesalahan:**
  Menuliskan angka statistik atau hasil pemodelan secara manual (*hardcoded*) di dalam komponen antarmuka React (`.tsx`). Ketika dataset Sakernas atau model diperbarui, angka di web menjadi usang (*stale*), inkonsisten dengan laporan resmi, dan melanggar prinsip *single source of truth*.
* **Standar Pencegahan:**
  * Seluruh data yang dikonsumsi oleh aplikasi web wajib bersumber dari berkas `data/clean/*.csv` dan dikompilasi secara otomatis oleh skrip terpusat `scripts/export_web_data.py` ke `web/src/data/labor_data.json`.
  * Skrip ekspor wajib menyematkan pengujian asersi (*self-verifying assertions*) untuk menjamin konsistensi dimensi data, kelengkapan 38 provinsi, dan ketiadaan nilai `NaN` sebelum berkas JSON ditulis.

### Prinsip 5: Desain UI Responsif, Komposisi Bebas Slop, & Tema Adaptif (Web & Shadcn Invariants)
* **Pola Kesalahan:**
  1. Menjejali bar navigasi utama dengan telemetri analitik (`SDM Panel | Moran: +0.246 | Pseudo-R²: 0.547`) sehingga header menjadi sempit dan bertabrakan pada resolusi tablet (768px–1024px) serta laptop kecil.
  2. Menggunakan warna statis gelap (*hardcoded* `bg-slate-950/80` atau `border-slate-800`) sehingga navbar tidak sinkron saat tema beralih ke mode terang.
  3. Menggunakan utilitas legasi Tailwind `space-x-*` (yang rapuh terhadap wrapping) dan menyisipkan animasi `animate-pulse` tak bermakna tanpa fungsi interaktif.
* **Standar Pencegahan:**
  * **Hierarki Layout Bersih:** Bar navigasi utama hanya memuat Brand, Navigasi Halaman, dan Kontrol Sistem. Indikator telemetri dialihkan ke *analytical context strip* (sub-bar) tersendiri agar navigasi tetap lega.
  * **Responsivitas Berjenjang:** Navigasi desktop penuh hanya aktif di layar lebar (`lg:`, 1024px+). Pada tablet dan mobile (< `lg:`), gunakan Radix `Sheet` drawer yang dilengkapi `SheetTitle` untuk aksesibilitas.
  * **Harmonisasi Tema Penuh:** Gunakan token semantik Shadcn/Tailwind (`bg-background`, `border-border`, `text-foreground`, `text-muted-foreground`) pada seluruh elemen antarmuka.
  * **Kepatuhan Antislop:** Dilarang keras menggunakan utilitas `space-x-*`/`space-y-*` (wajib gunakan `flex gap-*`), dilarang menggunakan gradien warna AI generik, dan dilarang animasi berulang tanpa aksi pengguna.

### Prinsip 6: Verifikasi Antarmuka Web Menggunakan Browser Tools Sebelum Commit (Web-App Browser QA)
* **Pola Kesalahan:**
  Menganggap penambahan fitur web selesai hanya karena file `.tsx` tersimpan dan build Vite berhasil, tanpa menguji rendering antarmuka di peramban nyata. Akibatnya, terjadi kegagalan runtime tersembunyi (misal: tombol tidak reaktif, nilai `undefined` saat interaksi slider, drawer mobile tidak terbuka, atau layout pecah di breakpoint tertentu).
* **Standar Pencegahan:**
  * **Zero Unchecked Commit:** Dilarang keras melakukan commit atau membuat PR untuk perubahan web sebelum dilakukan uji coba langsung menggunakan **Browser Tools**.
  * **Alur Pengujian Browser Wajib:**
    1. Luncurkan server lokal (`vite preview` atau `vite`).
    2. Buka tab via peramban otomatis: akses rute yang diubah.
    3. Eksekusi interaksi pengguna secara nyata (klik tombol, input range/slider, ubah dropdown).
    4. Periksa diagnostik browser: konsol peramban wajib bersih dari error fatal JavaScript (`tab.errors()`).
    5. Tutup sesi peramban (`await browser.close()`) dan laporkan bukti verifikasi sebelum melakukan commit git.
