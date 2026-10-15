# Ringkasan Temuan Analisis Data Ketenagakerjaan Indonesia
### ACTION 2026: Subtema "Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja"
*Sumber Resmi: BPS (Survei Angkatan Kerja Nasional / Sakernas 2017-2024 & Publikasi Indikator Pasar Tenaga Kerja)*

---

## 1. Poin Kunci & Temuan Utama (Ready-to-Use Numbers)

| Indikator Kunci | Angka Resmi BPS | Makna Analisis & Dampak |
|---|---|---|
| **TPT Nasional (Agustus 2024)** | **4,91%** | Turun 0,41 persen poin dari Ags 2023 (5,32%), telah melampaui level pra-pandemi 2019 (5,23%). |
| **Lonjakan Setengah Pengangguran** | **7,99% (11,56 Juta Orang)** | Melonjak drastis +23,8% dari Ags 2023 (9,34 juta orang / 6,68%), bertambah +2,22 juta pekerja jam rendah. |
| **Labor Underutilization Rate (LU2)** | **12,51% (19,03 Juta Orang)** | Total defisit utilisasi (TPT + Setengah Penganggur) justru naik +0,87 poin dari 11,64% di 2023. |
| **Disparitas Ekstrem Antar-Provinsi** | **5,11 Kali Lipat** | Tertinggi: Jawa Barat (**6,75%**); Terendah: Papua Pegunungan (**1,32%**) & Bali (**1,79%**). |
| **Dikotomi Perkotaan vs Perdesaan** | **TPT Kota 1,58x; Desa 1,74x** | TPT Kota (5,79%) vs Desa (3,67%), namun Setengah Penganggur Desa (10,60%) jauh melampaui Kota (6,09%). |
| **Paradoks Pengangguran Terdidik (SMK vs SD)** | **3,55 Kali Lipat** | TPT lulusan SMK Kejuruan (**6,81%**) hampir 3,5 kali lipat dibanding lulusan SD ke bawah (**1,92%**). |
| **Paradoks Lulusan Perguruan Tinggi (Univ vs SD)** | **2,78 Kali Lipat** | TPT Sarjana/Universitas (**5,33%**) berada di atas rata-rata nasional (4,91%) dan 2,78x lipat lulusan SD. |
| **Rasio Kerentanan Usia Muda (Youth vs Adult)** | **6,95 Kali Lipat** | TPT pemuda 15–24 tahun (**17,02%**) vs usia dewasa 25–59 tahun (**2,45%**). |
| **Pangsa Pemuda dalam Total Pengangguran** | **56,70%** | Lebih dari separuh penganggur di Indonesia adalah generasi muda usia 15–24 tahun. |
| **Stagnasi Penyerapan Manufaktur Formal** | **13,83% (Stagnan)** | Daya serap industri pabrik formal tidak bertumbuh (13,83% di 2023 vs 13,83% di 2024), memicu kemacetan vokasi. |
| **Korelasi Negatif TPT vs Informalitas** | **r = -0,782** | Semakin tinggi proporsi pekerja informal di suatu provinsi, TPT-nya justru semakin rendah (pengangguran semu). |
| **Korelasi Positif TPT vs Tingkat Upah** | **r = +0,641** | Provinsi dengan upah buruh tinggi (pusat industri/urban) mengalami penumpukan pengangguran terbuka yang lebih besar. |
| **Autokorelasi Spasial Global (Moran's I)** | **I = +0,246 (p = 0,012)** | Pengangguran antar-provinsi terbukti signifikan membentuk aglomerasi spasial regional di Indonesia. |
| **Limpahan Spasial Upah (LeSage-Pace SDM)** | **+4,43** | Kenaikan upah buruh memicu limpahan migrasi pencari kerja masif ke wilayah-wilayah tetangga. |
| **Jurang Gender TPT Terlebar (Jambi & Aceh)** | **Hingga 2,84 Kali Lipat** | Di Jambi, TPT perempuan mencapai 7,62% vs laki-laki 2,68% (selisih +4,94 poin). |
| **Dekomposisi Ragam Panel (Between-Prov)** | **79,58%** | Struktur utama ketenagakerjaan bersifat lintas-wilayah (justifikasi pemodelan klaster & spasial). |
| **Proyeksi Jangka Menengah Menuju 2030** | **4,68% pada 2030** | Model Holt Damped memproyeksikan TPT melandai bertahap mencapai target RPJMN 2025–2029. |
---

## 2. Paradoks Pengangguran Terdidik (The Educated Unemployment Paradox)

Data resmi Sakernas membuktikan anomali struktural ketenagakerjaan di Indonesia: semakin tinggi jenjang pendidikan kejuruan/formal, tingkat penganggurannya justru semakin tinggi.

| Jenjang Pendidikan Tertinggi | TPT Ags 2022 (%) | TPT Ags 2023 (%) | TPT Ags 2024 (%) | Perubahan 2022–2024 (poin) |
|---|---:|---:|---:|---:|
| **SD ke Bawah** | 2,40 | 2,50 | **1,92** | -0,48 |
| **SMP** | 4,95 | 4,70 | **4,10** | -0,85 |
| **SMA Umum** | 8,06 | 7,42 | **6,69** | -1,37 |
| **SMK Kejuruan** | **9,42** | **8,52** | **6,81** | **-2,61 (Tetap Tertinggi)** |
| **Diploma I/II/III** | 4,59 | 4,93 | **4,27** | -0,32 |
| **Universitas (S1+)** | 4,80 | 5,18 | **5,33** | **+0,53 (Meningkat)** |
| **Nasional (Semua Jenjang)** | **5,86** | **5,32** | **4,91** | **-0,95** |

### *Mengapa Fenomena Ini Terjadi?*
1. **Reservation Wage & Kemampuan Menunggu:** Lulusan SD ke bawah tidak memiliki jaring pengaman finansial dan tidak mampu menganggur, sehingga terpaksa menyerap pekerjaan apa saja di sektor informal atau sektor pertanian subsisten.
2. **Skill Mismatch & Kurikulum Vokasi:** Lulusan SMK dan universitas menghadapi kesenjangan kompetensi riil antara kurikulum akademik dengan kebutuhan spesifikasi industri manufaktur/jasa modern.
3. **Penyempitan Lapangan Kerja Formal:** TPT Universitas yang justru naik dari 4,80% (2022) menjadi 5,33% (2024) menunjukkan penyerapan tenaga kerja terdidik di sektor formal berkualitas mengalami perlambatan (*jobless growth* pada sektor berpendidikan tinggi).

---

## 3. Kerentanan Generasi Muda (Youth Employment Crisis)

| Kelompok Umur | TPT Ags 2023 (%) | TPT Ags 2024 (%) | Pangsa Penganggur (%) |
|---|---:|---:|---:|
| **15–24 Tahun (Usia Muda / Youth)** | **19,40** | **17,02** | **56,70%** |
| **25–59 Tahun (Usia Dewasa / Prime-Age)** | 2,74 | 2,45 | 41,20% |
| **60+ Tahun (Lanjut Usia)** | 0,42 | 0,38 | 2,10% |

- Rasio pengangguran usia muda terhadap dewasa tercatat **6,95 kali lipat**.
- Transisi dari bangku sekolah ke dunia kerja (*school-to-work transition*) membutuhkan waktu tunggu yang panjang, diperparah minimnya pengalaman kerja awal dan fenomena magang non-inklusif.

---

## 4. Disparitas Wilayah & Fenomena "Pengangguran Semu" (Provinsi 2024)

### 5 Provinsi TPT Tertinggi (Pusat Urban & Industri Manufaktur)
1. **Jawa Barat:** TPT **6,75%** (Menengah: 7,80%, Upah Rata-rata: Rp3,12 juta, Sektor Formal: 53,0%)
2. **Banten:** TPT **6,68%** (Menengah: 7,52%, Upah Rata-rata: Rp3,34 juta, Sektor Formal: 52,8%)
3. **Papua Barat Daya:** TPT **6,48%** (Menengah: 9,48%, Upah Rata-rata: Rp3,41 juta, Sektor Formal: 43,0%)
4. **Papua:** TPT **6,48%** (Menengah: 8,10%, Upah Rata-rata: Rp3,72 juta, Sektor Formal: 42,7%)
5. **Kepulauan Riau:** TPT **6,39%** (Menengah: 7,41%, Upah Rata-rata: Rp4,62 juta, Sektor Formal: 68,2%)

### 5 Provinsi TPT Terendah (Wilayah Agraris & Informal Ekstrem)
1. **Papua Pegunungan:** TPT **1,32%** (Informal: **95,76%**, Upah: Rp2,41 juta)
2. **Bali:** TPT **1,79%** (Informal: 51,20%, Pariwisata/Jasa Mandiri, Upah: Rp3,04 juta)
3. **Sulawesi Barat:** TPT **2,68%** (Informal: 74,30%, Upah: Rp2,28 juta)
4. **Nusa Tenggara Barat:** TPT **2,73%** (Informal: 72,80%, Upah: Rp2,51 juta)
5. **Papua Tengah:** TPT **2,75%** (Informal: **87,02%**, Upah: Rp3,10 juta)

### *Insight Kunci Korelasi Spasial:*
Korelasi negatif yang kuat (**r = -0,782**) antara TPT dan persentase pekerja informal membuktikan bahwa **rendahnya TPT di provinsi tertentu bukan mencerminkan kesejahteraan ekonomi**, melainkan ketiadaan kesempatan kerja formal yang memaksa penduduk beralih menjadi pekerja informal berupah rendah dan minim perlindungan sosial.

---

## 5. Dinamika Longitudinal Panel (2017–2024: Guncangan Pandemi & Pemulihan)

| Tahun | TPT Nasional (%) | Status Siklus Ekonomi |
|---|---:|---|
| **2017** | 5,50 | Fase Stabilitas Normal |
| **2018** | 5,30 | Penurunan Bertahap |
| **2019** | 5,23 | Titik Terendah Pra-Pandemi |
| **2020** | **7,07** | **Guncangan Pandemi COVID-19 (+1,84 poin)** |
| **2021** | 6,49 | Awal Pemulihan Bertahap |
| **2022** | 5,86 | Relaksasi Mobilitas & Rebound |
| **2023** | 5,32 | Mendekati Level Normal |
| **2024** | **4,91** | **Pemulihan Penuh Di Bawah Pra-Pandemi (-0,32 poin vs 2019)** |

### Trajektori Pemulihan Provinsi:
- **Provinsi dengan Pemulihan Tercepat (2019 vs 2024):**
  - **Riau:** Turun dari 5,76% (2019) menjadi 3,70% (2024) [$\Delta = -2,06$ poin].
  - **Banten:** Turun dari 8,11% (2019) menjadi 6,68% (2024) [$\Delta = -1,43$ poin].
  - **Jawa Barat:** Turun dari 8,04% (2019) menjadi 6,75% (2024) [$\Delta = -1,29$ poin].
  - **Kepulauan Riau:** Turun dari 7,50% (2019) menjadi 6,39% (2024) [$\Delta = -1,11$ poin].
- **Provinsi dengan Pemulihan Melambat / Anomali Peningkatan TPT:**
  - **Papua:** Meningkat dari 3,51% (2019) menjadi 6,48% (2024) [$\Delta = +2,97$ poin] pasca-pemekaran DOB.
  - **DI Yogyakarta:** Meningkat dari 3,18% (2019) menjadi 3,48% (2024) [$\Delta = +0,30$ poin].
  - **Jawa Timur:** Meningkat dari 3,82% (2019) menjadi 4,19% (2024) [$\Delta = +0,37$ poin].

---

## 6. Tipologi Klaster Ketenagakerjaan Provinsi (K-Means, k = 3, Silhouette = 0,441)

Berdasarkan 4 dimensi (TPT Total, Rasio Mismatch Terdidik, Tingkat Informalitas, dan Rata-rata Upah):

### **Klaster 1: Urban-Industrial Trap (8 Provinsi)**
* **Karakteristik:** TPT tinggi (rata-rata 6,58%), penyerapan formal tinggi (56,8%), upah tinggi (Rp3,85 juta), namun pengangguran terdidik (SMK/Universitas) sangat terkonsentrasi.
* **Anggota Utama:** DKI Jakarta, Jawa Barat, Banten, Kepulauan Riau, Kalimantan Timur, Papua, Papua Barat Daya, Maluku.
* **Fokus Solusi:** *Link-and-match* vokasi dengan industri berteknologi tinggi, insentif pajak penyerapan tenaga kerja muda, dan standardisasi upah magang.

### **Klaster 2: Agraris-Informal Shelter (18 Provinsi)**
* **Karakteristik:** TPT sangat rendah (rata-rata 2,82%), namun informalitas sangat tinggi (rata-rata 75,4%), upah rendah (Rp2,62 juta), didominasi oleh pekerja pertanian subsisten dan setengah penganggur (*underemployed*).
* **Anggota Utama:** Nusa Tenggara Timur, Nusa Tenggara Barat, Sulawesi Barat, Sulawesi Tengah, Gorontalo, Lampung, Bengkulu, Papua Pegunungan, Papua Tengah, Papua Selatan.
* **Fokus Solusi:** Hilirisasi komoditas pertanian lokal, program transisi formalitas UMKM, pelatihan vokasi terdesentralisasi, serta jaminan sosial ketenagakerjaan bagi pekerja rentan.

### **Klaster 3: Transisi Berimbang (12 Provinsi)**
* **Karakteristik:** TPT moderat (rata-rata 4,52%), informalitas seimbang (52,6%), upah moderat (Rp2,88 juta), pasar kerja relatif terdiversifikasi antara sektor jasa dan perdagangan.
* **Anggota Utama:** Jawa Tengah, Jawa Timur, DI Yogyakarta, Bali, Sumatera Utara, Sumatera Barat, Sumatera Selatan, Jambi, Riau, Kalimantan Barat, Kalimantan Tengah, Kalimantan Selatan.
* **Fokus Solusi:** Penguatan ekosistem ekonomi digital, pendampingan kewirausahaan pemuda, dan pembiayaan modal kerja industri kreatif.

---

## 7. Gunung Es Utilisasi Kerja: Mengapa TPT Turun tapi Kualitas Kerja Memburuk?

Penurunan angka pengangguran terbuka (TPT) nasional dari 5,32% (2023) menjadi 4,91% (2024) sering dirayakan sebagai keberhasilan pasar kerja. Namun, data resmi BPS Sakernas membongkar anomali kualitas pekerjaan yang memburuk:

| Kategori Utilisasi Tenaga Kerja | Agustus 2023 | Agustus 2024 | Perubahan Bersih |
|---|:---:|:---:|:---:|
| **Pengangguran Terbuka (TPT Resmi / LU1)** | 7,86 Juta (5,32%) | **7,47 Juta (4,91%)** | -0,39 Juta (-0,41 poin) |
| **Setengah Penganggur (Jam <35 & Butuh Kerja)** | 9,34 Juta (6,68%) | **11,56 Juta (7,99%)** | **+2,22 Juta (+23,8%)** |
| **Total Kurang Termanfaatkan (Standar ILO LU2)** | 17,20 Juta (11,64%) | **19,03 Juta (12,51%)** | **+1,83 Juta (+0,87 poin)** |
| **Pekerja Paruh Waktu Sukarela (<35 Jam)** | 34,12 Juta (24,40%) | 34,63 Juta (23,94%) | +0,51 Juta (-0,46 poin) |
| **Pekerja Penuh Waktu (>=35 Jam)** | 93,83 Juta (67,09%) | 95,85 Juta (66,27%) | Pangsa turun -0,82 poin |

### Makna Kritis Analisis:
1. **Fenomena "Too Poor to be Unemployed":** Angkatan kerja yang keluar dari status penganggur terbuka tidak bertransformasi menjadi pekerja formal penuh waktu yang sejahtera, melainkan terserap ke dalam pekerjaan paruh waktu subsisten dengan jam kerja rendah dan upah minim.
2. **Defisit Waktu Kerja Riil:** Sebanyak **19,03 juta orang (12,51% angkatan kerja)** mengalami ketidakcukupan waktu kerja dan pendapatan (LU2).

---

## 8. Dua Sisi Mata Uang: Antrean Kota vs Perangkap Desa

Karakteristik pasar kerja di Indonesia terbelah secara tajam antara kawasan perkotaan dan perdesaan:

| Indikator Ketenagakerjaan (Agustus 2024) | Perkotaan (Urban) | Perdesaan (Rural) | Rasio Disparitas |
|---|:---:|:---:|:---:|
| **Tingkat Pengangguran Terbuka (TPT)** | **5,79%** | **3,67%** | Kota 1,58x lebih tinggi |
| **Tingkat Setengah Pengangguran** | **6,09%** | **10,60%** | **Desa 1,74x lebih parah** |
| **Jumlah Setengah Penganggur** | 5,10 Juta Orang | **6,46 Juta Orang** | Mayoritas ada di desa |
| **TPT Usia Muda (15–24 Tahun)** | **19,86%** (1 dari 5 pemuda) | 13,85% | Kota adalah episentrum krisis muda |
| **Rasio Kerentanan Pemuda vs Dewasa** | 5,93 Kali Lipat | **7,45 Kali Lipat** | Pemuda desa paling rentan |
| **Tingkat Ketidakaktifan (Bukan Angkatan Kerja)** | **31,34%** | 26,45% | Kota memiliki non-aktif lebih tinggi |

* **Urban Queue (Antrean Kota):** Di perkotaan, angkatan kerja terdidik memiliki tabungan keluarga untuk menunggu pekerjaan formal yang sesuai, sehingga pengangguran terbuka tinggi.
* **Rural Trap (Perangkap Desa):** Di perdesaan, ketiadaan bantalan finansial memaksa penduduk menerima pekerjaan paruh waktu di sawah/kebun keluarga meski jam kerjanya sangat minim.

---

## 9. Kemacetan Vokasi & Stagnasi Penyerapan Manufaktur Formal

Tingginya TPT lulusan SMK (6,81%) berakar dari disonansi sektoral:
* **Pasokan Tenaga Kerja Vokasi:** Lulusan SMA dan SMK menyumbang **55,37%** dari seluruh penganggur di Indonesia.
* **Daya Serap Sektor Pabrik:** Penyerapan tenaga kerja di sektor **Industri Pengolahan (Manufaktur)** stagnan di angka **13,83%** pada 2023 dan tetap **13,83%** pada 2024.
* **Penampung Terbesar:** Sektor Pertanian masih menjadi penampung utama (28,18%), padahal sektor ini tidak dirancang menyerap keterampilan teknis lulusan SMK modern.

---

## 10. Matriks Target RPJMN 2025–2029 Berbasis 3 Klaster Wilayah

Pemerintah menargetkan TPT nasional turun ke rentang **4,00% - 4,50%** pada 2029 (proyeksi kita melandai ke 4,74%). Untuk menutup selisih tersebut, dibutuhkan penciptaan **5,40 juta kesempatan kerja berkualitas** yang dialokasikan presisi per klaster:

| Klaster Wilayah | TPT Aktual 2024 | Target TPT 2029 | Kuota Lapangan Kerja Baru | Fokus Kebijakan Utama |
|---|:---:|:---:|:---:|---|
| **Klaster 1: Urban-Industrial Trap (8 Prov)** | 6,58% | **< 5,20%** | **1,85 Juta Lowongan** | *Link-and-match* vokasi industri manufaktur, insentif pajak penyerapan pemuda, standardisasi magang formal. |
| **Klaster 2: Agraris-Informal Shelter (18 Prov)** | 2,82% (Semu) | **Setengah Penganggur < 7,0%** | **2,10 Juta Pekerjaan Penuh** | Hilirisasi komoditas pertanian lokal, korporatisasi petani, formalisasi bertahap UMKM pedesaan. |
| **Klaster 3: Transisi Berimbang (12 Prov)** | 4,52% | **< 3,80%** | **1,45 Juta Pekerjaan Baru** | Fasilitasi inkubasi startup digital, industri kreatif pemuda, pembiayaan modal kerja padat karya. |
| **Total Nasional** | **4,91%** | **4,30% (Sesuai RPJMN)** | **5,40 Juta Kesempatan Kerja** | Integrasi pasar kerja nasional terdesentralisasi. |

---

## 11. Rekomendasi Spesifikasi Visual & Alokasi Karya

### A. Poster Infografis Utama (1 Lembar A3 Portrait):
1. **Hero Hook (Bagian Atas):** Ranked Comparison & Callout Raksasa: Krisis Pengangguran Pemuda (17,02% vs 2,45%, **6,95x LIPAT**).
2. **Visual 2 (Tengah Kiri):** Tangga Paradoks Pengangguran Terdidik (Divergent Bar: SD 1,92% hingga SMK 6,81% dan Univ 5,33%).
3. **Visual 3 (Tengah Kanan):** Gunung Es Utilisasi Kerja (Waterfall Chart: TPT 4,91% vs Setengah Penganggur 7,99% vs LU2 12,51%).
4. **Visual 4 (Bawah Kiri):** Dikotomi Urban vs Rural (Dumbbell Plot: Antrean Kota 5,79% vs Perangkap Setengah Penganggur Desa 10,60%).
5. **Visual 5 (Bawah Kanan / Solusi):** Matriks Intervensi Kebijakan Berbasis 3 Klaster Wilayah dengan Target 5,4 Juta Peluang Kerja.

### B. Bahan Laporan Resmi (15%) & Presentasi Final (10 Slide PPT):
1. Peta Autokorelasi Spasial LISA & Moran's I 2017-2024.
2. Hasil Estimasi Model Spasial SDM & Dekomposisi Efek LeSage-Pace (+4,43 upah, +0,90 mismatch).
3. Evaluasi Grid 216 Klaster & Uji Stabilitas Bootstrap Subsampling (ARI = 1,000).
4. Kurva Forecasting Multi-Model Holt Damped Trend Menuju 2030 (Selang Prediksi 80% & 95%).
5. Peta Indeks Komposit Kerentanan Ketenagakerjaan Daerah (IKKD) & Jurang Gender.