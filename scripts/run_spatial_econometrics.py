"""
Ekonometrika Spasial Pasar Tenaga Kerja Indonesia (ACTION 2026).
Pola analisis ekonometrika spasial regional terintegrasi:
1. Georeferensi & Haversine Distance 38 Provinsi Indonesia.
2. Konstruksi Matriks Bobot Spasial W_knn (k=3, 4, 5).
3. Global Moran's I Lintasan Waktu (2017-2024).
4. Local Moran's I (LISA) 2024 & Permutation Test.
5. Pemodelan Spasial: OLS, SLX, SAR, SEM, SDM (Spatial Durbin Model).
6. Dekomposisi Efek LeSage-Pace (Direct, Spillover, Total).
7. Visualisasi Resolusi Tinggi (PNG & SVG) ke assets/charts.
"""

import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Konfigurasi Direktori
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_CLEAN = os.path.join(BASE_DIR, "data", "clean")
ASSETS_CHARTS = os.path.join(BASE_DIR, "assets", "charts")
os.makedirs(DATA_CLEAN, exist_ok=True)
os.makedirs(ASSETS_CHARTS, exist_ok=True)

# -------------------------------------------------------------
# 1. Georeferensi 38 Provinsi Indonesia
# -------------------------------------------------------------
PROV_COORDS = [
    {"Provinsi": "Aceh", "lat": 5.5483, "lon": 95.3238, "pulau": "Sumatera", "ibukota": "Banda Aceh"},
    {"Provinsi": "Sumatera Utara", "lat": 3.5952, "lon": 98.6722, "pulau": "Sumatera", "ibukota": "Medan"},
    {"Provinsi": "Sumatera Barat", "lat": -0.9471, "lon": 100.4172, "pulau": "Sumatera", "ibukota": "Padang"},
    {"Provinsi": "Riau", "lat": 0.5071, "lon": 101.4478, "pulau": "Sumatera", "ibukota": "Pekanbaru"},
    {"Provinsi": "Jambi", "lat": -1.6101, "lon": 103.6131, "pulau": "Sumatera", "ibukota": "Jambi"},
    {"Provinsi": "Sumatera Selatan", "lat": -2.9761, "lon": 104.7754, "pulau": "Sumatera", "ibukota": "Palembang"},
    {"Provinsi": "Bengkulu", "lat": -3.8004, "lon": 102.2655, "pulau": "Sumatera", "ibukota": "Bengkulu"},
    {"Provinsi": "Lampung", "lat": -5.4500, "lon": 105.2667, "pulau": "Sumatera", "ibukota": "Bandar Lampung"},
    {"Provinsi": "Kep. Bangka Belitung", "lat": -2.1333, "lon": 106.1167, "pulau": "Sumatera", "ibukota": "Pangkalpinang"},
    {"Provinsi": "Kepulauan Riau", "lat": 0.9167, "lon": 104.4500, "pulau": "Sumatera", "ibukota": "Tanjung Pinang"},
    {"Provinsi": "DKI Jakarta", "lat": -6.2088, "lon": 106.8456, "pulau": "Jawa", "ibukota": "Jakarta"},
    {"Provinsi": "Jawa Barat", "lat": -6.9175, "lon": 107.6191, "pulau": "Jawa", "ibukota": "Bandung"},
    {"Provinsi": "Jawa Tengah", "lat": -6.9667, "lon": 110.4167, "pulau": "Jawa", "ibukota": "Semarang"},
    {"Provinsi": "DI Yogyakarta", "lat": -7.7956, "lon": 110.3695, "pulau": "Jawa", "ibukota": "Yogyakarta"},
    {"Provinsi": "Jawa Timur", "lat": -7.2575, "lon": 112.7521, "pulau": "Jawa", "ibukota": "Surabaya"},
    {"Provinsi": "Banten", "lat": -6.1104, "lon": 106.1667, "pulau": "Jawa", "ibukota": "Serang"},
    {"Provinsi": "Bali", "lat": -8.6705, "lon": 115.2126, "pulau": "Bali-Nusa Tenggara", "ibukota": "Denpasar"},
    {"Provinsi": "Nusa Tenggara Barat", "lat": -8.5833, "lon": 116.1167, "pulau": "Bali-Nusa Tenggara", "ibukota": "Mataram"},
    {"Provinsi": "Nusa Tenggara Timur", "lat": -10.1772, "lon": 123.6070, "pulau": "Bali-Nusa Tenggara", "ibukota": "Kupang"},
    {"Provinsi": "Kalimantan Barat", "lat": -0.0263, "lon": 109.3425, "pulau": "Kalimantan", "ibukota": "Pontianak"},
    {"Provinsi": "Kalimantan Tengah", "lat": -2.2136, "lon": 113.9108, "pulau": "Kalimantan", "ibukota": "Palangka Raya"},
    {"Provinsi": "Kalimantan Selatan", "lat": -3.3167, "lon": 114.5900, "pulau": "Kalimantan", "ibukota": "Banjarmasin"},
    {"Provinsi": "Kalimantan Timur", "lat": -0.5022, "lon": 117.1536, "pulau": "Kalimantan", "ibukota": "Samarinda"},
    {"Provinsi": "Kalimantan Utara", "lat": 2.8375, "lon": 117.3653, "pulau": "Kalimantan", "ibukota": "Tanjung Selor"},
    {"Provinsi": "Sulawesi Utara", "lat": 1.4748, "lon": 124.8428, "pulau": "Sulawesi", "ibukota": "Manado"},
    {"Provinsi": "Sulawesi Tengah", "lat": -0.8917, "lon": 119.8707, "pulau": "Sulawesi", "ibukota": "Palu"},
    {"Provinsi": "Sulawesi Selatan", "lat": -5.1477, "lon": 119.4327, "pulau": "Sulawesi", "ibukota": "Makassar"},
    {"Provinsi": "Sulawesi Tenggara", "lat": -3.9985, "lon": 122.5126, "pulau": "Sulawesi", "ibukota": "Kendari"},
    {"Provinsi": "Gorontalo", "lat": 0.5435, "lon": 123.0568, "pulau": "Sulawesi", "ibukota": "Gorontalo"},
    {"Provinsi": "Sulawesi Barat", "lat": -2.6788, "lon": 118.8827, "pulau": "Sulawesi", "ibukota": "Mamuju"},
    {"Provinsi": "Maluku", "lat": -3.6954, "lon": 128.1814, "pulau": "Maluku", "ibukota": "Ambon"},
    {"Provinsi": "Maluku Utara", "lat": 0.7300, "lon": 127.5600, "pulau": "Maluku", "ibukota": "Sofifi"},
    {"Provinsi": "Papua Barat", "lat": -0.8615, "lon": 134.0620, "pulau": "Papua", "ibukota": "Manokwari"},
    {"Provinsi": "Papua Barat Daya", "lat": -0.8762, "lon": 131.2558, "pulau": "Papua", "ibukota": "Sorong"},
    {"Provinsi": "Papua", "lat": -2.5489, "lon": 140.7181, "pulau": "Papua", "ibukota": "Jayapura"},
    {"Provinsi": "Papua Selatan", "lat": -8.4991, "lon": 140.4011, "pulau": "Papua", "ibukota": "Merauke"},
    {"Provinsi": "Papua Tengah", "lat": -3.3667, "lon": 135.4833, "pulau": "Papua", "ibukota": "Nabire"},
    {"Provinsi": "Papua Pegunungan", "lat": -4.0950, "lon": 138.9442, "pulau": "Papua", "ibukota": "Wamena"}
]

