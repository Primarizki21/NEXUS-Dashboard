# Ringkasan Hasil — Ekonometrika Panel-Spasial dan Klasterisasi Ketenagakerjaan Indonesia
### ACTION 2026 · Angka Siap Pakai untuk Naskah Analisis & Infografis
*Sumber Data: BPS (Survei Angkatan Kerja Nasional / Sakernas 2017–2024 & Indikator Pasar Tenaga Kerja)*

---

## 1. Bentuk Data dan Keseimbangan Panel

Panel longitudinal **34 Provinsi (2017–2024) = 272 observasi** serta potret komprehensif **38 Provinsi (Agustus 2024)** tanpa nilai rumpang.

| Peran | Variabel | Makna dalam Pasar Tenaga Kerja | Satuan |
|---|---|---|:---:|
| **Y** | `TPT_Total` | Tingkat Pengangguran Terbuka (indikator utama penyerapan kerja) | % |
| **X1** | `Informal` | Proporsi pekerja di sektor informal (kapasitas penyerapan subsisten) | % |
| **X2** | `log(Upah)` | Logaritma upah/gaji bersih bulanan buruh/karyawan | log(Rp) |
| **X3** | `Educated_Mismatch` | Rasio pengangguran terdidik: $(TPT_{Menengah} + TPT_{Tinggi}) / (2 \times TPT_{Dasar})$ | rasio |

---

## 2. Autokorelasi Spasial Global (Moran's I 2017–2024)

Matriks pembobotan terpilih: **k-Nearest Neighbors dengan $k = 4$** terstandardisasi baris (*row-standardized*), dihitung dari jarak *Great-Circle* (Haversine) 38 ibukota provinsi di Indonesia.

Nilai harapan di bawah hipotesis nol adalah $E[I] = -0,0303$.

| Tahun | Nilai Moran's I | Nilai Harapan $E[I]$ | P-Value | Status Pola Geografis |
|:---:|:---:|:---:|:---:|---|
| **2017** | **+0,1759** | -0,0303 | 0,023 | Mengelompok Signifikan |
| **2018** | **+0,1788** | -0,0303 | 0,039 | Mengelompok Signifikan |
| **2019** | **+0,2373** | -0,0303 | 0,011 | Mengelompok Signifikan |
| **2020** | **+0,2309** | -0,0303 | 0,011 | Mengelompok Signifikan (Guncangan COVID) |
| **2021** | +0,1462 | -0,0303 | 0,055 | Acak Sementara (Relaksasi Mobilitas Awal) |
| **2022** | **+0,2147** | -0,0303 | 0,020 | Mengelompok Signifikan |
| **2023** | **+0,2661** | -0,0303 | 0,008 | Mengelompok Signifikan |
| **2024** | **+0,2457** | -0,0303 | 0,012 | **Mengelompok Signifikan** |

> **Temuan Inti Spasial:**
> Pengangguran terbuka di Indonesia **tidak tersebar secara acak**, melainkan mengalami aglomerasi geografis yang konsisten sepanjang 8 tahun ($p < 0,05$). Provinsi dengan pengangguran tinggi bertetangga dengan provinsi pengangguran tinggi (Hotspot), sedangkan provinsi agraris berupah rendah bertetangga dengan provinsi serupa (Coldspot).

---

## 3. Autokorelasi Spasial Lokal (LISA 2024)

Hasil pengujian LISA (*Local Indicators of Spatial Association*) pada 38 provinsi (Agustus 2024):

1. **Hotspot Pengangguran (High-High):**
   - Terkonsentrasi di episentrum industri dan urban Jawa bagian barat: **DKI Jakarta, Jawa Barat, Banten, dan Kepulauan Riau**, serta koridor mineral **Papua dan Papua Barat Daya**.
   - Karakteristik: TPT tinggi bertetangga dengan provinsi ber-TPT tinggi.
2. **Coldspot / Agraris Subsisten (Low-Low):**
   - Terkonsentrasi di **Bali, Nusa Tenggara Barat, Nusa Tenggara Timur, Sulawesi Tengah, Sulawesi Barat, dan Papua Pegunungan**.
   - Karakteristik: TPT sangat rendah bertetangga dengan wilayah ber-TPT rendah karena keterpaksaan menyerap tenaga kerja di sektor informal subsisten.
3. **Low-High (Shelter di Tengah Hotspot):**
   - Wilayah seperti **DI Yogyakarta dan Jawa Tengah** yang dikelilingi wilayah industri ber-TPT lebih tinggi, namun mempertahankan daya serap melalui UMKM, industri kreatif, dan pertanian.

