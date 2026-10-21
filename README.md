# ACTION 2026: Analisis Pengangguran Terbuka Indonesia

Repositori ini memuat seluruh kode analisis data, dataset kurasi BPS, visualisasi statistik, dan draf narasi infografis untuk kompetisi **ACTION 2026 (Annual Competition of Data Science 2026)** yang diselenggarakan oleh HMP Sains Data Universitas Negeri Surabaya (UNESA).

**Subtema:** *Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja*  
**Judul Analisis:** *Paradoks Ijazah di Negeri Zamrud: Menyingkap Peta Retak Pengangguran Terbuka dan Merajut Peluang Kerja Inklusif Indonesia*

---

## 📁 Struktur Direktori

```text
action-infografis-2026/
├── data/
│   ├── clean/                # 28 CSV data resmi BPS (panel, klaster, gender, spasial, forecast)
│   ├── raw/                  # Berkas mentah BPS
│   └── RINGKASAN_TEMUAN.md   # Ringkasan metrik deskriptif & temuan statistik
├── web/                      # Interactive Web Companion (Vite + React + Tailwind + Shadcn UI)
│   ├── src/
│   │   ├── components/       # Navbar, Footer, MetricBadge, UI Primitives (Button, Badge, Sheet)
│   │   ├── pages/            # 6 Modul Analitik (Home, Cartography, Spatial, Simulator, Forecast, Method)
│   │   └── data/             # labor_data.json (Bundle data terkurasi hasil ekspor Python)
│   ├── components.json       # Konfigurasi Shadcn UI
│   └── package.json          # Konfigurasi dependensi web frontend
├── notebooks/
│   ├── analisis_ketenagakerjaan_action2026.ipynb   # Notebook visual storytelling (5 chart utama)
│   ├── Analisis_Klaster_Panel_Spasial_ACTION.ipynb # Notebook ekonometrika spasial (SDM, Moran, LISA)
│   └── Analisis_Forecasting_ACTION.ipynb           # Notebook proyeksi TPT 2025-2030
├── scripts/
│   ├── export_web_data.py             # Generator bundle data JSON terpusat untuk web app
│   ├── run_statistical_analysis.py    # Pipeline kalkulasi statistik & klasterisasi K-Means
│   ├── run_spatial_econometrics.py    # Estimasi model SDM Panel & autokorelasi spasial
│   ├── run_forecasting_analysis.py    # Pemodelan peramalan TPT multi-horizon
│   ├── generate_notebook.py           # Generator otomatis notebook analisis
│   └── populate_template_masalah.py   # Generator pengisian template docx untuk tim desain
├── assets/
│   └── charts/               # Ekspor grafik resolusi tinggi (PNG 300 DPI & SVG vektor)
├── docs/                     # Dokumen panduan & draf resmi kompetisi
│   ├── template_masalah_terisi.docx   # Dokumen kerja tim desain infografis
│   ├── DRAFT_TEMPLATE_MASALAH.md      # Versi markdown dokumen template
│   ├── DRAF_LAPORAN_ANALISIS_DATA.md  # Draf bab metodologi & analisis laporan lomba
│   └── guide-book-action-2026_*.pdf   # Panduan resmi kompetisi ACTION 2026
├── pyproject.toml            # Konfigurasi dependensi uv
├── requirements.txt          # Dependensi universal untuk pip
└── README.md
```

---

## 🚀 Panduan Memulai (Quickstart)

### Opsi 1: Menggunakan Standard `pip` (Python 3.10+)

```bash
# 1. Buat dan aktifkan virtual environment
python -m venv .venv
source .venv/bin/activate    # Di Linux/macOS
# .venv\Scripts\activate     # Di Windows

# 2. Pasang dependensi
pip install -r requirements.txt

# 3. Jalankan Jupyter Lab atau Notebook
jupyter lab
# Buka notebooks/analisis_ketenagakerjaan_action2026.ipynb
```

### Opsi 2: Menggunakan `uv` (Rekomendasi Cepat)

```bash
# Sinkronkan environment dan jalankan jupyter
uv sync
uv run jupyter lab
```

---

## 🌐 Menjalankan Web Dashboard Interaktif (Web Companion)

Web companion ini menyajikan visualisasi data interaktif, simulator kebijakan RPJMN 2029, peta klaster spasial, dan dekomposisi ekonometrika LeSage-Pace.

### Prasyarat
- **Node.js** v18+ atau **Bun** v1.0+ (disarankan Bun untuk instalasi dan build instan).
- Python 3.10+ (untuk ekspor dataset).

### Langkah Menjalankan:

1. **(Opsional) Sinkronisasi Data Analisis ke Web:**
   Jika Anda memperbarui dataset mentah atau menjalankan pemodelan statistik baru di `data/clean/`, jalankan script ekspor:
   ```bash
   python scripts/export_web_data.py
   ```
   *Skrip ini memvalidasi konsistensi data dan memperbarui `web/src/data/labor_data.json` secara otomatis.*