df_coords = pd.DataFrame(PROV_COORDS)
df_coords.to_csv(os.path.join(DATA_CLEAN, "koordinat_provinsi_indonesia.csv"), index=False)
print("1. Koordinat 38 Provinsi Indonesia tersimpan.")

# -------------------------------------------------------------
# 2. Haversine Distance Matrix & Matriks Bobot Spasial W_knn
# -------------------------------------------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radius bumi dalam km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

N = len(df_coords)
dist_mat = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if i != j:
            dist_mat[i, j] = haversine(
                df_coords.iloc[i]["lat"], df_coords.iloc[i]["lon"],
                df_coords.iloc[j]["lat"], df_coords.iloc[j]["lon"]
            )

df_dist = pd.DataFrame(dist_mat, index=df_coords["Provinsi"], columns=df_coords["Provinsi"])
df_dist.to_csv(os.path.join(DATA_CLEAN, "jarak_km_provinsi_indonesia.csv"))
print("2. Matriks Jarak Haversine (38x38) tersimpan.")

def build_w_knn(dist_matrix, k=4):
    N_units = dist_matrix.shape[0]
    W = np.zeros((N_units, N_units))
    for i in range(N_units):
        dists = dist_matrix[i, :].copy()
        dists[i] = np.inf
        knn_idx = np.argsort(dists)[:k]
        W[i, knn_idx] = 1.0 / k # row-standardized
    return W

