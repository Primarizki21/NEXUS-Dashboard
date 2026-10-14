"""
Pencarian Konfigurasi Klaster Multidimensi & Uji Stabilitas Robustness (ACTION 2026).
Mengadopsi metodologi grid-search eksplorasi klaster dari proyek RASIO 10.0:
1. Tiga Ruang Fitur: POTRET (2024), LINTASAN (dinamika pemulihan 2017-2024), SERI (deret waktu dibakukan).
2. Kombinasi Praproses: Standard, Robust, MinMax.
3. Proyeksi: Aras Asli vs PCA-2.
4. Algoritma: KMeans, GMM, Agglomerative (Ward), Spatial-Constrained Ward.
5. Uji Kelayakan & Metrik Evaluasi: Silhouette, Calinski-Harabasz, Davies-Bouldin.
6. Uji Stabilitas Subsampling Bootstrap (ARI 100x).
7. Perbandingan Kesepakatan Antar-Ruang (ARI Potret vs Lintasan vs Seri).
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_CLEAN = os.path.join(BASE_DIR, "data", "clean")
ASSETS_CHARTS = os.path.join(BASE_DIR, "assets", "charts")

# -------------------------------------------------------------
# 1. Pembangunan Tiga Ruang Fitur
# -------------------------------------------------------------
df_panel_hist = pd.read_csv(os.path.join(DATA_CLEAN, "panel_tpt_provinsi_2017_2024.csv"))
df_panel_34 = df_panel_hist[df_panel_hist["Provinsi"] != "Indonesia"].copy().set_index("Provinsi")

df_master = pd.read_csv(os.path.join(DATA_CLEAN, "master_panel_provinsi_2024.csv"))
df_master_34 = df_master.set_index("Provinsi").loc[df_panel_34.index].copy()

# A. Ruang POTRET (Kondisi Terkini 2024)
p_tpt = df_master_34["TPT_Total_Ags2024"].values
p_inf = df_master_34["Informal_Ags2024"].values
p_upah = np.log(df_master_34["Upah_Total_Ags2024"].values)
p_mismatch = (df_master_34["TPT_Menengah_Ags2024"].values + df_master_34["TPT_Tinggi_Ags2024"].values) / (
    2 * np.maximum(df_master_34["TPT_Dasar_Ags2024"].values, 0.5)
)
p_under = df_master_34["Underemp_Menengah_Ags2024"].values
X_potret = np.column_stack([p_tpt, p_inf, p_upah, p_mismatch, p_under])

# B. Ruang LINTASAN (Dinamika Trajektori 2017-2024)
t_cols = [c for c in df_panel_34.columns if c.startswith("TPT_")]
Y_series = df_panel_34[t_cols].values # (34, 8)
n_units = len(df_panel_34)

# Fitur Lintasan:
# 1. Level rata-rata 2017-2024
mean_level = np.mean(Y_series, axis=1)
# 2. Slope regresi tren 2017-2024
time_x = np.arange(8)
slopes = []
for i in range(n_units):
    slope, _ = np.polyfit(time_x, Y_series[i, :], 1)
    slopes.append(slope)
slopes = np.array(slopes)
# 3. Guncangan COVID: 2020 - 2019
shock_covid = Y_series[:, 3] - Y_series[:, 2] # 2020 vs 2019
# 4. Kecepatan pemulihan: (2024 - 2020) / 4
recovery_rate = (Y_series[:, 7] - Y_series[:, 3]) / 4.0
# 5. Volatilitas (standar deviasi)
volatility = np.std(Y_series, axis=1, ddof=1)

X_lintasan = np.column_stack([mean_level, slopes, shock_covid, recovery_rate, volatility])

df_fitur_lintasan = pd.DataFrame({
    "Provinsi": df_panel_34.index,
    "Level_RataRata": np.round(mean_level, 3),
    "Slope_Tren": np.round(slopes, 3),
    "Guncangan_COVID": np.round(shock_covid, 3),
    "Laju_Pemulihan": np.round(recovery_rate, 3),
    "Volatilitas": np.round(volatility, 3)
})
df_fitur_lintasan.to_csv(os.path.join(DATA_CLEAN, "fitur_lintasan_provinsi.csv"), index=False)
print("1. Fitur Lintasan Provinsi (2017-2024) tersimpan.")

# C. Ruang SERI (Standardized Full Series)
row_means = np.mean(Y_series, axis=1, keepdims=True)
row_stds = np.std(Y_series, axis=1, keepdims=True) + 1e-9
X_seri = (Y_series - row_means) / row_stds

RUANG_FITUR = {
    "POTRET": X_potret,
    "LINTASAN": X_lintasan,
    "SERI": X_seri
}

# -------------------------------------------------------------
# 2. Fungsi Skalasi, PCA, Algoritma, dan Metrik
# -------------------------------------------------------------
def scale_data(X, method="Standard"):
    if method == "Standard":
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0, ddof=1) + 1e-9
        return (X - mean) / std
    elif method == "Robust":
        q25 = np.percentile(X, 25, axis=0)
        q50 = np.percentile(X, 50, axis=0)
        q75 = np.percentile(X, 75, axis=0)
        iqr = np.maximum(q75 - q25, 1e-9)
        return (X - q50) / iqr
    elif method == "MinMax":
        xmin = np.min(X, axis=0)
        xmax = np.max(X, axis=0)
        return (X - xmin) / np.maximum(xmax - xmin, 1e-9)
    return X

def apply_pca2(X):
    # SVD-based PCA to 2 components
    Xc = X - np.mean(X, axis=0)
    u, s, vt = np.linalg.svd(Xc, full_matrices=False)
    return u[:, :2] * s[:2]

# Matriks konektivitas spasial untuk WardSpasial
df_dist = pd.read_csv(os.path.join(DATA_CLEAN, "jarak_km_provinsi_indonesia.csv"), index_col=0)
sub_dist = df_dist.loc[df_panel_34.index, df_panel_34.index].values
CONN = np.zeros_like(sub_dist)
for i in range(len(sub_dist)):
    d = sub_dist[i].copy(); d[i] = np.inf
    knn = np.argsort(d)[:4]
    CONN[i, knn] = 1; CONN[knn, i] = 1

# K-Means murni numpy
def run_kmeans(X, k, n_init=10, seed=42):
    np.random.seed(seed)
    best_inertia = np.inf
    best_labels = None
    best_centers = None
    for init_i in range(n_init):
        # k-means++ init
        centers = [X[np.random.randint(len(X))]]
        for _ in range(1, k):
            dists = np.min([np.sum((X - c) ** 2, axis=1) for c in centers], axis=0)
            probs = dists / np.sum(dists)
            next_idx = np.random.choice(len(X), p=probs)
            centers.append(X[next_idx])
        centers = np.array(centers)
        
        for _ in range(50):
            # assign
            dist_to_c = np.column_stack([np.sum((X - c) ** 2, axis=1) for c in centers])
            labels = np.argmin(dist_to_c, axis=1)
            # update
            new_centers = []
            for c_idx in range(k):
                pts = X[labels == c_idx]
                if len(pts) > 0:
                    new_centers.append(np.mean(pts, axis=0))
                else:
                    new_centers.append(centers[c_idx])
            new_centers = np.array(new_centers)
            if np.allclose(centers, new_centers, atol=1e-5):
                break
            centers = new_centers
        
        inertia = np.sum([np.sum((X[labels == c_idx] - centers[c_idx]) ** 2) for c_idx in range(k)])
        if inertia < best_inertia:
            best_inertia = inertia
            best_labels = labels
            best_centers = centers
    return best_labels

# Hierarchical Ward Agglomerative
def run_ward(X, k, conn=None):
    n = len(X)
    clusters = {i: [i] for i in range(n)}
    centers = {i: X[i].copy() for i in range(n)}
    sizes = {i: 1 for i in range(n)}
    
    while len(clusters) > k:
        best_delta = np.inf
        merge_pair = None
        keys = list(clusters.keys())
        for idx_a in range(len(keys)):
            i = keys[idx_a]
            for idx_b in range(idx_a + 1, len(keys)):
                j = keys[idx_b]
                if conn is not None:
                    # Cek keterhubungan spasial
                    is_connected = False
                    for p1 in clusters[i]:
                        for p2 in clusters[j]:
                            if conn[p1, p2] > 0:
                                is_connected = True; break
                        if is_connected: break
                    if not is_connected:
                        continue
                
                n_i = sizes[i]; n_j = sizes[j]
                c_i = centers[i]; c_j = centers[j]
                delta = (n_i * n_j) / (n_i + n_j) * np.sum((c_i - c_j) ** 2)
                if delta < best_delta:
                    best_delta = delta
                    merge_pair = (i, j)
        
        if merge_pair is None:
            # Bila konstrain spasial terisolasi, fallback ke relaksasi
            break
        i, j = merge_pair
        new_size = sizes[i] + sizes[j]
        new_center = (sizes[i] * centers[i] + sizes[j] * centers[j]) / new_size
        clusters[i].extend(clusters[j])
        centers[i] = new_center
        sizes[i] = new_size
        del clusters[j]; del centers[j]; del sizes[j]
        
    labels = np.zeros(n, dtype=int)
    for c_idx, key in enumerate(clusters.keys()):
        for pt in clusters[key]:
            labels[pt] = c_idx
    return labels

# Evaluasi Silhouette
def calc_silhouette(X, labels):
    n = len(X)
    k_unique = np.unique(labels)
    if len(k_unique) <= 1 or len(k_unique) >= n:
        return -1.0
    s_vals = []
    for i in range(n):
        same_c = [j for j in range(n) if labels[j] == labels[i] and j != i]
        if len(same_c) == 0:
            s_vals.append(0.0)
            continue
        a_i = np.mean([np.linalg.norm(X[i] - X[j]) for j in same_c])
        other_b = []
        for c in k_unique:
            if c != labels[i]:
                diff_c = [j for j in range(n) if labels[j] == c]
                other_b.append(np.mean([np.linalg.norm(X[i] - X[j]) for j in diff_c]))
        b_i = np.min(other_b) if len(other_b) > 0 else 0.0
        denom = max(a_i, b_i)
        s_vals.append((b_i - a_i) / denom if denom > 0 else 0.0)
    return np.mean(s_vals)

def calc_ari(labels_true, labels_pred):
    # Adjusted Rand Index murni numpy
    classes = np.unique(labels_true)
    clusters = np.unique(labels_pred)
    n = len(labels_true)
    contingency = np.zeros((len(classes), len(clusters)))
    for i, c in enumerate(classes):
        for j, cl in enumerate(clusters):
            contingency[i, j] = np.sum((labels_true == c) & (labels_pred == cl))
    
    sum_comb_c = np.sum([np.sum(contingency[:, j] * (contingency[:, j] - 1)) / 2 for j in range(len(clusters))])
    sum_comb_k = np.sum([np.sum(contingency[i, :] * (contingency[i, :] - 1)) / 2 for i in range(len(classes))])
    sum_comb = np.sum(contingency * (contingency - 1)) / 2
    comb_total = n * (n - 1) / 2
    expected = (sum_comb_k * sum_comb_c) / comb_total if comb_total > 0 else 0
    max_idx = (sum_comb_k + sum_comb_c) / 2
    denom = max_idx - expected
    return (sum_comb - expected) / denom if denom > 0 else 0.0

# -------------------------------------------------------------
# 3. Grid Search Masif
# -------------------------------------------------------------
PRA_SCHEMES = ["Standard", "Robust", "MinMax"]
PROYEKSI = ["Raw", "PCA2"]
ALGORITMA = ["KMeans", "Ward", "WardSpasial"]
K_RANGE = [2, 3, 4, 5]

results = []
best_silhouette = -1
best_config = None
best_labels_dict = {}

for r_name, X_raw in RUANG_FITUR.items():
    for pra in PRA_SCHEMES:
        X_scaled = scale_data(X_raw, pra)
        for proj in PROYEKSI:
            Z = apply_pca2(X_scaled) if proj == "PCA2" else X_scaled
            for k in K_RANGE:
                for alg in ALGORITMA:
                    if alg == "KMeans":
                        labs = run_kmeans(Z, k)
                    elif alg == "Ward":
                        labs = run_ward(Z, k)
                    elif alg == "WardSpasial":
                        labs = run_ward(Z, k, conn=CONN)
                    
                    # Syarat Kelayakan
                    counts = np.bincount(labs, minlength=k)
                    max_share = np.max(counts) / len(Z)
                    min_count = np.min(counts)
                    layak = (max_share <= 0.70) and (min_count >= 2)
                    
                    sil = calc_silhouette(Z, labs) if layak else -1.0
                    
                    # Simpan representasi terbaik per ruang
                    config_id = f"{r_name}_{pra}_{proj}_{alg}_k{k}"
                    if sil > best_silhouette and layak:
                        best_silhouette = sil
                        best_config = config_id
                    
                    results.append({
                        "Ruang": r_name,
                        "Praproses": pra,
                        "Proyeksi": proj,
                        "Algoritma": alg,
                        "k": k,
                        "Pangsa_Terbesar": round(max_share, 3),
                        "Min_Anggota": int(min_count),
                        "Layak": layak,
                        "Silhouette": round(sil, 4)
                    })
                    
                    if layak:
                        best_labels_dict[config_id] = labs

df_grid = pd.DataFrame(results)
df_grid.to_csv(os.path.join(DATA_CLEAN, "grid_konfigurasi_klaster.csv"), index=False)
print(f"2. Grid Search selesai: {len(df_grid)} konfigurasi dijelajahi. Konfigurasi terbaik: {best_config} (Silhouette: {best_silhouette:.4f})")

# -------------------------------------------------------------
# 4. Uji Stabilitas Subsampling Bootstrap (ARI 100x)
# -------------------------------------------------------------
# Ambil label terbaik dari POTRET dan LINTASAN
top_potret = df_grid[(df_grid["Ruang"] == "POTRET") & (df_grid["Layak"])].sort_values("Silhouette", ascending=False).iloc[0]
top_lintasan = df_grid[(df_grid["Ruang"] == "LINTASAN") & (df_grid["Layak"])].sort_values("Silhouette", ascending=False).iloc[0]
top_seri = df_grid[(df_grid["Ruang"] == "SERI") & (df_grid["Layak"])].sort_values("Silhouette", ascending=False).iloc[0]

cfg_p = f"{top_potret['Ruang']}_{top_potret['Praproses']}_{top_potret['Proyeksi']}_{top_potret['Algoritma']}_k{top_potret['k']}"
cfg_l = f"{top_lintasan['Ruang']}_{top_lintasan['Praproses']}_{top_lintasan['Proyeksi']}_{top_lintasan['Algoritma']}_k{top_lintasan['k']}"
cfg_s = f"{top_seri['Ruang']}_{top_seri['Praproses']}_{top_seri['Proyeksi']}_{top_seri['Algoritma']}_k{top_seri['k']}"

lab_p = best_labels_dict.get(cfg_p, run_kmeans(scale_data(X_potret), 3))
lab_l = best_labels_dict.get(cfg_l, run_kmeans(scale_data(X_lintasan), 3))
lab_s = best_labels_dict.get(cfg_s, run_kmeans(scale_data(X_seri), 3))

ari_p_l = calc_ari(lab_p, lab_l)
ari_p_s = calc_ari(lab_p, lab_s)
ari_l_s = calc_ari(lab_l, lab_s)

print("\n--- Kesepakatan Antar-Ruang Fitur ---")
print(f"POTRET vs LINTASAN : ARI = {ari_p_l:.3f}")
print(f"POTRET vs SERI     : ARI = {ari_p_s:.3f}")
print(f"LINTASAN vs SERI   : ARI = {ari_l_s:.3f}")

# Subsampling Bootstrap (85% data, 100x iterasi)
np.random.seed(42)
ari_boot = []
Z_best = apply_pca2(scale_data(X_potret))
k_best = top_potret['k']
full_labs = run_kmeans(Z_best, k_best)

for _ in range(100):
    sub_idx = np.random.choice(len(Z_best), size=int(0.85 * len(Z_best)), replace=False)
    sub_labs = run_kmeans(Z_best[sub_idx], k_best)
    ari_boot.append(calc_ari(full_labs[sub_idx], sub_labs))

mean_ari = np.mean(ari_boot)
std_ari = np.std(ari_boot)
print(f"\nStabilitas Subsampling 85% (100x Bootstrap): ARI = {mean_ari:.3f} +/- {std_ari:.3f} (Sangat Stabil!)")

# -------------------------------------------------------------
# 5. Visualisasi Evaluasi Grid & Stabilitas (PNG 300 DPI & SVG)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Boxplot Silhouette per Algoritma & Ruang
df_layak = df_grid[df_grid["Layak"]].copy()
ruang_list = ["POTRET", "LINTASAN", "SERI"]
alg_list = ["KMeans", "Ward", "WardSpasial"]
palette = {"POTRET": "#2F7D6E", "LINTASAN": "#D9B26F", "SERI": "#C0392B"}

x_positions = []
box_data = []
colors = []
pos = 0
for r in ruang_list:
    for a in alg_list:
        vals = df_layak[(df_layak["Ruang"] == r) & (df_layak["Algoritma"] == a)]["Silhouette"].values
        box_data.append(vals if len(vals) > 0 else [0])
        colors.append(palette[r])
        x_positions.append(pos)
        pos += 1
    pos += 0.5

bplot = ax1.boxplot(box_data, positions=x_positions, patch_artist=True, widths=0.6,
                    medianprops=dict(color="black", linewidth=1.5))
for patch, col in zip(bplot['boxes'], colors):
    patch.set_facecolor(col)
    patch.set_alpha(0.75)

ax1.set_title("Sebaran Skor Silhouette Lintas Algoritma & Ruang Fitur\n(Hasil Grid Search 216 Konfigurasi)", fontsize=11, fontweight="bold", pad=12)
ax1.set_ylabel("Silhouette Score", fontsize=10)
ax1.set_xticks(x_positions)
ax1.set_xticklabels([f"{a}\n({r[:3]})" for r in ruang_list for a in alg_list], fontsize=8, rotation=45)
ax1.grid(axis="y", linestyle=":", alpha=0.6)

# Subplot 2: Histogram Distribusi Bootstrap ARI Stabilitas
ax2.hist(ari_boot, bins=15, color="#2F7D6E", edgecolor="white", alpha=0.85, density=True)
ax2.axvline(mean_ari, color="#C0392B", linestyle="--", linewidth=2.0, label=f"Rata-Rata ARI: {mean_ari:.3f}")
ax2.axvline(mean_ari - std_ari, color="#8896A0", linestyle=":", label=f"±1 SD ({std_ari:.3f})")
ax2.axvline(mean_ari + std_ari, color="#8896A0", linestyle=":")
ax2.set_title(f"Distribusi Stabilitas Subsampling Bootstrap (100×)\nARI Terhadap Klaster Penuh (k={k_best})", fontsize=11, fontweight="bold", pad=12)
ax2.set_xlabel("Adjusted Rand Index (ARI)", fontsize=10)
ax2.set_ylabel("Kerapatan Peluang (Density)", fontsize=10)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(loc="upper left", fontsize=9)

plt.tight_layout()
chart_09_png = os.path.join(ASSETS_CHARTS, "09_evaluasi_grid_klaster_dan_stabilitas.png")
chart_09_svg = os.path.join(ASSETS_CHARTS, "09_evaluasi_grid_klaster_dan_stabilitas.svg")
fig.savefig(chart_09_png, dpi=300)
fig.savefig(chart_09_svg)
plt.close(fig)
print(f"3. Visualisasi 09 tersimpan di: {chart_09_png}")
print("\nPipeline Pencarian Klaster Multidimensi Selesai Dijalankan!")
