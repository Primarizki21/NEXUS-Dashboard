# Ringkasan Hasil — Klasterisasi dan Ekonometrika Panel-Spasial Sistem Pangan ASEAN
### RASIO 10.0 · angka siap pakai untuk bagian Pembahasan

Seluruh angka di bawah diperoleh dari menjalankan `Analisis_Klaster_Panel_Spasial_RASIO.ipynb`
atas data Our World in Data (*CO2 and Greenhouse Gas Emissions*, Global Carbon Budget & Jones dkk.).

---

## 1. Bentuk data

Panel seimbang **44 negara Asia-Pasifik × 64 tahun (1961–2024) = 2.816 observasi**, tanpa satu pun
nilai rumpang pada keempat variabel. Sepuluh negara ASEAN seluruhnya termasuk.

| Peran | Variabel | Makna dalam sistem pangan |
|---|---|---|
| Y | CO₂ alih guna lahan per kapita | tekanan konversi hutan menjadi lahan pangan |
| X1 | Metana per kapita | sawah tergenang dan ternak ruminansia |
| X2 | N₂O per kapita | intensitas pemupukan nitrogen |
| X3 | CO₂ energi per kapita | mekanisasi, rantai dingin, pengangkutan |

**Dekomposisi ragam panel** — pangsa ragam antar-negara: CO₂ lahan 75,8%, metana 86,1%,
N₂O 92,8%, CO₂ energi 85,9%. Struktur utama bersifat lintang, sehingga klaster berbasis aras sah,
tetapi dimensi waktu tetap diuji terpisah (lihat butir 3).

---

## 2. Klaster

Konfigurasi terpilih dari **864 kombinasi** yang dijelajahi (4 praproses × 3 ruang fitur ×
3 proyeksi × 4 nilai k × 6 algoritma), 543 di antaranya lolos syarat kelayakan:
**POTRET · Standard · PCA2 · KMeans · k = 5**.

- Silhouette **0,5336**; PC1 (56,6%) + PC2 (28,3%) = **84,9%** ragam terjelaskan
- Stabilitas subsampling 85% (300×): **ARI 0,973 ± 0,042** — sangat stabil
- Hanya satu negara bersilhouette negatif (Lebanon)

| Klaster | n | ASEAN di dalamnya |
|---|---|---|
| **Frontier Konversi Lahan** | 8 | **Kamboja, Indonesia, Laos, Malaysia, Myanmar, Thailand, Vietnam** |
| Peternakan Ekstensif | 4 | Brunei |
| Padat Penduduk Intensitas Rendah | 14 | Filipina |
| Industri Mapan Rendah-Lahan | 12 | Singapura |
| Petro-Ekonomi Pengimpor Pangan | 6 | — |

**Temuan inti: tujuh dari sepuluh negara ASEAN membentuk satu klaster tunggal**, bergabung hanya
dengan Papua Nugini. Filipina, Singapura, dan Brunei adalah tiga pengecualian.

---

## 3. Mengapa panel tidak boleh direduksi jadi satu tahun

Kesepakatan tipologi antar-ruang-fitur sangat rendah:

| Perbandingan | ARI |
|---|---|
| POTRET vs LINTASAN | 0,173 |
| POTRET vs SERI | 0,055 |
| LINTASAN vs SERI | 0,143 |

Artinya tipologi berdasarkan **lintasan 64 tahun** berbeda nyata dari tipologi berdasarkan potret
satu periode. Ini justifikasi metodologis bahwa analisis harus panel, bukan lintang.

**Kestabilan lintas dekade** — rata-rata 1,17 perpindahan klaster per negara ASEAN dari 5 transisi.
Indonesia, Laos, Malaysia, dan Singapura tidak pernah berpindah klaster sejak 1961.

---

## 4. Indeks komposit — tiga sudut pandang yang berbeda