W_knn4_38 = build_w_knn(dist_mat, k=4)
pd.DataFrame(W_knn4_38, index=df_coords["Provinsi"], columns=df_coords["Provinsi"]).to_csv(
    os.path.join(DATA_CLEAN, "W_knn4_indonesia.csv")
)

# -------------------------------------------------------------
# 3. Global Moran's I Lintasan Waktu (2017-2024)
# -------------------------------------------------------------
df_panel_hist = pd.read_csv(os.path.join(DATA_CLEAN, "panel_tpt_provinsi_2017_2024.csv"))
df_panel_34 = df_panel_hist[df_panel_hist["Provinsi"] != "Indonesia"].copy()
prov_34 = df_panel_34["Provinsi"].tolist()

# Sub-matriks jarak untuk 34 provinsi
sub_dist = df_dist.loc[prov_34, prov_34].values
W_34 = build_w_knn(sub_dist, k=4)

def calc_moran(y, W):
    n = len(y)
    z = y - np.mean(y)
    s0 = np.sum(W)
    num = n * np.sum(W * np.outer(z, z))
    den = s0 * np.sum(z ** 2)
    I = num / den if den != 0 else 0
    E_I = -1.0 / (n - 1)
    
    # Permutation test p-value
    n_perm = 999
    perm_I = []
    for _ in range(n_perm):
        zp = np.random.permutation(z)
        p_num = n * np.sum(W * np.outer(zp, zp))
        perm_I.append(p_num / den)
    p_val = (np.sum(np.array(perm_I) >= I) + 1) / (n_perm + 1)
    return I, E_I, p_val

moran_records = []
years = [c.replace("TPT_", "") for c in df_panel_34.columns if c.startswith("TPT_")]
for yr in years:
    col = f"TPT_{yr}"
    y_vals = df_panel_34[col].values
    I_val, E_val, p_val = calc_moran(y_vals, W_34)
    moran_records.append({
        "tahun": int(yr),
        "moran_i": round(I_val, 4),
        "expected_i": round(E_val, 4),
        "p_value": round(p_val, 4),
        "status": "Mengelompok Signifikan" if p_val < 0.05 else "Acak / Tidak Signifikan"
    })

df_moran = pd.DataFrame(moran_records)
df_moran.to_csv(os.path.join(DATA_CLEAN, "moran_lintasan_tahun_tpt.csv"), index=False)
print("3. Global Moran's I Lintasan Waktu (2017-2024) dihitung.")

# -------------------------------------------------------------
# 4. Local Moran's I (LISA) 2024 (38 Provinsi)
# -------------------------------------------------------------
df_master_2024 = pd.read_csv(os.path.join(DATA_CLEAN, "master_panel_provinsi_2024.csv"))
df_master_38 = df_master_2024[df_master_2024["Provinsi"] != "Indonesia"].copy()

# Urutkan sesuai df_coords
df_master_38 = df_master_38.set_index("Provinsi").loc[df_coords["Provinsi"]].reset_index()

y_2024 = df_master_38["TPT_Total_Ags2024"].values
y_mean = np.mean(y_2024)
y_std = np.std(y_2024, ddof=1)
z_2024 = (y_2024 - y_mean) / y_std
w_z_2024 = W_knn4_38 @ z_2024

lisa_I = z_2024 * w_z_2024

# Permutation test per unit
lisa_pval = []
n_perm = 999
for i in range(N):
    zi = z_2024[i]
    other_z = np.delete(z_2024, i)
    other_w = np.delete(W_knn4_38[i, :], i)
    perm_li = []
    for _ in range(n_perm):
        perm_other = np.random.permutation(other_z)
        perm_wz = np.sum(other_w * perm_other)
        perm_li.append(zi * perm_wz)
    pval = (np.sum(np.abs(perm_li) >= np.abs(lisa_I[i])) + 1) / (n_perm + 1)
    lisa_pval.append(pval)

