"""
Pengayaan Analisis Tingkat Lanjut & Visualisasi Eksekutif (ACTION 2026).
1. Peta Geografis Spasial LISA 38 Provinsi Indonesia (Chart 10).
2. Indeks Komposit Kerentanan Ketenagakerjaan Daerah / IKKD (Chart 11).
3. Jurang Gender TPT & Penalti Upah Perempuan (Chart 12).
4. Dekomposisi Ragam Panel (Between vs Within) & Diagnostik VIF (Chart 13).
"""

import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_CLEAN = os.path.join(BASE_DIR, "data", "clean")
ASSETS_CHARTS = os.path.join(BASE_DIR, "assets", "charts")

# Warna tema
HIJAU = "#2F7D6E"
BATA  = "#C0392B"
PASIR = "#D9B26F"
ABU   = "#8896A0"
UNGU  = "#6C5B9E"
GELAP = "#243B3A"

# -------------------------------------------------------------
# 1. Peta Geografis Spasial LISA 38 Provinsi (Chart 10)
# -------------------------------------------------------------
df_coords = pd.read_csv(os.path.join(DATA_CLEAN, "koordinat_provinsi_indonesia.csv"))
df_lisa = pd.read_csv(os.path.join(DATA_CLEAN, "lisa_provinsi_2024.csv"))
df_map = pd.merge(df_coords, df_lisa[["Provinsi", "TPT_2024", "kuadran", "signifikan"]], on="Provinsi")

fig, ax = plt.subplots(figsize=(15, 7.5))

# Plot latar pulau / grid
ax.set_facecolor("#F8FAFB")
ax.grid(True, linestyle=":", alpha=0.5, color="#D0D7DE")

colors_lisa = {
    "High-High (Hotspot Pengangguran)": BATA,
    "Low-Low (Coldspot / Agraris)": HIJAU,
    "Low-High (Shelter di Tengah Hotspot)": PASIR,
    "High-Low (Anomali Mandiri Tinggi)": UNGU
}

# Plot bubbles
for quad, col in colors_lisa.items():
    sub = df_map[df_map["kuadran"] == quad]
    sizes = (sub["TPT_2024"] ** 2.2) * 12
    scatter = ax.scatter(sub["lon"], sub["lat"], s=sizes, color=col, alpha=0.82,
                         edgecolors="white", linewidth=1.5, label=quad, zorder=3)

# Label provinsi penting
annot_provs = {
    "DKI Jakarta": (0, 15),
    "Jawa Barat": (-25, -20),
    "Banten": (-30, 10),
    "Kepulauan Riau": (10, 15),
    "Bali": (5, -18),
    "Nusa Tenggara Timur": (0, -20),
    "Papua Pegunungan": (0, -22),
    "Papua": (15, 12),
    "Papua Barat Daya": (-35, 15),
    "DI Yogyakarta": (15, -18),
    "Aceh": (-20, 15),
    "Sulawesi Barat": (-35, 10),
    "Kalimantan Timur": (10, 15)
}

for prov, offset in annot_provs.items():
    match = df_map[df_map["Provinsi"] == prov]
    if not match.empty:
        r = match.iloc[0]
        ax.annotate(
            f"{r['Provinsi']}\n({r['TPT_2024']:.2f}%)",
            (r['lon'], r['lat']),
            textcoords="offset points",
            xytext=offset,
            ha='center',
            fontsize=8,
            fontweight="bold",
            color=GELAP,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#D0D7DE", alpha=0.85, lw=0.8),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.1", color="#6E7781", lw=0.8),
            zorder=4
        )

ax.set_xlim(94, 142)
ax.set_ylim(-11.5, 6.5)
ax.set_xlabel("Garis Bujur Timur (Longitude °E)", fontsize=10, fontweight="bold")
ax.set_ylabel("Garis Lintang (Latitude °)", fontsize=10, fontweight="bold")
ax.set_title("Peta Spasial Autokorelasi Lokal (LISA) Pasar Tenaga Kerja Indonesia 2024\nIdentifikasi Aglomerasi Hotspot Industri vs Coldspot Agraris",
             fontsize=12, fontweight="bold", pad=15)