| Ukuran | Peringkat teratas | ASEAN teratas |
|---|---|---|
| A. Intensitas per kapita (bobot PC1) | Mongolia 0,852 | Brunei 0,644 (ke-4) |
| B. Tekanan konversi lahan | Selandia Baru 0,833 | Laos 0,666 (ke-4) |
| C. **Pangsa emisi lahan global 2024** | **Indonesia 12,57%** | Indonesia |

Korelasi Spearman antara A dan C hanya **0,008** — praktis nol. Negara yang tampak terburuk
per kapita sama sekali bukan negara yang menentukan secara global. Perbedaan ini sendiri layak
jadi satu panel infografis.

**Angka pembuka terkuat: ASEAN menyumbang 22,78% emisi CO₂ alih guna lahan dunia pada 2024,**
padahal hanya 7,44% dari total GHG global. Indonesia sendirian menyumbang 12,57%.

---

## 5. Autokorelasi spasial

Bobot terpilih: **k-tetangga-terdekat dengan k = 4** (ketergantungan residual terkuat, Moran's I
residual OLS = 0,7029).

Moran's I 2024: CO₂ lahan **+0,7285** (p = 0,001, mengelompok) · metana +0,2517 (p = 0,007) ·
CO₂ energi +0,3628 (p = 0,003) · N₂O +0,1117 (p = 0,185, acak).

**Lintasan Moran's I untuk CO₂ alih guna lahan — pengelompokan makin mengetat:**

| 1961 | 1975 | 1989 | 2003 | 2017 | 2024 |
|---|---|---|---|---|---|
| +0,255 | +0,498 | +0,472 | +0,593 | +0,601 | **+0,729** |

Seluruhnya signifikan pada 5%. Nilai harapan di bawah hipotesis nol hanya −0,023.

**LISA 2024** — 10 negara High-High, **7 di antaranya ASEAN**: Kamboja, Indonesia, Laos, Malaysia,
Myanmar, Thailand, Vietnam (bersama Australia, Selandia Baru, Papua Nugini).
**Filipina dan Singapura justru Low-High** — dua pengecualian di tengah hotspot-nya sendiri.

Ketekunan lintas 7 titik dekade: Kamboja High-High 6/7, Thailand 5/7, Laos 4/7, Indonesia 4/7,
Vietnam 4/7, Malaysia 3/7.

---

## 6. Model panel spasial

Efek tetap **waktu** (spesifikasi utama):

| Model | par | logLik | AIC | ρ / λ | R² |
|---|---|---|---|---|---|
| OLS | 3 | −2812,2 | 5630,3 | — | 0,243 |
| SLX | 6 | −2712,8 | 5437,6 | — | 0,294 |
| SAR | 4 | −2420,4 | 4848,8 | 0,507 | 0,460 |
| SEM | 4 | −2414,4 | 4836,7 | 0,551 | 0,469 |
| **SDM** | **7** | **−2369,0** | **4752,0** | **0,516** | **0,481** |

Uji LR: SAR vs OLS = 783,5 · SEM vs OLS = 795,6 · SDM vs SAR = 102,7 (khi-kuadrat 5% = 3,84).
**SDM terpilih menurut AIC.** Moran's I residual signifikan hanya pada 2 dari 64 tahun (3%) —
ketergantungan spasial terserap.

Koefisien SDM (seluruhnya signifikan pada 1%):

| Variabel | β | t |
|---|---|---|
| log Metana/kap | +0,3694 | +15,77 |
| log N₂O/kap | +0,4179 | +12,02 |
| log CO₂ energi/kap | −0,3093 | −18,63 |
| W × log Metana/kap | −0,3342 | −8,74 |
| W × log N₂O/kap | +0,3586 | +3,66 |
| W × log CO₂ energi/kap | +0,1299 | +4,55 |

**Dekomposisi efek LeSage–Pace:**

