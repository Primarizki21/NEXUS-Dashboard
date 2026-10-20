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
4. **Verification (Multi-Environment):** Eksekusi script secara langsung, cek konsistensi angka dan ketiadaan nilai hilang tak terduga. Untuk file notebook (.ipynb) atau modul interaktif, verifikasi wajib dijalankan sukses dari dua working directory: root repositori (`.`) dan folder `notebooks/`.
5. **Atomic Commit:** Lakukan commit git terpisah untuk setiap capaian logis yang telah diverifikasi.
6. **Feature Branch Only:** Dilarang commit atau push langsung ke `main`. Setiap perubahan wajib dibuat di branch terpisah (`feat/*`, `fix/*`) dan melalui Pull Request.
7. **Environment-Agnostic Execution:** Dilarang mengasumsikan satu *working directory* tunggal atau menggunakan *hardcoded relative path* yang rapuh terhadap konteks eksekusi (IDE vs terminal vs runner otomatis).
8. **Self-Verifying Outputs:** Setiap tahap persiapan atau pemuatan data wajib menghasilkan diagnostik atau validasi konkret (inspeksi dimensi, kelengkapan, atau uji asumsi awal), bukan hanya mencetak teks status tanpa bukti eksekusi.

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
  * **Validasi Skema Wajib:** Setiap regenerasi `.docx` wajib diverifikasi menggunakan validator skema OpenXML (`validate.py`) dengan hasil `All validations PASSED!`.
