# Ringkasan Hasil — Peramalan Tekanan Sistem Pangan ASEAN
### RASIO 10.0 · angka siap pakai untuk panel pembuka (Latar Belakang)

Seluruh angka dihasilkan dari `Analisis_Forecasting_RASIO.ipynb` (51 sel, 29 sel kode,
sudah diuji berjalan penuh tanpa galat) atas data Our World in Data 1961–2024.

---

## 1. Cakupan percobaan

**2.904 evaluasi fold-model**: 12 model × 4 horizon (h = 1, 3, 5, 10) × 2 skema jendela
(expanding dan rolling 30 tahun) × 24–34 fold per kombinasi. Origin minimum 30 tahun.

Model yang diuji: Naive · Drift · Rata-rata 5 tahun · Holt · Holt teredam · Holt tuned (SSE) ·
Theta · ARIMA orde-AICc (Hannan-Rissanen) · ARIMAX (+populasi) · Tren linear · Ridge lag-3 ·
Gradient Boosting lag-3.

---

## 2. Pemeriksaan pra-model

| Uji | Hasil | Kesimpulan |
|---|---|---|
| Kekuatan tren (LOESS) | **0,998** | tren hampir deterministik |
| ADF level (log) | −0,179 | non-stasioner |
| KPSS level | 1,695 | non-stasioner |
| ADF setelah d=1 | **−9,093** | stasioner |
| KPSS setelah d=1 | **0,049** | stasioner |

Kedua uji sepakat pada **d = 1**. Data tahunan, sehingga tidak ada komponen musiman —
STL periode-12 dan SARIMA musiman tidak berlaku dan diganti dekomposisi tren LOESS.

**Keputusan regressor eksogen.** `luc` (CO₂ alih guna lahan tahunan) dikeluarkan karena
kebocoran data — nilainya baru diketahui pada tahun yang sama dengan target. `populasi`
dipertahankan karena proyeksinya dirilis PBB independen dan jauh ke depan.

---

## 3. Model juara

Juara ditentukan lewat **rata-rata peringkat atas 32 kombinasi** (4 horizon × 4 metrik ×
2 skema jendela), bukan rata-rata MAPE mentah.

| Model | h=1 | h=3 | h=5 | h=10 |
|---|---|---|---|---|
| **Drift** | **1,34%** | **2,18%** | **2,67%** | **3,10%** |
| ARIMA (AICc) | 1,52% | 2,27% | 2,75% | 3,60% |
| Holt | 1,57% | 2,41% | 2,81% | 3,70% |
| ARIMAX (+populasi) | 1,59% | 2,42% | 2,89% | 3,72% |
| Naive (baseline) | 2,16% | 3,08% | 3,88% | 6,58% |

**Juara: Drift**, runner-up ARIMA (AICc) dengan selisih peringkat 0,75. MASE pada h=1 =
**0,987** — mengungguli naive. Hasil identik pada skema rolling, jadi juaranya tidak
bergantung pada pilihan jendela.

Temuan yang layak ditulis: model sederhana mengalahkan Gradient Boosting dan Ridge. Pada
deret tahunan 64 titik dengan tren kuat dan sedikit struktur lain, model kompleks hanya
menambah ragam tanpa menambah informasi.

---

## 4. Uji Diebold-Mariano

Selisih MAPE antarmodel diuji formal (koreksi Harvey-Leybourne-Newbold, h=5). Hasilnya:
**tujuh model tidak berbeda signifikan** dari juara — Holt, Holt teredam, Holt tuned, Theta,
ARIMA, Tren linear, Ridge lag-3.

Konsekuensi metodologisnya: karena tidak ada bukti satu model unggul, **ensemble dapat
dibenarkan** — merata-ratakan mengurangi risiko salah pilih. Anggota ensemble final:
Drift, Holt, Holt teredam, Holt tuned.

---

## 5. Kalibrasi selang prediksi

Pita dibangun dari **kuantil galat walk-forward empiris**, bukan asumsi normalitas.
Cakupan terverifikasi:

| Nominal | h=1 | h=3 | h=5 | h=10 |
|---|---|---|---|---|
| 50% | 50% | 50% | 50% | 50% |
| 80% | 75% | 75% | 75% | 75% |
| 95% | 92% | 92% | 92% | 92% |

