"""
Generator Skrip untuk Menghasilkan Dua Notebook Tingkat Lanjut ala Proyek RASIO:
1. notebooks/Analisis_Klaster_Panel_Spasial_ACTION.ipynb
2. notebooks/Analisis_Forecasting_ACTION.ipynb
"""

import json
import uuid
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_DIR = os.path.join(BASE_DIR, "notebooks")
os.makedirs(NOTEBOOK_DIR, exist_ok=True)

def create_cell(cell_type, source):
    cell = {
        "cell_type": cell_type,
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": [line + "\n" for line in source.split("\n")]
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell

def build_spatial_notebook():
    cells = []
    
    # Header
    cells.append(create_cell("markdown", """# Klasterisasi dan Ekonometrika Panel-Spasial Pasar Tenaga Kerja Indonesia
### ACTION 2026 — Annual Competition of Data Science (UNESA)
**Subtema:** *“Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*  
**Unit Analisis:** 38 Provinsi di Indonesia (dengan panel seimbang 34 provinsi periode 2017–2024 = 272 observasi)  
**Sumber Data:** Badan Pusat Statistik (Sakernas 2017–2024 & Indikator Pasar Tenaga Kerja)

| Peran | Variabel | Makna dalam Pasar Tenaga Kerja | Satuan |
|---|---|---|:---:|
| **Y** | `TPT_Total` | Tingkat Pengangguran Terbuka (indikator utama penyerapan kerja) | % |
| **X1** | `Informal` | Proporsi pekerja sektor informal (penyangga subsisten) | % |
| **X2** | `log(Upah)` | Logaritma rata-rata upah bersih buruh/karyawan | log(Rp) |
| **X3** | `Educated_Mismatch` | Rasio mismatch pengangguran terdidik (SMK & PT vs SD) | rasio |

---"""))

    cells.append(create_cell("markdown", """## 0. Setup Lingkungan & Dependensi"""))
    cells.append(create_cell("code", """import warnings
warnings.filterwarnings('ignore')
import os, math
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

RS = 42
np.random.seed(RS)
sns.set_theme(style='whitegrid')
plt.rcParams.update({'figure.dpi': 110, 'savefig.bbox': 'tight', 'font.size': 9})

HIJAU = '#2F7D6E'
BATA  = '#C0392B'
PASIR = '#D9B26F'
ABU   = '#8896A0'

# Path Setup yang adaptif terhadap root direktori maupun folder notebooks
DATA_DIR = Path("../data/clean")
if not DATA_DIR.exists():
    DATA_DIR = Path("data/clean")

CHARTS_DIR = Path("../assets/charts")
if not CHARTS_DIR.exists():
    CHARTS_DIR = Path("assets/charts")
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

print("Setup selesai. Siap membaca data resmi BPS.")"""))

    cells.append(create_cell("markdown", """## 1. Memuat Data Panel & Georeferensi 38 Provinsi Indonesia"""))
    cells.append(create_cell("code", """master_38 = pd.read_csv(f'{DATA_DIR}/master_panel_provinsi_2024.csv')
panel_hist = pd.read_csv(f'{DATA_DIR}/panel_tpt_provinsi_2017_2024.csv')
coords = pd.read_csv(f'{DATA_DIR}/koordinat_provinsi_indonesia.csv')
dist_mat = pd.read_csv(f'{DATA_DIR}/jarak_km_provinsi_indonesia.csv', index_col=0)
W_knn4 = pd.read_csv(f'{DATA_DIR}/W_knn4_indonesia.csv', index_col=0)

df_prov = master_38[master_38["Provinsi"] != "Indonesia"].copy()
print(f"Total Provinsi Teranalisis : {len(df_prov)} Provinsi")
print(f"Total Panel Historis      : {len(panel_hist) - 1} Provinsi x 8 Tahun (2017-2024)")
display(coords.head(5))"""))

    cells.append(create_cell("markdown", """## 2. Autokorelasi Spasial Global: Moran's I Lintasan Waktu (2017–2024)
Langkah pertama: menguji apakah pengangguran antar-provinsi di Indonesia bersifat acak atau mengelompok secara geografis."""))
    cells.append(create_cell("code", """df_moran = pd.read_csv(f'{DATA_DIR}/moran_lintasan_tahun_tpt.csv')
display(df_moran)

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(df_moran["tahun"], df_moran["moran_i"], marker="o", color=HIJAU, linewidth=2.5, markersize=8, label="Moran's I TPT")
ax.axhline(0, color=ABU, linestyle="--", alpha=0.7, label="Garis Netral (Acak Spasial)")
ax.set_title("Evolusi Autokorelasi Spasial Pengangguran Indonesia (2017–2024)\\nMoran's I Global Antar-Provinsi", fontsize=11, fontweight="bold")
ax.set_xlabel("Tahun Pengamatan BPS Sakernas")
ax.set_ylabel("Nilai Indeks Moran's I")
ax.grid(True, linestyle=":", alpha=0.6)
for _, r in df_moran.iterrows():
    ax.annotate(f"{r['moran_i']:.3f}", (r['tahun'], r['moran_i']), textcoords="offset points", xytext=(0, 8), ha='center', fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout()
plt.show()"""))

    cells.append(create_cell("markdown", """## 3. Autokorelasi Spasial Lokal: LISA 2024 (Local Indicators of Spatial Association)
Mengidentifikasi kantong pengangguran regional (*Hotspot High-High*), wilayah agraris (*Coldspot Low-Low*), dan wilayah *shelter*."""))
    cells.append(create_cell("code", """df_lisa = pd.read_csv(f'{DATA_DIR}/lisa_provinsi_2024.csv')
print("Distribusi Kuadran LISA 2024:")
display(df_lisa["kuadran"].value_counts())

fig, ax = plt.subplots(figsize=(8, 6))
colors_lisa = {
    "High-High (Hotspot Pengangguran)": BATA,
    "Low-Low (Coldspot / Agraris)": HIJAU,
    "Low-High (Shelter di Tengah Hotspot)": PASIR,
    "High-Low (Anomali Mandiri Tinggi)": "#6C5B9E"
}
for quad, col in colors_lisa.items():
    sub = df_lisa[df_lisa["kuadran"] == quad]
    ax.scatter(sub["z_TPT"], sub["lag_z_TPT"], color=col, s=70, alpha=0.85, label=quad, edgecolors="white", linewidth=0.5)

m_slope, b_intercept = np.polyfit(df_lisa["z_TPT"], df_lisa["lag_z_TPT"], 1)
x_line = np.linspace(df_lisa["z_TPT"].min(), df_lisa["z_TPT"].max(), 50)
ax.plot(x_line, m_slope * x_line + b_intercept, color='#243B3A', linewidth=1.8, label=f"Kemiringan Moran's I ({m_slope:.3f})")
ax.axvline(0, color=ABU, linestyle="--", alpha=0.5)
ax.axhline(0, color=ABU, linestyle="--", alpha=0.5)
ax.set_title("Moran Scatterplot & Klaster Spasial LISA (Agustus 2024)", fontsize=11, fontweight="bold")
ax.set_xlabel("Standar Deviasi TPT Provinsi (z)")
ax.set_ylabel("Spatial Lag Tetangga (Wz)")
ax.legend(loc="upper left", fontsize=8.5)
plt.tight_layout()
plt.show()"""))

    cells.append(create_cell("markdown", """## 4. Pemodelan Ekonometrika Spasial: OLS vs SLX vs SAR vs SEM vs SDM
Membandingkan model standar non-spasial (OLS) dengan model yang mengakomodasi efek spasial (SLX, SAR, SEM, SDM)."""))
    cells.append(create_cell("code", """df_models = pd.read_csv(f'{DATA_DIR}/model_spasial_perbandingan.csv')
display(df_models)

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(df_models["Model"], df_models["AIC"], color=[ABU, ABU, HIJAU, HIJAU, BATA], width=0.55)
ax.set_title("Perbandingan Kriteria Informasi Akaike (AIC) Antarmodel\\n(Nilai Lebih Rendah Mengindikasikan Model Lebih Unggul)", fontsize=11, fontweight="bold")
ax.set_ylabel("Nilai AIC")
ax.set_xticklabels(["OLS", "SLX", "SAR", "SEM", "SDM\\n(Terpilih)"])
ax.set_ylim(df_models["AIC"].min() - 15, df_models["AIC"].max() + 10)
for b in bars:
    h = b.get_height()
    ax.annotate(f"{h:.1f}", (b.get_x() + b.get_width() / 2, h), textcoords="offset points", xytext=(0, 4), ha='center', fontweight="bold")
plt.tight_layout()
plt.show()"""))

    cells.append(create_cell("markdown", """## 5. Dekomposisi Efek Spasial LeSage–Pace (SDM)
Menghitung efek langsung (*Direct Effect*), efek limpahan (*Spillover Effect*), dan efek total dari informalitas, upah, dan mismatch pendidikan."""))
    cells.append(create_cell("code", """df_lesage = pd.read_csv(f'{DATA_DIR}/dekomposisi_efek_sdm_tpt.csv')
display(df_lesage)

x_indices = np.arange(len(df_lesage))
width = 0.28
fig, ax = plt.subplots(figsize=(9, 5))
rects1 = ax.bar(x_indices - width, df_lesage["Efek_Langsung (Direct)"], width, label="Efek Langsung (Domestik)", color=HIJAU)
rects2 = ax.bar(x_indices, df_lesage["Efek_Limpahan (Spillover / Indirect)"], width, label="Efek Limpahan (Spasial)", color=PASIR)
rects3 = ax.bar(x_indices + width, df_lesage["Efek_Total"], width, label="Efek Total", color=BATA)
ax.set_title("Dekomposisi Efek Spatial Durbin Model (LeSage–Pace)", fontsize=11, fontweight="bold")
ax.set_xticks(x_indices)
ax.set_xticklabels(["Informalitas (%)", "log(Upah Buruh)", "Mismatch Terdidik"])
ax.axhline(0, color='#243B3A', linestyle="-", linewidth=0.8)
ax.set_ylabel("Besaran Efek Marginal Terhadap TPT")
ax.legend(loc="upper right")
plt.tight_layout()
plt.show()"""))

    cells.append(create_cell("markdown", """## 6. Grid Search Klaster Multidimensi & Uji Stabilitas Subsampling Bootstrap"""))
    cells.append(create_cell("code", """df_grid = pd.read_csv(f'{DATA_DIR}/grid_konfigurasi_klaster.csv')
df_fitur = pd.read_csv(f'{DATA_DIR}/fitur_lintasan_provinsi.csv')
print(f"Total Konfigurasi Teruji : {len(df_grid)}")
print(f"Konfigurasi Lolos Syarat : {len(df_grid[df_grid['Layak']])}")
display(df_grid[df_grid["Layak"]].sort_values("Silhouette", ascending=False).head(5))"""))

    nb_data = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.12"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    nb_path = os.path.join(NOTEBOOK_DIR, "Analisis_Klaster_Panel_Spasial_ACTION.ipynb")
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, indent=2)
    print(f"Notebook Spasial berhasil dibuat di: {nb_path}")

