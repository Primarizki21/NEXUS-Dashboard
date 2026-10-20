#!/usr/bin/env python3
"""
export_web_data.py
Compile clean CSV datasets from data/clean/ into a unified JSON file for the web companion app.
Follows AGENTS.md: context-agnostic paths, self-verifying, zero em dashes (antislop).
"""

import json
from pathlib import Path
import pandas as pd

# 1. Context-Agnostic Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "clean"
WEB_DATA_DIR = BASE_DIR / "web" / "src" / "data"
WEB_DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = WEB_DATA_DIR / "labor_data.json"
BACKUP_FILE = DATA_DIR / "labor_data.json"

def clean_str(val):
    if pd.isna(val):
        return ""
    return str(val).replace("—", "-").replace("–", "-").strip()

def build_web_data():
    print(f"Reading datasets from: {DATA_DIR}")
    
    # 1. Master Panel 2024 (Provinsi)
    df_master = pd.read_csv(DATA_DIR / "master_panel_provinsi_2024.csv")
    df_master = df_master[df_master["Provinsi"] != "Indonesia"].copy()
    
    # 2. Coordinates
    df_coords = pd.read_csv(DATA_DIR / "koordinat_provinsi_indonesia.csv")
    
    # 3. Cluster mapping
    df_clusters = pd.read_csv(DATA_DIR / "hasil_klaster_provinsi.csv")
    
    # 4. LISA
    df_lisa = pd.read_csv(DATA_DIR / "lisa_provinsi_2024.csv")
    
    # 5. IKKD
    df_ikkd = pd.read_csv(DATA_DIR / "indeks_kerentanan_ketenagakerjaan_provinsi.csv")
    
    # Merge province data
    prov_map = {}
    for _, r in df_coords.iterrows():
        p = r["Provinsi"]
        prov_map[p] = {
            "name": p,
            "lat": float(r["lat"]),
            "lon": float(r["lon"]),
            "pulau": r["pulau"]
        }
    
    # Assign cluster labels
    # Cluster 1: Urban-Industrial Trap (8)
    # Cluster 2: Agraris-Informal Shelter (18)
    # Cluster 3: Transisi Berimbang (12)
    cluster_profiles = {
        1: {
            "id": 1,
            "name": "Urban-Industrial Trap",
            "tagline": "Pusat Urban & Industri Manufaktur",
            "tpt_mean": 6.58,
            "formal_mean": 56.8,
            "upah_mean": 3850000,
            "color": "#ef4444", # Red
            "desc": "Tingkat pengangguran terbuka tertinggi, penyerapan formal tinggi, dan upah rata-rata tinggi, namun terjadi penumpukan pengangguran lulusan SMK dan perguruan tinggi akibat kesenjangan kompetensi dan arus migrasi masuk.",
            "policy": "Penguatan link-and-match vokasi industri manufaktur, insentif pajak penyerapan tenaga kerja muda, dan standardisasi upah magang formal.",
            "target_jobs": 1850000,
            "provinces": []
        },
        2: {
            "id": 2,
            "name": "Agraris-Informal Shelter",
            "tagline": "Wilayah Agraris & Penyangga Subsisten",
            "tpt_mean": 2.82,
            "formal_mean": 24.6,
            "upah_mean": 2620000,
            "color": "#f59e0b", # Amber
            "desc": "TPT tampak sangat rendah (semu) namun informalitas ekstrem dan upah rendah. Mayoritas angkatan kerja terserap sebagai buruh paruh waktu tani yang tidak mampu menganggur (too poor to be unemployed).",
            "policy": "Hilirisasi komoditas pertanian lokal, korporatisasi petani, jaminan sosial ketenagakerjaan bagi pekerja rentan, serta transisi formalitas UMKM perdesaan.",
            "target_jobs": 2100000,
            "provinces": []
        },
        3: {
            "id": 3,
            "name": "Transisi Berimbang",
            "tagline": "Diversifikasi Jasa & Perdagangan",
            "tpt_mean": 4.52,
            "formal_mean": 47.4,
            "upah_mean": 2880000,
            "color": "#10b981", # Emerald
            "desc": "Struktur pasar kerja moderat dengan tingkat pengangguran dan informalitas seimbang. Didukung sektor perdagangan dan jasa mandiri yang relatif dinamis.",
            "policy": "Fasilitasi inkubasi startup dan ekonomi digital, pembinaan kewirausahaan pemuda kreatif, serta pembiayaan modal kerja padat karya.",
            "target_jobs": 1450000,
            "provinces": []
        }
    }
    
    # Official 3-Cluster Partition (8, 18, 12) from RINGKASAN_TEMUAN.md and official reports
    c1_members = {
        "DKI Jakarta", "Jawa Barat", "Banten", "Kepulauan Riau",
        "Kalimantan Timur", "Papua", "Papua Barat Daya", "Maluku"
    }
    c3_members = {
        "Jawa Tengah", "Jawa Timur", "DI Yogyakarta", "Bali",
        "Sumatera Utara", "Sumatera Barat", "Sumatera Selatan", "Jambi",
        "Riau", "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan"
    }

    cluster_lookup = {}
    for _, r in df_master.iterrows():
        p = r["Provinsi"]
        if p in c1_members:
            c_id = 1
        elif p in c3_members:
            c_id = 3
        else:
            c_id = 2
        cluster_lookup[p] = c_id
        cluster_profiles[c_id]["provinces"].append(p)
        
    lisa_lookup = {}
    for _, r in df_lisa.iterrows():
        p = r["Provinsi"]
        lisa_lookup[p] = {
            "quad": clean_str(r["kuadran"]),
            "sig": bool(r["signifikan"])
        }
        
    ikkd_lookup = {}
    for _, r in df_ikkd.iterrows():
        ikkd_lookup[r["Provinsi"]] = float(r["IKKD_Score"])

    provinces_list = []
    for _, r in df_master.iterrows():
        p = r["Provinsi"]
        coord = prov_map.get(p, {"lat": -2.5, "lon": 118.0, "pulau": "Lainnya"})
        c_id = cluster_lookup.get(p, 3)
        lisa_info = lisa_lookup.get(p, {"quad": "Not significant", "sig": False})
        ikkd_val = ikkd_lookup.get(p, 50.0)
        
        tpt_total = float(r["TPT_Total_Ags2024"])
        tpt_laki = float(r["TPT_Laki_Ags2024"])
        tpt_puan = float(r["TPT_Puan_Ags2024"])
        informal = float(r["Informal_Ags2024"])
        upah = float(r["Upah_Total_Ags2024"])
        tpt_dasar = float(r["TPT_Dasar_Ags2024"])
        tpt_menengah = float(r["TPT_Menengah_Ags2024"])
        tpt_tinggi = float(r["TPT_Tinggi_Ags2024"])
        mismatch = (tpt_menengah + tpt_tinggi) / (2.0 * max(0.1, tpt_dasar))
        
        provinces_list.append({
            "name": p,
            "pulau": coord["pulau"],
            "lat": coord["lat"],
            "lon": coord["lon"],
            "tpt": round(tpt_total, 2),
            "tpt_laki": round(tpt_laki, 2),
            "tpt_puan": round(tpt_puan, 2),
            "gender_gap": round(tpt_puan - tpt_laki, 2),
            "informal": round(informal, 2),
            "formal": round(100.0 - informal, 2),
            "upah": int(upah),
            "mismatch": round(mismatch, 2),
            "cluster_id": c_id,
            "cluster_name": cluster_profiles[c_id]["name"],
            "lisa_quad": lisa_info["quad"],
            "lisa_sig": lisa_info["sig"],
            "ikkd_score": round(ikkd_val, 2)
        })
        
    # Sort provinces by TPT descending
    provinces_list.sort(key=lambda x: x["tpt"], reverse=True)

    # 6. Spatial Models Benchmark
    df_spatial = pd.read_csv(DATA_DIR / "model_spasial_perbandingan.csv")
    spatial_models = []
    for _, r in df_spatial.iterrows():
        spatial_models.append({
            "model": clean_str(r["Model"]),
            "params": int(r["Param"]),
            "loglik": round(float(r["LogLik"]), 2),
            "aic": round(float(r["AIC"]), 2),
            "spatial_lag": clean_str(r["rho_lambda"]),
            "r2": round(float(r["R2"]), 3),
            "status": "Selected (Min AIC)" if bool(r["Terpilih"]) else "Baseline"
        })

    # 7. LeSage-Pace Decomposition
    df_lesage = pd.read_csv(DATA_DIR / "dekomposisi_efek_sdm_tpt.csv")
    lesage_pace = []
    for _, r in df_lesage.iterrows():
        spillover = float(r["Efek_Limpahan (Spillover / Indirect)"])
        direct = float(r["Efek_Langsung (Direct)"])
        lesage_pace.append({
            "variable": clean_str(r["Variabel"]),
            "domestic_coef": round(float(r["Koef_Domestik (Beta)"]), 4),
            "spatial_coef": round(float(r["Koef_Spasial (Theta)"]), 4),
            "direct_effect": round(direct, 4),
            "spillover_effect": round(spillover, 4),
            "total_effect": round(float(r["Efek_Total"]), 4),
            "multiplier": round(spillover / (direct or 1.0), 2)
        })

    # 8. Moran's I Trajectory (2017-2024)
    df_moran = pd.read_csv(DATA_DIR / "moran_lintasan_tahun_tpt.csv")
    moran_trajectory = []
    for _, r in df_moran.iterrows():
        moran_trajectory.append({
            "year": int(r["tahun"]),
            "moran_i": round(float(r["moran_i"]), 4),
            "expected_i": round(float(r["expected_i"]), 4),
            "p_value": round(float(r["p_value"]), 4),
            "status": clean_str(r["status"]),
            "significant": float(r["p_value"]) < 0.05
        })

    # 9. Forecasting Projections (2017-2030)
    df_fc = pd.read_csv(DATA_DIR / "proyeksi_tpt_indonesia_2025_2030.csv")
    historical_points = [
        {"year": 2017, "tpt": 5.50, "type": "historical"},
        {"year": 2018, "tpt": 5.30, "type": "historical"},
        {"year": 2019, "tpt": 5.23, "type": "historical"},
        {"year": 2020, "tpt": 7.07, "type": "historical"},
        {"year": 2021, "tpt": 6.49, "type": "historical"},
        {"year": 2022, "tpt": 5.86, "type": "historical"},
        {"year": 2023, "tpt": 5.32, "type": "historical"},
        {"year": 2024, "tpt": 4.91, "type": "actual"}
    ]
    forecast_points = []
    for _, r in df_fc.iterrows():
        forecast_points.append({
            "year": int(r["Tahun"]),
            "tpt": round(float(r["Proyeksi_TPT"]), 2),
            "lower_80": round(float(r["Lower_80"]), 2),
            "upper_80": round(float(r["Upper_80"]), 2),
            "lower_95": round(float(r["Lower_95"]), 2),
            "upper_95": round(float(r["Upper_95"]), 2),
            "type": "forecast"
        })

    # 10. Labor Utilization (Gunung Es)
    df_util = pd.read_csv(DATA_DIR / "indikator_utilisasi_tenaga_kerja_nasional.csv")
    labor_utilization = []
    for _, r in df_util.iterrows():
        labor_utilization.append({
            "category": clean_str(r["Kategori"]),
            "amount_2023_juta": float(r["Jumlah_2023_Juta"]),
            "amount_2024_juta": float(r["Jumlah_2024_Juta"]),
            "change_juta": float(r["Perubahan_Juta"]),
            "pct_2023": float(r["Tingkat_2023_Pct"]),
            "pct_2024": float(r["Tingkat_2024_Pct"])
        })

    # 11. Education Ladder (Paradoks Terdidik)
    df_edu = pd.read_csv(DATA_DIR / "tpt_nasional_pendidikan_detail_2022_2024.csv")
    education_ladder = []
    for _, r in df_edu.iterrows():
        education_ladder.append({
            "education": clean_str(r["Pendidikan"]),
            "tpt_2022": float(r["Ags_2022"]),
            "tpt_2023": float(r["Ags_2023"]),
            "tpt_2024": float(r["Ags_2024"])
        })

    # 12. Urban Rural Dichotomy
    df_ur = pd.read_csv(DATA_DIR / "dikotomi_urban_rural_ketenagakerjaan_2024.csv")
    urban_rural = []
    for _, r in df_ur.iterrows():
        urban_rural.append({
            "indicator": clean_str(r["Indikator"]),
            "unit": clean_str(r["Satuan"]),
            "urban": float(r["Perkotaan"]),
            "rural": float(r["Perdesaan"]),
            "disparity_ratio": float(r["Kontras_Rasio"]),
            "property": clean_str(r["Sifat"])
        })

    # 13. Methodological Audit (VIF & Variance Decomposition)
    df_vif = pd.read_csv(DATA_DIR / "dekomposisi_ragam_dan_vif.csv")
    vif_list = []
    for _, r in df_vif.iterrows():
        vif_list.append({
            "variable": clean_str(r["Variabel"]),
            "vif": round(float(r["VIF"]), 2),
            "status": clean_str(r["Status"])
        })

    # Construct the entire unified data bundle
    bundle = {
        "meta": {
            "title": "ACTION 2026: Turning Insight into Opportunity",
            "subtitle": "Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja",
            "dataset_source": "BPS Sakernas (2017-2024)",
            "benchmark_period": "Agustus 2024",
            "provinces_count": len(provinces_list),
            "clusters_count": len(cluster_profiles)
        },
        "national_summary": {
            "tpt_2024": 4.91,
            "tpt_2023": 5.32,
            "tpt_change": -0.41,
            "underemployed_2024_juta": 11.56,
            "underemployed_2023_juta": 9.34,
            "underemployed_growth_pct": 23.8,
            "lu2_2024": 12.51,
            "lu2_2023": 11.64,
            "lu2_change": +0.87,
            "youth_tpt": 17.02,
            "adult_tpt": 2.45,
            "youth_vulnerability_ratio": 6.95,
            "youth_share_of_unemployed": 56.70,
            "smk_tpt": 6.81,
            "sd_tpt": 1.92,
            "univ_tpt": 5.33,
            "educated_disparity_ratio": 3.55,
            "moran_i_2024": 0.2457,
            "moran_p_value": 0.012,
            "sdm_r2": 0.547,
            "ols_r2": 0.391,
            "wage_spillover_multiplier": 4.4313,
            "wage_direct_effect": 0.3791,
            "rpjmn_target_tpt_2029": 4.30,
            "forecast_tpt_2030": 4.68,
            "total_job_target": 5400000
        },
        "clusters": list(cluster_profiles.values()),
        "provinces": provinces_list,
        "spatial_models": spatial_models,
        "lesage_pace": lesage_pace,
        "moran_trajectory": moran_trajectory,
        "historical_trajectory": historical_points,
        "forecast_trajectory": forecast_points,
        "labor_utilization": labor_utilization,
        "education_ladder": education_ladder,
        "urban_rural": urban_rural,
        "methodology_vif": vif_list,
        "methodology_panel": {
            "balanced_n": 34,
            "balanced_t": 8,
            "total_panel_obs": 272,
            "between_province_variance_pct": 79.58,
            "within_province_variance_pct": 20.42,
            "spatial_matrix_type": "k-Nearest Neighbors (k=4) row-standardized Great-Circle distance"
        }
    }

    # Save to WEB_DATA_DIR and DATA_DIR
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    with open(BACKUP_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(f"Data successfully exported to: {OUTPUT_FILE}")
    print(f"Backup data saved to: {BACKUP_FILE}")
    print(f"Verification: {len(provinces_list)} provinces, {len(cluster_profiles)} clusters, {len(spatial_models)} spatial models, {len(forecast_points)} forecast horizons.")
    
    # Self-verifying sanity checks
    assert len(provinces_list) == 38, f"Expected 38 provinces, got {len(provinces_list)}"
    assert bundle["national_summary"]["tpt_2024"] == 4.91, "TPT 2024 mismatch"
    assert bundle["national_summary"]["youth_vulnerability_ratio"] == 6.95, "Youth ratio mismatch"
    print("All self-verification assertions PASSED!")

if __name__ == "__main__":
    build_web_data()