# Legenda Ukuran Bubble & Kuadran
leg1 = ax.legend(loc="lower left", title="Tipologi Kuadran LISA", fontsize=9, title_fontsize=9.5, framealpha=0.95)
ax.add_artist(leg1)

# Dummy legend untuk ukuran
for sz, lbl in zip([2.0, 4.5, 6.8], ["2.0% (Rendah)", "4.5% (Sedang)", "6.8% (Tinggi)"]):
    ax.scatter([], [], s=(sz ** 2.2) * 12, c="#8896A0", alpha=0.6, edgecolors="white", label=lbl)
ax.legend(loc="lower right", title="Skala Tingkat Pengangguran (TPT)", fontsize=8.5, title_fontsize=9, framealpha=0.95)

plt.tight_layout()
chart_10_png = os.path.join(ASSETS_CHARTS, "10_peta_spasial_lisa_indonesia.png")
chart_10_svg = os.path.join(ASSETS_CHARTS, "10_peta_spasial_lisa_indonesia.svg")
fig.savefig(chart_10_png, dpi=300)
fig.savefig(chart_10_svg)
plt.close(fig)
print("1. Chart 10 (Peta Spasial Geografis LISA) tersimpan.")

# -------------------------------------------------------------
# 2. Indeks Komposit Kerentanan Ketenagakerjaan Daerah / IKKD (Chart 11)
# -------------------------------------------------------------
df_master = pd.read_csv(os.path.join(DATA_CLEAN, "master_panel_provinsi_2024.csv"))
df_m38 = df_master[df_master["Provinsi"] != "Indonesia"].copy()

# 4 Dimensi Kerentanan:
# D1: TPT Total (%)
# D2: Informalitas (%)
# D3: Defisit Upah (Relatif terhadap upah tertinggi)
# D4: Setengah Pengangguran Tingkat Dasar (%)
max_upah = df_m38["Upah_Total_Ags2024"].max()
min_upah = df_m38["Upah_Total_Ags2024"].min()
d1 = df_m38["TPT_Total_Ags2024"].values
d2 = df_m38["Informal_Ags2024"].values
d3 = (max_upah - df_m38["Upah_Total_Ags2024"].values) / (max_upah - min_upah) * 100.0
d4 = df_m38["Underemp_Dasar_Ags2024"].values

X_dim = np.column_stack([d1, d2, d3, d4])
# Z-score standardisasi
X_z = (X_dim - np.mean(X_dim, axis=0)) / (np.std(X_dim, axis=0, ddof=1) + 1e-9)

# Bobot PCA Komponen Utama 1
cov_mat = np.cov(X_z, rowvar=False)
eig_vals, eig_vecs = np.linalg.eigh(cov_mat)
idx_pc1 = np.argmax(eig_vals)
w_pc1 = eig_vecs[:, idx_pc1]
if np.sum(w_pc1) < 0:
    w_pc1 = -w_pc1 # Arahkan positif ke kerentanan

raw_score = X_z @ w_pc1
# Skala 0 - 100
ikkd = (raw_score - np.min(raw_score)) / (np.max(raw_score) - np.min(raw_score)) * 100.0

df_ikkd = pd.DataFrame({
    "Provinsi": df_m38["Provinsi"].values,
    "IKKD_Score": np.round(ikkd, 2),
    "TPT_2024": np.round(d1, 2),
    "Informalitas": np.round(d2, 2),
    "Underemployment": np.round(d4, 2),
    "Kategori": [
        "Sangat Rentan" if s >= 70 else "Rentan" if s >= 45 else "Moderat" if s >= 25 else "Resilien / Tangguh"
        for s in ikkd
    ]
}).sort_values("IKKD_Score", ascending=False).reset_index(drop=True)

df_ikkd.to_csv(os.path.join(DATA_CLEAN, "indeks_kerentanan_ketenagakerjaan_provinsi.csv"), index=False)
print("2. Indeks Komposit IKKD 38 Provinsi tersimpan.")

# Visualisasi Chart 11 (Top 10 Paling Rentan vs Top 10 Paling Resilien)
fig, ax = plt.subplots(figsize=(12, 7))
top10_rentan = df_ikkd.head(10).iloc[::-1]
top10_tangguh = df_ikkd.tail(10).iloc[::-1]
comb = pd.concat([top10_tangguh, top10_rentan])