| Variabel | Langsung | Tak langsung | Total |
|---|---|---|---|
| log Metana/kap | +0,3486 | −0,2759 | +0,0727 |
| log N₂O/kap | +0,5011 | **+1,1046** | +1,6057 |
| log CO₂ energi/kap | −0,3137 | −0,0573 | −0,3710 |

Tafsir untuk naskah: intensitas pupuk punya **limpahan lintas negara lebih dari dua kali lipat
efek domestiknya** — tekanan konversi lahan tidak berhenti di batas negara. Sebaliknya, metana
tetangga justru berasosiasi negatif dengan konversi lahan sendiri, pola yang konsisten dengan
spesialisasi regional. *Catatan kehati-hatian:* persentase limpahan untuk metana tidak dilaporkan
karena efek totalnya mendekati nol sehingga rasionya tidak stabil.

---

## 7. Catatan metodologis yang wajib ditulis di naskah

**Pertama — mengapa efek tetap waktu saja, bukan dua arah.** Pada efek tetap dua arah seluruh suku
spasial runtuh (ρ = 0,019; LR = 0,53; R² = 0,017). Penyebabnya, efek tetap negara menyerap justru
variasi antar-negara yang merupakan sinyal spasial itu sendiri — konsisten dengan dekomposisi ragam
di butir 1 yang menunjukkan 76–93% ragam bersifat antar-negara. Pilihan ini harus dinyatakan
terbuka, bukan didiamkan, karena juri yang paham akan menanyakannya.

**Kedua — mengapa 44 negara, bukan 10.** Pada ASEAN-10 saja, Moran's I tidak signifikan di seluruh
spesifikasi yang diuji (inverse-distance, KNN k=3, aras, log): nilainya −0,05 sampai −0,23 dengan
p > 0,17, sementara nilai harapan di bawah hipotesis nol sudah −0,111. Regresi spasial pada n=10
tidak punya kuasa uji yang memadai.

**Ketiga — perluasan sampel tidak menggeser cerita ASEAN.** Tipologi ASEAN identik antara sampel
Asia-44 dan Asia Monsun-19: **ARI = 1,000**. Pada sampel Monsun-19 model tetap sahih
(ρ = +0,375; LR = 89,9; Moran's I 2024 = +0,346, p = 0,003). Jadi perluasan sampel murni demi
kesahihan statistik, bukan demi hasil yang lebih enak.

**Keempat — Brunei adalah pencilan sejati.** Metananya 6,31 t/kapita berasal dari migas, bukan
sistem pangan. Perlakukan khusus atau jelaskan terbuka sebagai anomali petro-state.

---

## 8. Daftar berkas

**Data**
`panel_asia_1961_2024.csv` (2.816 × 16, panel utama) · `potret_2015_2024.csv` ·
`fitur_lintasan_negara.csv` · `koordinat_negara.csv` · `jarak_km_asia44.csv` ·
`W_knn{3..8}_asia44.csv` · `W_knn{3..8}_monsun19.csv`

**Hasil**
`hasil_klaster_lengkap.csv` · `hasil_klaster_asean10.csv` · `jalur_klaster_dekade.csv` ·
`grid_konfigurasi_klaster.csv` · `lisa_2024.csv` · `moran_lintasan_tahun.csv` ·
`dekomposisi_efek_sdm.csv`

**Analisis**
`Analisis_Klaster_Panel_Spasial_RASIO.ipynb` — 39 sel, seluruhnya sudah diuji berjalan tanpa galat.
Ditulis dengan numpy murni sehingga tidak memerlukan libpysal/spreg; Bagian 14 memuat sel
pembanding bila paket itu tersedia di komputer kalian.

**Gambar** (SVG vektor, siap dibuka di Figma/Illustrator)
`gambar/01_sebar_klaster` · `02_silhouette` · `03_moran_lintasan` · `04_pencar_moran` ·
`05_peta_lisa` · `06_dendrogram` · `07_lintasan_asean` · `08_dekomposisi_efek`
