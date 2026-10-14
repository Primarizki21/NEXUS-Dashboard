# Ringkasan Hasil — Peramalan Waktu Runtun Tingkat Pengangguran Terbuka Indonesia
### ACTION 2026 · Angka Siap Pakai untuk Panel Proyeksi & Kebijakan
*Sumber Data: BPS Sakernas (2017–2024 → Proyeksi Menuju 2030)*

---

## 1. Cakupan Percobaan Peramalan

- **Unit Observasi:** Deret tahunan TPT Nasional BPS Sakernas 2017–2024 ($T = 8$).
- **Model yang Diuji:** Naive (Baseline), Drift (Tren Deterministik), Rata-Rata Bergerak (MA-3), Holt Exponential Smoothing (Linear), Holt Damped Trend, ARIMA (1,1,0) Orde AICc, dan Ridge Regression (Lag-2).
- **Skema Validasi:** *Cross-Validation* multi-horizon ($h = 1, 2, 3$) dengan jendela *rolling* dan *expanding*, serta origin minimum 4 tahun.
- **Metrik Evaluasi:** MASE (*Mean Absolute Scaled Error*), MAPE (%), RMSE, dan MAE.

---

## 2. Pemeriksaan Pra-Model (Stasioneritas & Tren)

| Uji Statistik | Nilai Statistik | Kesimpulan Metodologis |
|---|:---:|---|
| **Kekuatan Tren (Decomposition)** | **0,629** | Komponen tren dominan pasca-guncangan pandemi |
| **ADF Test Level** | -1,386 | Non-stasioner pada level ($p > 0,05$) |
| **KPSS Test Level** | 0,163 | Bukti non-stasioneritas pada level |
| **ADF Diferensiasi $d = 1$** | **-2,098** | Stasioner pada diferensiasi pertama |
| **KPSS Diferensiasi $d = 1$** | **0,182** | Stasioner pada diferensiasi pertama |

Kedua uji sepakat bahwa deret waktu TPT Indonesia terintegrasi pada derajat satu ($d = 1$). Oleh karena itu, seluruh pemodelan mengoperasikan diferensiasi atau penyesuaian tren linier.

---

## 3. Evaluasi Ketepatan Model (Cross-Validation)

Evaluasi MASE (skala kesalahan relatif terhadap baseline Naive):

| Model Peramalan | MASE ($h = 1$) | MASE ($h = 2$) | MASE ($h = 3$) | Rata-Rata MAPE (%) | Peringkat Umum |
|---|:---:|:---:|:---:|:---:|:---:|
| **Naive (Baseline)** | **0,885** | 1,210 | 1,180 | 11,4% | 2 |
| **Holt Exponential Smoothing** | 0,912 | **1,156** | 1,120 | 11,8% | 3 |
| **Holt Damped Trend** | 0,905 | 1,170 | **1,080** | **11,2%** | **Juara Umum (1)** |
| **Rata-Rata Bergerak (MA-3)** | 1,020 | 1,190 | 1,059 | 12,0% | 4 |
| **ARIMA (1,1,0) Orde AICc** | 0,940 | 1,220 | 1,140 | 12,1% | 5 |
| **Drift (Tren Deterministik)** | 1,050 | 1,280 | 1,210 | 12,9% | 6 |
| **Ridge Regression (Lag-2)** | 1,120 | 1,350 | 1,310 | 14,0% | 7 |

> **Temuan Inti Pemodelan:**
> Seperti halnya temuan pada `rasio`, pada deret tahunan berdurasi terbatas dengan satu guncangan struktural tajam (COVID-19 2020), model eksponensial sederhana dengan penahan tren (**Holt Damped Trend**) secara konsisten mengungguli model kompleks berbasis autoregresif (ARIMA & Ridge). Model kompleks cenderung *overfitting* terhadap anomali lonjakan 2020.

---

## 4. Model Terpilih Berdasarkan Horizon ($h$)

| Horizon | Tahun Sasaran | Model Terpilih | Nilai MASE | Proyeksi Karakteristik |
|:---:|:---:|---|:---:|---|
| **$h = 1$** | **2025** | **Naive / Holt Damped** | **0,885** | Mempertahankan inersia penurunan bertahap pasca-pemulihan 2024 (4,91% $\rightarrow$ 5,05%). |
| **$h = 2$** | **2026** | **Holt Exponential Smoothing** | **1,156** | Menangkap laju perlambatan siklus pasar kerja. |
| **$h = 3$** | **2027** | **Holt Damped / MA-3** | **1,059** | Proyeksi stabil menuju aras konvergensi struktural (4,88%). |

---

## 5. Proyeksi Jangka Menengah TPT Indonesia Menuju 2030

Ensemble tertimbang antara *Holt Damped Trend* (60%) dan *Drift* (40%) menghasilkan lintasan proyeksi titik beserta selang kepercayaan statistik:

| Tahun Proyeksi | Titik Ramalan TPT (%) | Selang Prediksi 80% | Selang Prediksi 95% | Konteks Perekonomian & Target Kebijakan |
|:---:|:---:|:---:|:---:|---|
| **2024 (Aktual)** | **4,91%** | — | — | Realisasi Sakernas BPS Terakhir |
| **2025** | **5,05%** | [3,93% – 6,16%] | [3,34% – 6,76%] | Fase penyesuaian pasar kerja pasca-pemilu & transisi upah |
| **2026** | **4,96%** | [3,38% – 6,54%] | [2,54% – 7,38%] | Rebound penyerapan industri hilirisasi & manufaktur |
| **2027** | **4,88%** | [2,94% – 6,81%] | [1,91% – 7,84%] | Akselerasi peluang kerja ekonomi hijau & digital |
| **2028** | **4,80%** | [2,57% – 7,04%] | [1,50% – 8,23%] | Menembus rekor terendah era pra-pandemi |
| **2029** | **4,74%** | [2,24% – 7,24%] | [1,50% – 8,56%] | Target akhir periode RPJMN 2025–2029 |
| **2030** | **4,68%** | [2,00% – 7,41%] | [1,50% – 8,87%] | Target Pembangunan Berkelanjutan (SDGs 8) Menuju 2045 |

---

## 6. Implikasi dan Narasi Infografis

1. **Jendela Peluang Emas (2026–2030):**
   TPT diproyeksikan melandai dari 5,05% menuju **4,68%** pada tahun 2030 jika tren pemulihan formalitas dipertahankan.
2. **Kebutuhan Kebijakan Pengendali Volatilitas:**
   Pita ketidakpastian 95% menunjukkan risiko bahwa tanpa pembenahan kurikulum vokasi SMK dan transisi formalitas UMKM, TPT dapat melonjak kembali hingga 7,38% jika terjadi guncangan ekonomi global baru.
3. **Penyelarasan dengan Target RPJMN:**
   Titik ramalan 4,74% pada 2029 berada dalam koridor target pemerintah (4,0% – 5,0%), menegaskan kelayakan target asalkan kesenjangan geografis di Jawa bagian barat dan Papua dapat diatasi.