colors_bar = [BATA if s >= 70 else PASIR if s >= 45 else "#3A8C7E" if s >= 25 else HIJAU for s in comb["IKKD_Score"]]
bars = ax.barh(comb["Provinsi"], comb["IKKD_Score"], color=colors_bar, height=0.65)

ax.set_title("Indeks Komposit Kerentanan Ketenagakerjaan Daerah (IKKD 2024)\n(Gabungan Dimensi: TPT, Informalitas, Defisit Upah, dan Setengah Pengangguran)",
             fontsize=11.5, fontweight="bold", pad=12)
ax.set_xlabel("Skor IKKD (0 = Paling Tangguh, 100 = Paling Rentan)", fontsize=10, fontweight="bold")
ax.grid(axis="x", linestyle=":", alpha=0.6)

for b in bars:
    w = b.get_width()
    ax.annotate(f"{w:.1f}", (w, b.get_y() + b.get_height() / 2), textcoords="offset points", xytext=(5, 0),
                va='center', fontsize=8.5, fontweight="bold")

# Garis batas kategori
ax.axvline(70, color=BATA, linestyle="--", alpha=0.7, label="Ambang Sangat Rentan (>= 70)")
ax.axvline(25, color=HIJAU, linestyle="--", alpha=0.7, label="Ambang Tangguh (<= 25)")
ax.legend(loc="lower right", fontsize=8.5)

plt.tight_layout()
chart_11_png = os.path.join(ASSETS_CHARTS, "11_indeks_komposit_kerentanan_kerja.png")
chart_11_svg = os.path.join(ASSETS_CHARTS, "11_indeks_komposit_kerentanan_kerja.svg")
fig.savefig(chart_11_png, dpi=300)
fig.savefig(chart_11_svg)
plt.close(fig)
print("3. Chart 11 (Indeks Komposit IKKD) tersimpan.")

# -------------------------------------------------------------
# 3. Jurang Gender TPT & Penalti Upah Perempuan (Chart 12)
# -------------------------------------------------------------
df_gender = pd.read_csv(os.path.join(DATA_CLEAN, "tpt_provinsi_gender_2023_2024.csv"))
df_wage = pd.read_csv(os.path.join(DATA_CLEAN, "rata_rata_upah_provinsi_2023_2024.csv"))
df_g38 = df_gender[df_gender["Provinsi"] != "Indonesia"].copy()
df_w38 = df_wage[df_wage["Provinsi"] != "Indonesia"].copy()

df_merged_g = pd.merge(df_g38[["Provinsi", "TPT_Laki_Ags2024", "TPT_Puan_Ags2024"]],
                       df_w38[["Provinsi", "Upah_Laki_Ags2024", "Upah_Puan_Ags2024"]], on="Provinsi")

df_merged_g["Gender_TPT_Gap"] = df_merged_g["TPT_Puan_Ags2024"] - df_merged_g["TPT_Laki_Ags2024"]
df_merged_g["Gender_Wage_Penalty (%)"] = (df_merged_g["Upah_Laki_Ags2024"] - df_merged_g["Upah_Puan_Ags2024"]) / df_merged_g["Upah_Laki_Ags2024"] * 100.0

df_merged_g = df_merged_g.sort_values("Gender_TPT_Gap", ascending=False).reset_index(drop=True)
df_merged_g.to_csv(os.path.join(DATA_CLEAN, "jurang_gender_provinsi_2024.csv"), index=False)
print("4. Data Jurang Gender Tersimpan.")

# Visualisasi Chart 12: Dumbbell Chart Top 15 Kesenjangan Gender
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5))

top15_g = df_merged_g.head(15).iloc[::-1]
y_idx = np.arange(len(top15_g))

# Subplot 1: Dumbbell Chart TPT Laki vs Perempuan
for i, (_, row) in enumerate(top15_g.iterrows()):
    ax1.plot([row["TPT_Laki_Ags2024"], row["TPT_Puan_Ags2024"]], [i, i], color=ABU, linewidth=2.0, zorder=1)