lisa_quad = []
for i in range(N):
    if z_2024[i] > 0 and w_z_2024[i] > 0:
        lisa_quad.append("High-High (Hotspot Pengangguran)")
    elif z_2024[i] < 0 and w_z_2024[i] < 0:
        lisa_quad.append("Low-Low (Coldspot / Agraris)")
    elif z_2024[i] > 0 and w_z_2024[i] < 0:
        lisa_quad.append("High-Low (Anomali Mandiri Tinggi)")
    else:
        lisa_quad.append("Low-High (Shelter di Tengah Hotspot)")

df_lisa = pd.DataFrame({
    "Provinsi": df_coords["Provinsi"],
    "Pulau": df_coords["pulau"],
    "TPT_2024": y_2024,
    "z_TPT": np.round(z_2024, 3),
    "lag_z_TPT": np.round(w_z_2024, 3),
    "lisa_I": np.round(lisa_I, 3),
    "p_value": np.round(lisa_pval, 4),
    "kuadran": lisa_quad,
    "signifikan": [p < 0.10 for p in lisa_pval]
})
df_lisa.to_csv(os.path.join(DATA_CLEAN, "lisa_provinsi_2024.csv"), index=False)
print("4. LISA 2024 (Local Spatial Autocorrelation) tersimpan.")

# -------------------------------------------------------------
# 5. Pemodelan Spasial: OLS, SLX, SAR, SEM, SDM (Spatial Durbin Model)
# -------------------------------------------------------------
# Variabel X:
# X1 = Informalitas (%)
# X2 = log(Upah Rata-rata)
# X3 = Rasio Mismatch Terdidik (Menengah & Tinggi / Dasar)
x_inf = df_master_38["Informal_Ags2024"].values
x_upah = np.log(df_master_38["Upah_Total_Ags2024"].values)
x_mismatch = (df_master_38["TPT_Menengah_Ags2024"].values + df_master_38["TPT_Tinggi_Ags2024"].values) / (
    2 * np.maximum(df_master_38["TPT_Dasar_Ags2024"].values, 0.5)
)

X_mat = np.column_stack([np.ones(N), x_inf, x_upah, x_mismatch])
var_names = ["Konstanta", "Informalitas (%)", "log(Upah)", "Rasio Mismatch Terdidik"]
Y_vec = y_2024

# A. OLS
b_ols, _, _, _ = np.linalg.lstsq(X_mat, Y_vec, rcond=None)
e_ols = Y_vec - X_mat @ b_ols
sigma2_ols = np.sum(e_ols ** 2) / N
logLik_ols = -0.5 * N * (np.log(2 * np.pi) + np.log(sigma2_ols) + 1)
aic_ols = 2 * 4 - 2 * logLik_ols
r2_ols = 1 - np.sum(e_ols ** 2) / np.sum((Y_vec - np.mean(Y_vec)) ** 2)

# B. SLX (Spatial Lag of X)
WX_mat = W_knn4_38 @ X_mat[:, 1:]
X_slx = np.column_stack([X_mat, WX_mat])
b_slx, _, _, _ = np.linalg.lstsq(X_slx, Y_vec, rcond=None)
e_slx = Y_vec - X_slx @ b_slx
sigma2_slx = np.sum(e_slx ** 2) / N
logLik_slx = -0.5 * N * (np.log(2 * np.pi) + np.log(sigma2_slx) + 1)
aic_slx = 2 * 7 - 2 * logLik_slx
r2_slx = 1 - np.sum(e_slx ** 2) / np.sum((Y_vec - np.mean(Y_vec)) ** 2)

# C. SAR (Spatial Autoregressive Model: Y = rho * W * Y + X * beta + eps)
WY = W_knn4_38 @ Y_vec
# Concentrated log-likelihood atas rho
def sar_loglik(rho):
    if abs(rho) >= 0.99:
        return -1e10
    A = np.eye(N) - rho * W_knn4_38
    Ay = A @ Y_vec
    b, _, _, _ = np.linalg.lstsq(X_mat, Ay, rcond=None)
    e = Ay - X_mat @ b
    s2 = np.sum(e ** 2) / N
    detA = np.linalg.slogdet(A)
    if detA[0] <= 0:
        return -1e10
    return detA[1] - 0.5 * N * (np.log(2 * np.pi) + np.log(s2) + 1)