2. **Masuk ke Direktori Web & Pasang Dependensi:**
   ```bash
   cd web
   bun install   # atau: npm install
   ```

3. **Jalankan Development Server:**
   ```bash
   bun run dev   # atau: npm run dev
   ```
   Aplikasi akan aktif di **`http://localhost:3000`** dengan fitur Hot Module Replacement (HMR).

4. **Build & Preview Mode Production:**
   ```bash
   bun run build
   bun run preview   # aktif di http://localhost:4173
   ```

### 🧭 Fitur Utama Web Companion:
1. **Beranda (Paradoks Pasar Kerja):** KPI makro nasional, krisis pemuda, ilusi informalitas, dan status utilisasi tenaga kerja.
2. **Kartografi (Tipologi 3 Klaster):** Peta interaktif 38 provinsi hasil klasterisasi K-Means terstandarisasi.
3. **Ekonometrika Spasial:** Dekomposisi efek langsung & tumpahan (*spillover effect*) model SDM Panel ($k=4$).
4. **Simulator Kebijakan (RPJMN 2029):** Simulasi interaktif intervensi upah, investasi modal, dan pendidikan vokasi terhadap TPT.
5. **Proyeksi (Forecasting 2025–2030):** Trajektori TPT berbasis kombinasi model peramalan terbaik BPS.
6. **Metodologi & Audit Data:** Transparansi uji diagnostik, matriks bobot spasial, dan spesifikasi data resmi.

---

## 🤝 Alur Kolaborasi (Git Workflow)

Repositori ini menerapkan aturan kolaborasi ketat: **dilarang melakukan commit atau push langsung ke branch `main`**.

1. **Aktifkan Git Hook (Wajib Sekali di Awal):**
   ```bash
   git config core.hooksPath .githooks
   ```
2. **Kerjakan di Feature Branch:**
   ```bash
   git checkout -b feat/<nama-fitur>
   # Kerjakan analisis, lalu commit dan push:
   git push -u origin feat/<nama-fitur>
   ```
3. **Buat Pull Request (PR):** Buka PR di GitHub untuk digabungkan ke `main`.

Panduan lengkap tercantum di [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📊 Menjalankan Analisis & Regenerasi Output

1. **Jalankan Ulang Pipeline Statistik Lengkap:**
   ```bash
   python scripts/run_statistical_analysis.py
   ```
   *Output akan memperbarui `data/RINGKASAN_TEMUAN.md` dan tabel `hasil_klaster_provinsi.csv`.*

2. **Auto-Run Notebook (Tanpa Perlu Membuka Browser/GUI):**
   ```bash
   python scripts/run_notebook.py
   ```
   *Skrip ini mengeksekusi seluruh sel notebook end-to-end secara headless dan menyimpan hasilnya langsung ke dalam file `.ipynb`. Berkas notebook yang ada di repositori ini sudah dalam kondisi ter-run dengan seluruh grafik & metrik yang langsung tampil.*

   Jika ingin membukanya secara interaktif: Buka `notebooks/analisis_ketenagakerjaan_action2026.ipynb` melalui Jupyter Lab / VS Code.

3. **Perbarui Dokumen Desain (`template_masalah_terisi.docx`):**
   ```bash
   python scripts/populate_template_masalah.py
   ```

4. **Kompilasi & Sinkronisasi Dataset ke Web Companion (`labor_data.json`):**
   ```bash
   python scripts/export_web_data.py
   ```
   *Skrip ini menyatukan indikator panel, klaster, LISA, IKKD, dan proyeksi ke dalam `web/src/data/labor_data.json`.*
---

## 🎨 Ringkasan Visualisasi Utama (`assets/charts/`)
1. **Chart 01:** *The Youth Employment Crisis* : Perbandingan TPT Pemuda vs Dewasa (15-24 thn: **13,09%** vs Dewasa: **2,83%**; Rasio 4,6x).
2. **Chart 02:** *Educated Unemployment Paradox* : Anomali Pengangguran Terdidik (SMK Kejuruan: **6,81%** vs SD: **1,92%**).
3. **Chart 03:** *Spatial Labor Fracture & Informal Illusion* : Pencar TPT vs Sektor Informal per Provinsi ($r = -0,61$).
4. **Chart 04:** *Longitudinal Recovery Trajectory (2017-2024)* : Jejak Pemulihan Pascapandemi (Peak 2020: **7,07%** -> 2024: **4,91%**).
5. **Chart 05:** *Three Typologies of Provincial Labor Markets* : Pemetaan Klaster K-Means (Klaster 1: Aglomerasi Formal, Klaster 2: Vulnerable Agrarian, Klaster 3: Transisi/Jasa).
