"""
Pembuatan Grafik Infografis Pengayaan (Chart 14 & Chart 15).
Karya Kompetisi ACTION 2026.
Bebas em dash (R-02 antislop). Berbasis data resmi BPS Sakernas Agustus 2024.

1. Chart 14: Gunung Es Utilisasi Kerja (The Labor Underutilization Iceberg)
2. Chart 15: Dikotomi Perkotaan vs Perdesaan (Urban Queue vs Rural Trap)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_CLEAN = os.path.join(BASE_DIR, "data", "clean")
ASSETS_CHARTS = os.path.join(BASE_DIR, "assets", "charts")
os.makedirs(ASSETS_CHARTS, exist_ok=True)

# Palet warna
HIJAU = "#2F7D6E"  # Emerald / Positif / Penuh
BATA  = "#C0392B"  # Crimson / Kritis / Pengangguran
PASIR = "#D9B26F"  # Amber / Setengah Penganggur
ABU   = "#8896A0"  # Slate / Muted
BIRU  = "#2C3E50"  # Dark Slate Navy
KOTA  = "#34495E"  # Perkotaan
DESA  = "#27AE60"  # Perdesaan

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.edgecolor"] = "#BDC3C7"
plt.rcParams["axes.linewidth"] = 0.8

# ==============================================================================
# CHART 14: GUNUNG ES UTILISASI KERJA (THE UNDERUTILIZATION ICEBERG)
# ==============================================================================
def create_chart_14():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.8), gridspec_kw={"width_ratios": [1.1, 1.0]})
    fig.patch.set_facecolor("#FFFFFF")
    
    # ------------------ PANEL KIRI: Struktur Utilisasi 2024 ------------------
    ax1.set_facecolor("#F9FBFC")
    kategori = [
        "Pekerja Penuh Waktu\n(>=35 Jam/Minggu)",
        "Pekerja Paruh Waktu\nSukarela (<35 Jam)",
        "Setengah Penganggur\n(Jam Rendah & Cari Kerja)",
        "Pengangguran Terbuka\n(TPT Resmi BPS)"
    ]
    jumlah_juta = [95.85, 34.63, 11.56, 7.47]
    persen_share = [63.01, 22.77, 7.60, 4.91]  # dari total angkatan kerja 152.11 juta
    colors = [HIJAU, PASIR, "#E67E22", BATA]
    
    y_pos = np.arange(len(kategori))
    bars = ax1.barh(y_pos, jumlah_juta, color=colors, height=0.55, edgecolor="white", linewidth=1.2)
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(kategori, fontsize=10.5, fontweight="semibold", color=BIRU)
    ax1.invert_yaxis()  # Penuh di atas, penganggur di bawah
    ax1.set_xlabel("Jumlah Penduduk (Juta Orang)", fontsize=10.5, fontweight="semibold", color=BIRU)
    ax1.set_xlim(0, 115)
    ax1.grid(axis="x", linestyle=":", alpha=0.6, color="#BDC3C7")
    
    for bar, jt, pct in zip(bars, jumlah_juta, persen_share):
        w = bar.get_width()
        ax1.text(w + 1.8, bar.get_y() + bar.get_height()/2, f"{jt:.2f} Juta ({pct:.2f}%)",
                 va="center", ha="left", fontsize=9.5, fontweight="bold", color=BIRU)
        
    ax1.set_title("A. Anatomi Angkatan Kerja Indonesia (152,11 Juta Orang)\nAgustus 2024",
                  fontsize=12, fontweight="bold", color=BIRU, pad=12)
    
    # Highlight garis pembatas "Puncak Gunung Es"
    ax1.axhline(2.5, color=BATA, linestyle="--", linewidth=1.5, alpha=0.8)
    ax1.text(60, 2.38, "Batas Pengangguran Terbuka Resmi (Puncak Gunung Es)", 
             fontsize=8.5, color=BATA, fontweight="bold", ha="center")
    
    # ------------------ PANEL KANAN: Paradoks Perubahan 2023-2024 ------------
    ax2.set_facecolor("#F9FBFC")
    
    labels_delta = [
        "Pengangguran Terbuka (TPT)\n[Klaim Membaik]",
        "Setengah Penganggur\n[Kualitas Kerja Memburuk]",
        "Total Kurang Termanfaatkan\n(LU2: TPT + Setengah Penganggur)"
    ]
    delta_juta = [-0.39, +2.22, +1.83]
    delta_pct = [-0.41, +1.31, +0.87]
    bar_cols = [HIJAU if d < 0 else BATA for d in delta_juta]
    
    y_pos2 = np.arange(len(labels_delta))
    bars2 = ax2.barh(y_pos2, delta_juta, color=bar_cols, height=0.50, edgecolor="white", linewidth=1.2)
    
    ax2.axvline(0, color=BIRU, linewidth=1.0)
    ax2.set_yticks(y_pos2)
    ax2.set_yticklabels(labels_delta, fontsize=10, fontweight="semibold", color=BIRU)
    ax2.invert_yaxis()
    ax2.set_xlabel("Perubahan Jumlah Orang (Juta, 2023 ke 2024)", fontsize=10.5, fontweight="semibold", color=BIRU)
    ax2.set_xlim(-1.2, 3.2)
    ax2.grid(axis="x", linestyle=":", alpha=0.6, color="#BDC3C7")
    
    for bar, dj, dp in zip(bars2, delta_juta, delta_pct):
        w = bar.get_width()
        sign = "+" if dj > 0 else ""
        ha = "left" if dj >= 0 else "right"
        offset = 0.12 if dj >= 0 else -0.12
        ax2.text(w + offset, bar.get_y() + bar.get_height()/2, f"{sign}{dj:.2f} Juta ({sign}{dp:.2f} poin)",
                 va="center", ha=ha, fontsize=9.5, fontweight="bold",
                 color=BATA if dj > 0 else HIJAU)
                 
    ax2.set_title("B. Paradoks Dinamika Setahun Terakhir (Ags 2023 vs Ags 2024)\nPenurunan TPT Ditutupi Ledakan Setengah Pengangguran",
                  fontsize=12, fontweight="bold", color=BIRU, pad=12)
    
    # Kotak Callout Insight
    box_text = (
        "TEMUAN UTAMA (STANDAR ILO LU2):\n"
        "- TPT resmi turun dari 5,32% ke 4,91% (-390 ribu orang).\n"
        "- Namun setengah penganggur melonjak +23,8% (+2,22 juta orang)!\n"
        "- Total defisit utilisasi kerja (LU2) mencapai 19,03 JUTA ORANG (12,51%).\n"
        "- Angkatan kerja yang keluar dari status penganggur tidak masuk ke kerja formal,\n"
        "  melainkan terpaksa menerima pekerjaan paruh waktu berupah minim."
    )
    fig.text(0.5, 0.04, box_text, ha="center", fontsize=9.5,
             bbox=dict(boxstyle="round,pad=0.6", facecolor="#FFF8E7", edgecolor=PASIR, linewidth=1.5),
             color=BIRU, fontweight="medium")
    
    plt.subplots_adjust(top=0.86, bottom=0.22, left=0.18, right=0.96, wspace=0.45)
    
    plt.suptitle("GUNUNG ES KRISIS KETENAGAKERJAAN: DI BALIK PENURUNAN PENGANGGURAN TERBUKA",
                 fontsize=14, fontweight="bold", color=BIRU, y=0.96)
                 
    out_png = os.path.join(ASSETS_CHARTS, "14_gunung_es_utilisasi_kerja_nasional.png")
    out_svg = os.path.join(ASSETS_CHARTS, "14_gunung_es_utilisasi_kerja_nasional.svg")
    plt.savefig(out_png, dpi=300, bbox_inches="tight")
    plt.savefig(out_svg, bbox_inches="tight")
    plt.close()
    print("Generated Chart 14: 14_gunung_es_utilisasi_kerja_nasional.png & .svg")

# ==============================================================================
# CHART 15: DIKOTOMI KOTA VS DESA (URBAN QUEUE VS RURAL TRAP)
# ==============================================================================
def create_chart_15():
    fig, ax = plt.subplots(figsize=(13, 7.5))
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#F9FBFC")
    
    indikator = [
        "Tingkat Pengangguran Terbuka (TPT Total)",
        "Tingkat Pengangguran Pemuda (15-24 Tahun)",
        "Tingkat Setengah Pengangguran (Jam <35)",
        "Rasio Kerentanan Pemuda vs Dewasa",
        "Tingkat Ketidakaktifan (Bukan Angkatan Kerja)"
    ]
    
    kota_val = [5.79, 19.86, 6.09, 5.93, 31.34]
    desa_val = [3.67, 13.85, 10.60, 7.45, 26.45]
    satuan   = ["%", "%", "%", "x Lipat", "%"]
    
    y = np.arange(len(indikator))
    height = 0.32
    
    rects1 = ax.barh(y - height/2, kota_val, height, label="Perkotaan (Urban)", color=KOTA, edgecolor="white", linewidth=1.2)
    rects2 = ax.barh(y + height/2, desa_val, height, label="Perdesaan (Rural)", color=DESA, edgecolor="white", linewidth=1.2)
    
    ax.set_yticks(y)
    ax.set_yticklabels(indikator, fontsize=11, fontweight="semibold", color=BIRU)
    ax.invert_yaxis()
    ax.set_xlabel("Nilai Indikator (Persen / Rasio)", fontsize=11, fontweight="semibold", color=BIRU)
    ax.set_xlim(0, 37)
    ax.grid(axis="x", linestyle=":", alpha=0.6, color="#BDC3C7")
    
    # Label bar
    for r1, kv, st in zip(rects1, kota_val, satuan):
        w = r1.get_width()
        ax.text(w + 0.6, r1.get_y() + r1.get_height()/2, f"{kv:.2f}{st if st=='%' else 'x'}",
                va="center", ha="left", fontsize=9.5, fontweight="bold", color=KOTA)
                
    for r2, dv, st in zip(rects2, desa_val, satuan):
        w = r2.get_width()
        ax.text(w + 0.6, r2.get_y() + r2.get_height()/2, f"{dv:.2f}{st if st=='%' else 'x'}",
                va="center", ha="left", fontsize=9.5, fontweight="bold", color=DESA)
                
    ax.legend(loc="lower right", fontsize=11, framealpha=0.9, edgecolor="#BDC3C7")
    
    # Anotasi kontras tajam
    # Anotasi TPT Kota
    ax.annotate("Urban Queue: TPT Kota 1,58x lipat Desa\n(1 dari 5 pemuda kota menganggur terbuka)",
                xy=(19.86, 1 - height/2), xytext=(24, 0.8),
                arrowprops=dict(facecolor=KOTA, shrink=0.08, width=1.2, headwidth=6),
                fontsize=9, fontweight="bold", color=KOTA)
                
    # Anotasi Setengah Penganggur Desa
    ax.annotate("Rural Trap: Setengah Penganggur Desa 1,74x lipat Kota!\n(Pekerja terpaksa kerja subsisten jam rendah)",
                xy=(10.60, 2 + height/2), xytext=(15, 2.5),
                arrowprops=dict(facecolor=DESA, shrink=0.08, width=1.2, headwidth=6),
                fontsize=9, fontweight="bold", color=DESA)
                
    plt.title("DUA SISI MATA UANG KETENAGAKERJAAN: ANTREAN KOTA VS PERANGKAP DESA\n"
              "Potret Disparitas Pasar Kerja Perkotaan vs Perdesaan di Indonesia (BPS Sakernas Agustus 2024)",
              fontsize=13, fontweight="bold", color=BIRU, pad=18)
              
    callout = (
        "DUA REALITAS PASAR KERJA INDONESIA:\n"
        "1. KAWASAN PERKOTAAN (URBAN QUEUE): Antrean pencari kerja formal panjang. TPT mencapai 5,79% dan TPT pemuda menyentuh 19,86%.\n"
        "2. KAWASAN PERDESAAN (RURAL TRAP): Masyarakat tidak mampu menganggur (too poor to be unemployed), sehingga TPT tampak rendah (3,67%),\n"
        "   tetapi Setengah Pengangguran melonjak hingga 10,60% (didominasi sektor pertanian paruh waktu berupah rendah)."
    )
    fig.text(0.5, 0.02, callout, ha="center", fontsize=9.2,
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#F0F4F8", edgecolor="#BDC3C7", linewidth=1.2),
             color=BIRU, fontweight="medium")
             
    plt.subplots_adjust(top=0.88, bottom=0.18, left=0.28, right=0.96)
    
    out_png = os.path.join(ASSETS_CHARTS, "15_dikotomi_kota_desa_pengangguran.png")
    out_svg = os.path.join(ASSETS_CHARTS, "15_dikotomi_kota_desa_pengangguran.svg")
    plt.savefig(out_png, dpi=300, bbox_inches="tight")
    plt.savefig(out_svg, bbox_inches="tight")
    plt.close()
    print("Generated Chart 15: 15_dikotomi_kota_desa_pengangguran.png & .svg")

if __name__ == "__main__":
    create_chart_14()
    create_chart_15()