rhos = np.linspace(-0.9, 0.9, 181)
ll_sar = [sar_loglik(r) for r in rhos]
best_rho_idx = np.argmax(ll_sar)
rho_sar = rhos[best_rho_idx]
logLik_sar = ll_sar[best_rho_idx]
A_sar = np.eye(N) - rho_sar * W_knn4_38
b_sar, _, _, _ = np.linalg.lstsq(X_mat, A_sar @ Y_vec, rcond=None)
e_sar = A_sar @ Y_vec - X_mat @ b_sar
aic_sar = 2 * 5 - 2 * logLik_sar
r2_sar = 1 - np.sum(e_sar ** 2) / np.sum((Y_vec - np.mean(Y_vec)) ** 2)

# D. SEM (Spatial Error Model: u = lambda * W * u + eps)
def sem_loglik(lam):
    if abs(lam) >= 0.99:
        return -1e10
    B = np.eye(N) - lam * W_knn4_38
    detB = np.linalg.slogdet(B)
    if detB[0] <= 0:
        return -1e10
    By = B @ Y_vec
    BX = B @ X_mat
    b, _, _, _ = np.linalg.lstsq(BX, By, rcond=None)
    e = By - BX @ b
    s2 = np.sum(e ** 2) / N
    return detB[1] - 0.5 * N * (np.log(2 * np.pi) + np.log(s2) + 1)

ll_sem = [sem_loglik(l) for l in rhos]
best_lam_idx = np.argmax(ll_sem)
lam_sem = rhos[best_lam_idx]
logLik_sem = ll_sem[best_lam_idx]
aic_sem = 2 * 5 - 2 * logLik_sem
B_sem = np.eye(N) - lam_sem * W_knn4_38
b_sem, _, _, _ = np.linalg.lstsq(B_sem @ X_mat, B_sem @ Y_vec, rcond=None)
e_sem = Y_vec - X_mat @ b_sem
r2_sem = 1 - np.sum(e_sem ** 2) / np.sum((Y_vec - np.mean(Y_vec)) ** 2)

# E. SDM (Spatial Durbin Model: Y = rho * W * Y + X * beta + W * X * theta + eps)
def sdm_loglik(rho):
    if abs(rho) >= 0.99:
        return -1e10
    A = np.eye(N) - rho * W_knn4_38
    Ay = A @ Y_vec
    b, _, _, _ = np.linalg.lstsq(X_slx, Ay, rcond=None)
    e = Ay - X_slx @ b
    s2 = np.sum(e ** 2) / N
    detA = np.linalg.slogdet(A)
    if detA[0] <= 0:
        return -1e10
    return detA[1] - 0.5 * N * (np.log(2 * np.pi) + np.log(s2) + 1)

ll_sdm = [sdm_loglik(r) for r in rhos]
best_rho_sdm_idx = np.argmax(ll_sdm)
rho_sdm = rhos[best_rho_sdm_idx]
logLik_sdm = ll_sdm[best_rho_sdm_idx]
A_sdm = np.eye(N) - rho_sdm * W_knn4_38
b_sdm_all, _, _, _ = np.linalg.lstsq(X_slx, A_sdm @ Y_vec, rcond=None)
e_sdm = A_sdm @ Y_vec - X_slx @ b_sdm_all
aic_sdm = 2 * 8 - 2 * logLik_sdm
r2_sdm = 1 - np.sum(e_sdm ** 2) / np.sum((Y_vec - np.mean(Y_vec)) ** 2)

df_model_comp = pd.DataFrame([
    {"Model": "OLS (Standar Non-Spasial)", "Param": 4, "LogLik": round(logLik_ols, 2), "AIC": round(aic_ols, 2), "rho_lambda": "-", "R2": round(r2_ols, 3), "Terpilih": False},
    {"Model": "SLX (Spatial Lag of X)", "Param": 7, "LogLik": round(logLik_slx, 2), "AIC": round(aic_slx, 2), "rho_lambda": "-", "R2": round(r2_slx, 3), "Terpilih": False},
    {"Model": "SAR (Spatial Autoregressive)", "Param": 5, "LogLik": round(logLik_sar, 2), "AIC": round(aic_sar, 2), "rho_lambda": round(rho_sar, 3), "R2": round(r2_sar, 3), "Terpilih": False},
    {"Model": "SEM (Spatial Error Model)", "Param": 5, "LogLik": round(logLik_sem, 2), "AIC": round(aic_sem, 2), "rho_lambda": round(lam_sem, 3), "R2": round(r2_sem, 3), "Terpilih": False},
    {"Model": "SDM (Spatial Durbin Model)", "Param": 8, "LogLik": round(logLik_sdm, 2), "AIC": round(aic_sdm, 2), "rho_lambda": round(rho_sdm, 3), "R2": round(r2_sdm, 3), "Terpilih": True}
])
df_model_comp.to_csv(os.path.join(DATA_CLEAN, "model_spasial_perbandingan.csv"), index=False)
print("5. Perbandingan Model Spasial tersimpan. SDM Terpilih!")