Sedikit di bawah nominal pada 80% dan 95% — artinya pita cenderung **agak terlalu sempit**,
dan itu dilaporkan apa adanya, bukan disembunyikan.

---

## 6. Diagnostik residual

| Uji | Statistik | p | Kesimpulan |
|---|---|---|---|
| Ljung-Box (lag 5) | 3,155 | 0,676 | tidak ada autokorelasi tersisa |
| Ljung-Box (lag 10) | 11,801 | 0,299 | tidak ada autokorelasi tersisa |
| ARCH-LM(4) | 3,811 | 0,432 | tidak ada efek ARCH |
| Jarque-Bera | 2,117 | 0,347 | konsisten dengan normal |

Keempatnya lolos. Residual menyerupai white noise, sehingga selang prediksi layak dipercaya.

---

## 7. Robustness dan rekonsiliasi hirarkis

**Patahan struktural.** CUSUM tidak pernah melewati batas 5%. Uji Chow pada setiap tahun
kandidat menemukan patahan terkuat di **2009** (F = 25,51; p < 0,00001). Namun ketika dummy
patahan dimasukkan ke model, akurasi **tidak membaik** — skema "Tanpa dummy" tetap menang di
seluruh horizon. Ini temuan negatif yang tetap dilaporkan: patahan itu nyata secara historis
tetapi tidak membantu meramal ke depan.

**Rekonsiliasi hirarkis.** ASEAN adalah jumlah sepuluh negara, sehingga tersedia dua jalur:
meramal agregat langsung, atau meramal tiap negara lalu menjumlahkannya. Bobot optimal hasil
CV: **langsung 1,00, bottom-up 0,00** — agregat langsung lebih akurat di semua horizon, karena
galat sepuluh ramalan negara terakumulasi alih-alih saling meniadakan.

---

## 7B. Tuning lanjutan — 266 konfigurasi, validasi tiga arah

Ruang pencarian diperluas dari 12 kandidat berparameter tetap menjadi **266 konfigurasi**:
panjang jendela drift, faktor peredaman, drift kokoh berbasis median, grid Holt (α × β × φ),
bobot Theta, orde ARIMA sampai (3,2,3), dan strategi **direct multi-step** yang melatih regresi
terpisah untuk tiap horizon.

Karena memilih pemenang dari 266 kandidat pada data yang sama akan overfit terhadap pemilihan
itu sendiri, dipakai pembagian tiga arah:

| Bagian | Origin | Tahun | Fungsi |
|---|---|---|---|
| INNER | 30–41 | 1991–2002 | memilih hiperparameter |
| MID | 42–52 | 2003–2013 | memilih strategi |
| OUTER | 53–63 | 2014–2024 | menilai — tidak pernah disentuh |

**Hasil pada fold OUTER:**

| Horizon | Strategi terpilih (dari MID) | Drift polos | Terpilih | Perbaikan |
|---|---|---|---|---|
| h=1 | Drift polos | 1,588% | 1,588% | 0,0% |
| h=3 | Drift polos | 2,568% | 2,568% | 0,0% |
| h=5 | ens top-5 | 2,623% | **2,524%** | **−3,8%** |
| h=10 | ens top-5 | 5,230% | **3,773%** | **−27,8%** |
| **rata-rata** | | 3,002% | **2,613%** | **−13,0%** |

**Aturan final: h ≤ 3 → Drift polos; h ≥ 4 → ensemble top-5 tertuning.**

Temuan metodologisnya: pada horizon pendek, tuning **memperburuk** akurasi — nilai terakhir
mendominasi dan menambah parameter hanya menambah ragam. Pada horizon panjang, penaksiran tren
mendominasi galat, sehingga merata-ratakan lima penaksir tren terbaik menurunkan ragamnya secara
nyata. Memilih satu konfigurasi terbaik (top-1) justru tidak memberi perbaikan sama sekali
(−0,0%) — murni overfitting pemilihan.

MAPE CV model final: **2,473% pada h=5** (dari 2,668%) dan **2,935% pada h=10** (dari 3,10%).

---

## 8. Proyeksi akhir — angka untuk infografis

**Target utama — Metana ASEAN (Mt CO₂e/tahun), model final tertuning**

| | Nilai | vs 2024 |
|---|---|---|
| 2024 aktual | 809,2 | — |
| 2030 proyeksi | **884,2** | **+9,3%** |
| 2035 proyeksi | **990,3** | **+22,4%** |
| Selang 80% pada 2035 | 960,8 – 1.065,3 | |