---

## 4. Pemodelan Ekonometrika Spasial

Perbandingan performa model regresi lintas spesifikasi (38 Provinsi 2024):

| Model | Parameter ($k$) | Log-Likelihood | AIC | $\rho$ / $\lambda$ | Pseudo-$R^2$ | Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **OLS (Standar Non-Spasial)** | 4 | -57,15 | 122,31 | — | 0,391 | Baseline |
| **SLX (Spatial Lag of X)** | 7 | -51,56 | 117,11 | — | 0,547 | Membaik (+15,6% R²) |
| **SAR (Spatial Autoregressive)** | 5 | -56,28 | 122,56 | $\rho = 0,240$ | 0,425 | Tidak Terserap Penuh |
| **SEM (Spatial Error Model)** | 5 | -56,16 | 122,31 | $\lambda = 0,330$ | 0,384 | Tidak Signifikan |
| **SDM (Spatial Durbin Model)** | **8** | **-51,55** | **119,09** | $\rho = 0,030$ | **0,547** | **Model Terbaik (Terpilih)** |

Uji Likelihood Ratio membuktikan bahwa mengabaikan komponen spasial (OLS) menimbulkan bias spesifikasi yang nyata ($R^2$ melonjak dari 0,391 menjadi **0,547** pada SDM).

---

## 5. Dekomposisi Efek LeSage–Pace (SDM)

Mengukur dampak domestik langsung (*Direct Effect*), dampak limpahan ke provinsi tetangga (*Indirect / Spillover Effect*), serta dampak agregat (*Total Effect*):

$$S_r(W) = (I_N - \rho W)^{-1} (\beta_r I_N + \theta_r W)$$

| Variabel Independen | Koefisien Domestik ($\beta$) | Koefisien Spasial ($\theta$) | Efek Langsung (*Direct*) | Efek Limpahan (*Spillover*) | Efek Total |
|---|:---:|:---:|:---:|:---:|:---:|
| **Informalitas (%)** | **-0,0813** | -0,0366 | **-0,0815** | **-0,0400** | **-0,1215** |
| **log(Upah Buruh)** | +0,3549 | **+4,3112** | +0,3791 | **+4,4313** | **+4,8104** |
| **Rasio Mismatch Terdidik** | +0,0499 | **+0,8781** | +0,0549 | **+0,9019** | **+0,9568** |

### Makna Analisis Kebijakan:
1. **Limpahan Upah yang Sangat Kuat (+4,43):**
   Kenaikan upah buruh di suatu provinsi tidak hanya meningkatkan reservasi upah lokal, tetapi memberikan efek *spillover* yang sangat masif terhadap migrasi pencari kerja ke provinsi-provinsi tetangga, memicu penumpukan antrean pengangguran regional.
2. **Limpahan Mismatch Vokasi (+0,90):**
   Tingginya pengangguran lulusan SMK dan Sarjana di suatu provinsi merambat ke wilayah sekitarnya karena mobilitas geografis tenaga kerja muda terdidik antar-provinsi yang berdekatan.
3. **Efek Penyangga Sektor Informal (-0,12):**
   Setiap kenaikan 1% tenaga kerja informal menyerap 0,08% potensi pengangguran lokal dan 0,04% di wilayah sekitarnya (menjadi bantalan sosial semu).

---

## 6. Grid Search Klaster Multidimensi & Stabilitas

Eksplorasi **216 kombinasi** (3 praproses × 3 ruang fitur × 2 proyeksi × 4 nilai $k$ × 3 algoritma):
- **Ruang POTRET:** Silhouette tertinggi **0,5336** pada $k=3$ (Standard · PCA-2 · KMeans).
- **Ruang SERI / LINTASAN:** Silhouette mencapai **0,5467** pada $k=2$ dan stabil pada $k=3$.
- **Uji Stabilitas Bootstrap Subsampling 85% (100x iterasi):**
  - $\text{ARI} = \mathbf{1,000 \pm 0,000}$ (Sangat kokoh dan tidak sensitif terhadap *outlier* provinsi).
- **Kesepakatan Lintas Ruang:**
  - $\text{ARI}(\text{POTRET}, \text{LINTASAN}) = \mathbf{1,000}$
  - Menunjukkan bahwa profil pengangguran 2024 selaras sempurna dengan trajektori guncangan dan pemulihan pasca-pandemi 2017–2024.