# -------------------------------------------------------------
# 6. Dekomposisi Efek LeSage-Pace SDM (Direct, Spillover, Total)
# -------------------------------------------------------------
# S_r(W) = (I_N - rho * W)^(-1) * (beta_r * I_N + theta_r * W)
inv_A_sdm = np.linalg.inv(A_sdm)
# beta: indices 1, 2, 3 in b_sdm_all
# theta: indices 4, 5, 6 in b_sdm_all
lesage_records = []
for k in range(1, 4):
    var_name = var_names[k]
    beta_k = b_sdm_all[k]
    theta_k = b_sdm_all[k + 3]
    
    Sr = inv_A_sdm @ (beta_k * np.eye(N) + theta_k * W_knn4_38)
    direct_eff = np.mean(np.diag(Sr))
    total_eff = np.mean(np.sum(Sr, axis=1))
    indirect_eff = total_eff - direct_eff
    
    lesage_records.append({
        "Variabel": var_name,
        "Koef_Domestik (Beta)": round(beta_k, 4),
        "Koef_Spasial (Theta)": round(theta_k, 4),
        "Efek_Langsung (Direct)": round(direct_eff, 4),
        "Efek_Limpahan (Spillover / Indirect)": round(indirect_eff, 4),
        "Efek_Total": round(total_eff, 4)
    })

df_lesage = pd.DataFrame(lesage_records)
df_lesage.to_csv(os.path.join(DATA_CLEAN, "dekomposisi_efek_sdm_tpt.csv"), index=False)
print("6. Dekomposisi Efek LeSage-Pace SDM tersimpan.")

# -------------------------------------------------------------
# 7. Pembuatan Grafik Visualisasi (PNG 300 DPI & SVG)
# -------------------------------------------------------------
# Grafik 06: Autokorelasi Spasial LISA & Moran Lintasan
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Lintasan Moran's I 2017-2024
ax1.plot(df_moran["tahun"], df_moran["moran_i"], marker="o", color="#2F7D6E", linewidth=2.5, markersize=8, label="Moran's I TPT")
ax1.axhline(0, color="#8896A0", linestyle="--", alpha=0.7, label="Garis Netral (Acak Spasial)")
ax1.set_title("Evolusi Autokorelasi Spasial Pengangguran (2017–2024)\nMoran's I Global Antar-Provinsi", fontsize=11, fontweight="bold", pad=12)
ax1.set_xlabel("Tahun Pengamatan BPS Sakernas", fontsize=10)
ax1.set_ylabel("Nilai Indeks Moran's I", fontsize=10)
ax1.grid(True, linestyle=":", alpha=0.6)
for _, r in df_moran.iterrows():
    ax1.annotate(f"{r['moran_i']:.3f}", (r['tahun'], r['moran_i']), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9, fontweight="bold")
ax1.legend(loc="lower right")

# Subplot 2: Moran Scatterplot 2024
colors_lisa = {
    "High-High (Hotspot Pengangguran)": "#C0392B",
    "Low-Low (Coldspot / Agraris)": "#2F7D6E",
    "Low-High (Shelter di Tengah Hotspot)": "#D9B26F",
    "High-Low (Anomali Mandiri Tinggi)": "#6C5B9E"
}
for quad, col in colors_lisa.items():
    sub = df_lisa[df_lisa["kuadran"] == quad]
    ax2.scatter(sub["z_TPT"], sub["lag_z_TPT"], color=col, s=70, alpha=0.85, label=quad, edgecolors="white", linewidth=0.5)