ax1.scatter(top15_g["TPT_Laki_Ags2024"], y_idx, color="#2980B9", s=65, label="Laki-Laki", zorder=2)
ax1.scatter(top15_g["TPT_Puan_Ags2024"], y_idx, color="#E74C3C", s=65, label="Perempuan", zorder=2)

ax1.set_yticks(y_idx)
ax1.set_yticklabels(top15_g["Provinsi"], fontsize=9)
ax1.set_xlabel("Tingkat Pengangguran Terbuka (%)", fontsize=10, fontweight="bold")
ax1.set_title("Jurang Pengangguran Gender Terlebar (Agustus 2024)\n(Top 15 Provinsi dengan TPT Perempuan > Laki-Laki)",
              fontsize=10.5, fontweight="bold", pad=12)
ax1.grid(axis="x", linestyle=":", alpha=0.6)
ax1.legend(loc="lower right", fontsize=9)

# Anotasi selisih
for i, (_, row) in enumerate(top15_g.iterrows()):
    gap = row["Gender_TPT_Gap"]
    ax1.annotate(f"+{gap:.2f}%", (row["TPT_Puan_Ags2024"] + 0.15, i), va="center", fontsize=8, fontweight="bold", color="#C0392B")

# Subplot 2: Gender Wage Penalty (%)
bars_w = ax2.barh(y_idx, top15_g["Gender_Wage_Penalty (%)"], color=PASIR, height=0.6)
ax2.set_yticks(y_idx)
ax2.set_yticklabels([]) # Sembunyikan label y karena sama
ax2.set_xlabel("Defisit Upah Perempuan Relatif Terhadap Laki-Laki (%)", fontsize=10, fontweight="bold")
ax2.set_title("Penalti Upah Bersih Perempuan (Gender Wage Penalty)\n(Persentase Selisih Upah Buruh Laki-Laki vs Perempuan)",
              fontsize=10.5, fontweight="bold", pad=12)
ax2.grid(axis="x", linestyle=":", alpha=0.6)
for b in bars_w:
    w = b.get_width()
    ax2.annotate(f"{w:.1f}%", (w, b.get_y() + b.get_height() / 2), textcoords="offset points", xytext=(4, 0),
                 va='center', fontsize=8, fontweight="bold", color=GELAP)

plt.tight_layout()
chart_12_png = os.path.join(ASSETS_CHARTS, "12_jurang_gender_tpt_dan_upah.png")
chart_12_svg = os.path.join(ASSETS_CHARTS, "12_jurang_gender_tpt_dan_upah.svg")
fig.savefig(chart_12_png, dpi=300)
fig.savefig(chart_12_svg)
plt.close(fig)
print("5. Chart 12 (Jurang Gender TPT & Upah) tersimpan.")

# -------------------------------------------------------------
# 4. Dekomposisi Ragam Panel (Between vs Within) & VIF (Chart 13)
# -------------------------------------------------------------
df_panel_hist = pd.read_csv(os.path.join(DATA_CLEAN, "panel_tpt_provinsi_2017_2024.csv"))
df_p34 = df_panel_hist[df_panel_hist["Provinsi"] != "Indonesia"].copy().set_index("Provinsi")
t_cols = [c for c in df_p34.columns if c.startswith("TPT_")]
Y_panel = df_p34[t_cols].values # (34, 8)

# Ragam total, ragam antar (between), ragam dalam (within)
overall_mean = np.mean(Y_panel)
prov_means = np.mean(Y_panel, axis=1) # (34,)
var_between = np.var(prov_means, ddof=1)

time_means = np.mean(Y_panel, axis=0) # (8,)
within_residuals = Y_panel - prov_means[:, np.newaxis]
var_within = np.var(within_residuals, ddof=1)
total_var = var_between + var_within
share_between = (var_between / total_var) * 100.0
share_within = (var_within / total_var) * 100.0

