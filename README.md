# ACTION 2026: Analisis Pengangguran Terbuka Indonesia

Repositori ini memuat seluruh kode analisis data, dataset kurasi BPS, visualisasi statistik, dan draf narasi infografis untuk kompetisi **ACTION 2026 (Annual Competition of Data Science 2026)** yang diselenggarakan oleh HMP Sains Data Universitas Negeri Surabaya (UNESA).

**Subtema:** *Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja*  
**Judul Analisis:** *Paradoks Ijazah di Negeri Zamrud: Menyingkap Peta Retak Pengangguran Terbuka dan Merajut Peluang Kerja Inklusif Indonesia*

---

## 📁 Struktur Direktori

```text
action-infografis-2026/
├── data/
│   ├── clean/                # 10 CSV data resmi BPS (panel, klaster, gender, pendidikan)
│   ├── raw/                  # Berkas mentah BPS
│   └── RINGKASAN_TEMUAN.md   # Ringkasan metrik deskriptif & temuan statistik
├── notebooks/
│   └── analisis_ketenagakerjaan_action2026.ipynb   # Notebook visual storytelling (5 chart utama)
├── scripts/
│   ├── run_statistical_analysis.py    # Pipeline kalkulasi statistik & klasterisasi K-Means
│   ├── generate_notebook.py           # Generator otomatis notebook analisis
│   ├── populate_template_masalah.py   # Generator pengisian template docx untuk tim desain
│   ├── build_panel_tpt_2017_2024.py   # Pipeline ekstraksi panel longitudinal
│   └── extract_bps_tables.py          # Ekstraktor tabel laporan resmi BPS
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

---

## 🎨 Ringkasan Visualisasi Utama (`assets/charts/`)

1. **Chart 01:** *The Youth Employment Crisis* — Perbandingan TPT Pemuda vs Dewasa (15–24 thn: **13,09%** vs Dewasa: **2,83%**; Rasio 4,6x).
2. **Chart 02:** *Educated Unemployment Paradox* — Anomali Pengangguran Terdidik (SMK Kejuruan: **6,81%** vs SD: **1,92%**).
3. **Chart 03:** *Spatial Labor Fracture & Informal Illusion* — Pencar TPT vs Sektor Informal per Provinsi ($r = -0,61$).
4. **Chart 04:** *Longitudinal Recovery Trajectory (2017–2024)* — Jejak Pemulihan Pascapandemi (Peak 2020: **7,07%** $\to$ 2024: **4,91%**).
5. **Chart 05:** *Three Typologies of Provincial Labor Markets* — Pemetaan Klaster K-Means (Klaster 1: Aglomerasi Formal, Klaster 2: Vulnerable Agrarian, Klaster 3: Transisi/Jasa).