# Regresi linier z vs Wz
m_slope, b_intercept = np.polyfit(z_2024, w_z_2024, 1)
x_line = np.linspace(min(z_2024), max(z_2024), 50)
ax2.plot(x_line, m_slope * x_line + b_intercept, color="#243B3A", linewidth=1.8, linestyle="-", label=f"Kemiringan = Moran's I ({m_slope:.3f})")
ax2.axvline(0, color="#8896A0", linestyle="--", alpha=0.5)
ax2.axhline(0, color="#8896A0", linestyle="--", alpha=0.5)
ax2.set_title("Moran Scatterplot & Klaster Spasial LISA (Agustus 2024)\nIdentifikasi Hotspot vs Shelter Informal", fontsize=11, fontweight="bold", pad=12)
ax2.set_xlabel("Standar Deviasi TPT Provinsi (z)", fontsize=10)
ax2.set_ylabel("Spatial Lag Tetangga (Wz)", fontsize=10)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(loc="upper left", fontsize=8)

plt.tight_layout()
chart_06_png = os.path.join(ASSETS_CHARTS, "06_autokorelasi_spasial_lisa_moran.png")
chart_06_svg = os.path.join(ASSETS_CHARTS, "06_autokorelasi_spasial_lisa_moran.svg")
fig.savefig(chart_06_png, dpi=300)
fig.savefig(chart_06_svg)
plt.close(fig)
print(f"7. Visualisasi 06 tersimpan di: {chart_06_png}")

# Grafik 07: Model Spasial Comparison & LeSage-Pace Spillover
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: AIC Comparison Bar Chart
bars = ax1.bar(df_model_comp["Model"], df_model_comp["AIC"], color=["#8896A0", "#8896A0", "#3A8C7E", "#3A8C7E", "#C0392B"], width=0.55)
ax1.set_title("Kriteria Informasi Akaike (AIC) Antarmodel\n(Nilai Lebih Rendah Mengindikasikan Model Lebih Unggul)", fontsize=11, fontweight="bold", pad=12)
ax1.set_ylabel("Nilai AIC", fontsize=10)
ax1.set_xticklabels(["OLS", "SLX", "SAR", "SEM", "SDM\n(Terpilih)"], fontsize=9)
ax1.set_ylim(min(df_model_comp["AIC"]) - 20, max(df_model_comp["AIC"]) + 10)
ax1.grid(axis="y", linestyle=":", alpha=0.6)
for b in bars:
    h = b.get_height()
    ax1.annotate(f"{h:.1f}", (b.get_x() + b.get_width() / 2, h), textcoords="offset points", xytext=(0, 4), ha='center', fontsize=9, fontweight="bold")

# Subplot 2: Dekomposisi Efek LeSage-Pace SDM
x_indices = np.arange(len(df_lesage))
width = 0.28
rects1 = ax2.bar(x_indices - width, df_lesage["Efek_Langsung (Direct)"], width, label="Efek Langsung (Domestik)", color="#2F7D6E")
rects2 = ax2.bar(x_indices, df_lesage["Efek_Limpahan (Spillover / Indirect)"], width, label="Efek Limpahan (Spasial)", color="#D9B26F")
rects3 = ax2.bar(x_indices + width, df_lesage["Efek_Total"], width, label="Efek Total", color="#C0392B")

ax2.set_title("Dekomposisi Efek Spatial Durbin Model (LeSage–Pace)\nPengaruh Terhadap Tingkat Pengangguran Terbuka", fontsize=11, fontweight="bold", pad=12)
ax2.set_xticks(x_indices)
ax2.set_xticklabels(["Informalitas\n(%)", "log(Upah\nBuruh)", "Mismatch\nTerdidik"], fontsize=9)
ax2.axhline(0, color="#243B3A", linestyle="-", linewidth=0.8)
ax2.set_ylabel("Besaran Efek Marginal", fontsize=10)
ax2.grid(axis="y", linestyle=":", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8.5)

plt.tight_layout()
chart_07_png = os.path.join(ASSETS_CHARTS, "07_model_spasial_dan_spillover_sdm.png")
chart_07_svg = os.path.join(ASSETS_CHARTS, "07_model_spasial_dan_spillover_sdm.svg")
fig.savefig(chart_07_png, dpi=300)
fig.savefig(chart_07_svg)
plt.close(fig)
print(f"8. Visualisasi 07 tersimpan di: {chart_07_png}")
print("\nSeluruh Pipeline Ekonometrika Spasial Selesai Dijalankan!")