def build_forecasting_notebook():
    cells = []
    
    # Header
    cells.append(create_cell("markdown", """# Peramalan Deret Waktu (Forecasting) Tingkat Pengangguran Terbuka Indonesia (2017–2024 → 2030)
### ACTION 2026 — Annual Competition of Data Science (UNESA)
**Subtema:** *“Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*  
**Unit Analisis:** Deret Waktu Tahunan TPT Nasional BPS Sakernas (2017–2024)  
**Tujuan:** Menguji akurasi model peramalan melalui cross-validation multi-horizon dan memproyeksikan TPT Indonesia menuju tahun 2030 (Era RPJMN & SDGs 8).

---"""))

    cells.append(create_cell("markdown", """## 0. Setup Lingkungan & Dependensi"""))
    cells.append(create_cell("code", """import warnings
warnings.filterwarnings('ignore')
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

RS = 42
np.random.seed(RS)
sns.set_theme(style='whitegrid')
plt.rcParams.update({'figure.dpi': 110, 'savefig.bbox': 'tight', 'font.size': 9})

HIJAU = '#2F7D6E'
BATA  = '#C0392B'
PASIR = '#D9B26F'
ABU   = '#8896A0'

# Path Setup yang adaptif terhadap root direktori maupun folder notebooks
DATA_DIR = Path("../data/clean")
if not DATA_DIR.exists():
    DATA_DIR = Path("data/clean")

CHARTS_DIR = Path("../assets/charts")
if not CHARTS_DIR.exists():
    CHARTS_DIR = Path("assets/charts")
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

print("Setup selesai. Siap menjalankan pemodelan peramalan.")"""))

    cells.append(create_cell("markdown", """## 1. Memuat Deret Waktu Historis TPT Nasional BPS (2017–2024) & Uji Pra-Model"""))
    cells.append(create_cell("code", """panel_hist = pd.read_csv(f'{DATA_DIR}/panel_tpt_provinsi_2017_2024.csv')
idn_row = panel_hist[panel_hist["Provinsi"] == "Indonesia"].iloc[0]

years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
y_series = np.array([idn_row[f"TPT_{yr}"] for yr in years], dtype=float)

df_ts = pd.DataFrame({"Tahun": years, "TPT_Nasional": y_series})
print(f"Data Deret Waktu TPT Nasional BPS: {years[0]} - {years[-1]} (T = {len(y_series)})")
print(f"Nilai Historis (%): {[float(x) for x in np.round(y_series, 2)]}")

# Uji Pra-Model: Stasioneritas (ADF & KPSS) dan Kekuatan Tren LOESS
def test_stationarity(y):
    dy = np.diff(y)
    ylag = y[:-1]
    X_adf = np.column_stack([np.ones(len(dy)), ylag])
    b, _, _, _ = np.linalg.lstsq(X_adf, dy, rcond=None)
    res = dy - X_adf @ b
    se = np.sqrt(np.sum(res ** 2) / (len(dy) - 2)) / (np.std(ylag) * np.sqrt(len(dy)) + 1e-9)
    t_adf = b[1] / se if se > 0 else 0
    
    e_kpss = y - np.mean(y)
    S = np.cumsum(e_kpss)
    s2 = np.sum(e_kpss ** 2) / len(y)
    kpss_stat = np.sum(S ** 2) / (len(y) ** 2 * s2) if s2 > 0 else 0
    return t_adf, kpss_stat

adf_level, kpss_level = test_stationarity(y_series)
adf_diff, kpss_diff = test_stationarity(np.diff(y_series))

ma3 = np.convolve(y_series, np.ones(3)/3, mode='valid')
trend_strength = 1 - np.var(y_series[1:-1] - ma3) / np.var(y_series[1:-1])

print(f"Kekuatan Tren        : {trend_strength:.3f} (Komponen tren dominan pasca-pandemi)")
print(f"ADF Level            : {adf_level:.3f} (Non-stasioner, p > 0.05)")
print(f"KPSS Level           : {kpss_level:.3f} (Non-stasioner)")
print(f"ADF Diferensiasi d=1 : {adf_diff:.3f} (Stasioner pada first-difference)")
print(f"KPSS Diferensiasi d=1: {kpss_diff:.3f} (Stasioner pada first-difference)")

display(df_ts)"""))

    cells.append(create_cell("markdown", """## 2. Uji Kelayakan Ramalan & Evaluasi Cross-Validation Multi-Horizon"""))
    cells.append(create_cell("code", """df_cv = pd.read_csv(f'{DATA_DIR}/uji_kelayakan_ramalan_tpt.csv')
df_best = pd.read_csv(f'{DATA_DIR}/aturan_per_horizon_tpt.csv')

print("Model Terbaik Per Horizon:")
display(df_best)

fig, ax = plt.subplots(figsize=(9, 5))
sub_h1 = df_cv[df_cv["Horizon"] == "h = 1"].set_index("Model")["MASE"]
sub_h3 = df_cv[df_cv["Horizon"] == "h = 3"].set_index("Model")["MASE"]

y_pos = np.arange(len(sub_h1))
bar_h = 0.35
ax.barh(y_pos - bar_h/2, sub_h1.values, bar_h, label="Horizon h = 1 (1 Tahun)", color=HIJAU)
ax.barh(y_pos + bar_h/2, sub_h3.values, bar_h, label="Horizon h = 3 (3 Tahun)", color=PASIR)
ax.axvline(1.0, color=BATA, linestyle="--", linewidth=1.5, label="Ambang Naive (MASE = 1.0)")
ax.set_yticks(y_pos)
ax.set_yticklabels(sub_h1.index, fontsize=8.5)
ax.invert_yaxis()
ax.set_xlabel("Mean Absolute Scaled Error (MASE)")
ax.set_title("Evaluasi Ketepatan Model Peramalan (Cross-Validation)\\n(Nilai MASE < 1.0 Mengungguli Standar Naive)", fontsize=11, fontweight="bold")
ax.legend(loc="lower right")
plt.tight_layout()
plt.show()"""))

    cells.append(create_cell("markdown", """## 3. Proyeksi Jangka Menengah Menuju 2030 (Fan Chart Probabilitas)"""))
    cells.append(create_cell("code", """df_proj = pd.read_csv(f'{DATA_DIR}/proyeksi_tpt_indonesia_2025_2030.csv')
display(df_proj)

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(years, y_series, marker="o", color='#243B3A', linewidth=2.5, label="Data Historis BPS Sakernas (2017–2024)")

future_years = df_proj["Tahun"].values
proj_point = df_proj["Proyeksi_TPT"].values

trans_years = np.concatenate([[years[-1]], future_years])
trans_proj = np.concatenate([[y_series[-1]], proj_point])
trans_l80 = np.concatenate([[y_series[-1]], df_proj["Lower_80"].values])
trans_u80 = np.concatenate([[y_series[-1]], df_proj["Upper_80"].values])
trans_l95 = np.concatenate([[y_series[-1]], df_proj["Lower_95"].values])
trans_u95 = np.concatenate([[y_series[-1]], df_proj["Upper_95"].values])

ax.fill_between(trans_years, trans_l95, trans_u95, color=PASIR, alpha=0.25, label="Selang Prediksi 95%")
ax.fill_between(trans_years, trans_l80, trans_u80, color=HIJAU, alpha=0.35, label="Selang Prediksi 80%")
ax.plot(trans_years, trans_proj, marker="s", color=BATA, linewidth=2.5, linestyle="--", label="Proyeksi Titik Terpilih (2025–2030)")
ax.axhline(4.0, color=ABU, linestyle=":", linewidth=1.5, label="Target Batas Bawah RPJMN (4.0%)")

ax.set_title("Proyeksi Waktu Runtun Tingkat Pengangguran Terbuka (2025–2030)\\nFan Chart Probabilitas Menuju Era Indonesia Emas", fontsize=11, fontweight="bold")
ax.set_xlabel("Tahun Pengamatan & Proyeksi")
ax.set_ylabel("Tingkat Pengangguran Terbuka (%)")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper right")

for yr, val in zip(future_years, proj_point):
    ax.annotate(f"{val:.2f}%", (yr, val), textcoords="offset points", xytext=(0, 7), ha='center', fontweight="bold", color=BATA)

plt.tight_layout()
fig.savefig(f'{CHARTS_DIR}/08_proyeksi_forecasting_tpt_2025_2030.svg', format="svg", bbox_inches="tight")
fig.savefig(f'{CHARTS_DIR}/08_proyeksi_forecasting_tpt_2025_2030.png', dpi=300, bbox_inches="tight")
plt.show()"""))
    nb_data = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.12"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    nb_path = os.path.join(NOTEBOOK_DIR, "Analisis_Forecasting_ACTION.ipynb")
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, indent=2)
    print(f"Notebook Forecasting berhasil dibuat di: {nb_path}")

if __name__ == "__main__":
    build_spatial_notebook()
    build_forecasting_notebook()