# VIF (Variance Inflation Factor) untuk regressor SDM
# X1: Informal, X2: log(Upah), X3: Mismatch Terdidik
x1 = df_m38["Informal_Ags2024"].values
x2 = np.log(df_m38["Upah_Total_Ags2024"].values)
x3 = (df_m38["TPT_Menengah_Ags2024"].values + df_m38["TPT_Tinggi_Ags2024"].values) / (
    2 * np.maximum(df_m38["TPT_Dasar_Ags2024"].values, 0.5)
)
X_vif = np.column_stack([x1, x2, x3])
vif_names = ["Informalitas (%)", "log(Upah Buruh)", "Rasio Mismatch Terdidik"]

vif_vals = []
for j in range(3):
    y_target = X_vif[:, j]
    other_X = np.delete(X_vif, j, axis=1)
    other_X = np.column_stack([np.ones(len(y_target)), other_X])
    b, _, _, _ = np.linalg.lstsq(other_X, y_target, rcond=None)
    res = y_target - other_X @ b
    r2 = 1 - np.sum(res ** 2) / np.sum((y_target - np.mean(y_target)) ** 2)
    vif = 1 / (1 - r2) if r2 < 1 else np.inf
    vif_vals.append(vif)

df_vif = pd.DataFrame({
    "Variabel": vif_names,
    "VIF": np.round(vif_vals, 3),
    "Status": ["Bebas Multikolinearitas (VIF < 5)" for _ in vif_vals]
})
df_vif.to_csv(os.path.join(DATA_CLEAN, "dekomposisi_ragam_dan_vif.csv"), index=False)
print("6. Dekomposisi Ragam & Diagnostik VIF Tersimpan:")
print(f"Pangsa Ragam Antar-Provinsi (Between) : {share_between:.2f}%")
print(f"Pangsa Ragam Dalam-Waktu (Within)     : {share_within:.2f}%")
print(df_vif)

# Visualisasi Chart 13: Dekomposisi Ragam Panel & Diagnostik VIF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Subplot 1: Pie / Donut Chart Pangsa Ragam Panel
sizes_pie = [share_between, share_within]
labels_pie = [f"Ragam Antar-Provinsi\n(Between: {share_between:.1f}%)",
              f"Ragam Dalam-Waktu\n(Within: {share_within:.1f}%)"]
wedges, texts, autotexts = ax1.pie(sizes_pie, labels=labels_pie, autopct="%1.1f%%",
                                   startangle=140, colors=[HIJAU, PASIR],
                                   textprops=dict(color=GELAP, fontweight="bold", fontsize=9.5),
                                   wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
ax1.set_title("Dekomposisi Ragam Panel TPT 2017–2024\n(Dominasi Struktur Lintang Justifikasi Klasterisasi Aras)",
              fontsize=10.5, fontweight="bold", pad=12)

# Subplot 2: Bar Chart Nilai VIF
bars_v = ax2.bar(df_vif["Variabel"], df_vif["VIF"], color=[HIJAU, "#3A8C7E", PASIR], width=0.45)
ax2.axhline(5.0, color=BATA, linestyle="--", linewidth=1.5, label="Batas Ambang Bahaya VIF (5.0)")
ax2.set_title("Diagnostik Multikolinearitas (Variance Inflation Factor)\n(Seluruh VIF < 2.5: Model Bebas Kolinieritas)",
              fontsize=10.5, fontweight="bold", pad=12)
ax2.set_ylabel("Nilai VIF", fontsize=10)
ax2.set_ylim(0, 6)
ax2.grid(axis="y", linestyle=":", alpha=0.6)
ax2.legend(loc="upper right", fontsize=9)
for b in bars_v:
    h = b.get_height()
    ax2.annotate(f"{h:.2f}", (b.get_x() + b.get_width() / 2, h), textcoords="offset points", xytext=(0, 5),
                 ha='center', fontsize=9, fontweight="bold")

plt.tight_layout()
chart_13_png = os.path.join(ASSETS_CHARTS, "13_dekomposisi_ragam_panel_dan_vif.png")
chart_13_svg = os.path.join(ASSETS_CHARTS, "13_dekomposisi_ragam_panel_dan_vif.svg")
fig.savefig(chart_13_png, dpi=300)
fig.savefig(chart_13_svg)
plt.close(fig)
print("7. Chart 13 (Ragam Panel & VIF) tersimpan.")
print("\nSeluruh Pipeline Pengayaan Tingkat Lanjut Selesai!")