*Pembanding model dasar sebelum tuning: 2030 = 880,2 (+8,8%); 2035 = 940,9 (+16,3%).
Model tertuning memproyeksikan lebih tinggi karena pada horizon panjang komposisinya didominasi
model ekstrapolasi tren (LinTren, Direct), yang pada validasi OUTER terbukti 27,8% lebih akurat
di h=10 daripada drift polos.*

**Seri sekunder** (tiap seri memilih juaranya sendiri lewat CV terpisah)

| Seri | Model juara | MAPE h=5 | 2024 | 2035 | Perubahan |
|---|---|---|---|---|---|
| N₂O ASEAN (Mt CO₂e) | Theta | 3,27% | 170,7 | 194,8 | **+14,1%** |
| Pangsa metana global (%) | Drift | 2,30% | 8,52 | 9,18 | **+7,8%** |
| Kumulatif CO₂ alih guna lahan (Mt) | ARIMA | 0,79% | 164.518 | 187.123 | **+13,7%** |
| Populasi ASEAN (juta) | ARIMA | 0,21% | 693,7 | 730,2 | **+5,3%** |

---

## 9. Seri yang sengaja TIDAK diramal

| Seri | MAPE h=3 | h=5 | h=10 |
|---|---|---|---|
| CO₂ alih guna lahan tahunan | 18,8% | 23,1% | 32,8% |
| GHG sistem pangan absolut | 12,3% | 15,1% | 21,7% |
| Metana (pembanding, dipakai) | 2,2% | 2,7% | 3,1% |

Perubahan tahunan CO₂ alih guna lahan **15,6× lebih bergejolak** daripada metana, karena
tahun-tahun kebakaran gambut (1997–98, 2015). Meramalkannya menghasilkan pita selebar
grafiknya sendiri.

---

## 10. Dekomposisi skala vs intensitas — wajib dibaca sebelum menulis narasi

Perubahan 2000–2024:

| Indikator | Perubahan |
|---|---|
| Populasi | **+31,8%** |
| Metana absolut | **+55,4%** |
| N₂O absolut | **+39,4%** |
| GHG pangan absolut | +0,8% |
| Metana per kapita | +17,9% |
| CO₂ lahan absolut | **−23,5%** |
| CO₂ lahan per kapita | **−41,9%** |
| GHG pangan per kapita | **−23,5%** |

Narasi "konversi lahan ASEAN meledak" **bertentangan dengan data** — lajunya justru menurun.
Framing yang benar dan lebih kuat: **skala bertambah sementara intensitas per kapita membaik,
dan komposisi tekanan bergeser dari perluasan lahan ke intensifikasi.** Ini menyambung langsung
ke Pembahasan, tempat model SDM menunjukkan N₂O punya limpahan lintas negara terbesar (+1,105).

---

## 11. Daftar berkas

**Data**: `agregat_asean_tahunan.csv` (64 × 13) · `metana_per_negara_asean.csv` (64 × 10) ·
`proyeksi_metana_asean.csv`

**Analisis**: `Analisis_Forecasting_RASIO.ipynb` — 51 sel, 29 sel kode, sudah diuji berjalan
penuh. Ditulis dengan numpy/scipy murni sehingga tidak memerlukan statsmodels atau prophet;
Bagian 18 memuat sel pembanding bila paket itu tersedia.

**Gambar** (25 SVG vektor di `gambar_forecast/`): `00_empat_seri` · `01_dekomposisi_tren` ·
`02_acf_pacf` · `03_ccf_kebocoran` · `04_perbandingan_model_cv` · `05_sebar_antarfold` ·
`06_mape_per_window` · `07_diebold_mariano` · `08_kalibrasi_selang` · `09_cusum` · `10_chow` ·
`11_robustness_patahan` · `12_diagnostik_residual` · `13_rekonsiliasi_hirarkis` ·
`14_fan_h3` · `15_fan_h6` · `16_fan_h11` · `17_seri_sekunder` · `18_seri_ditolak` ·
`19_skala_vs_intensitas` · `20_hasil_tuning` · **`21_fan_penuh`** (fan chart dari titik awal
data 1961) · **`22_fan_penuh_log`** (skala log) · `23_fan_zoom` · `24_lama_vs_tuned`
