# Ringkasan Temuan Analisis Data Ketenagakerjaan Indonesia
### ACTION 2026 — Subtema: “Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”
*Sumber Resmi: BPS (Survei Angkatan Kerja Nasional / Sakernas 2017–2024 & Publikasi Indikator Pasar Tenaga Kerja)*

---

## 1. Poin Kunci & Temuan Utama (Ready-to-Use Numbers)

| Indikator Kunci | Angka Resmi BPS | Makna Analisis & Dampak |
|---|---|---|
| **TPT Nasional (Agustus 2024)** | **4,91%** | Turun 0,41 persen poin dari Ags 2023 (5,32%), telah melampaui level pra-pandemi 2019 (5,23%). |
| **Disparitas Ekstrem Antar-Provinsi** | **5,11 Kali Lipat** | Tertinggi: Jawa Barat (**6,75%**); Terendah: Papua Pegunungan (**1,32%**) & Bali (**1,79%**). |
| **Paradoks Pengangguran Terdidik (SMK vs SD)** | **3,55 Kali Lipat** | TPT lulusan SMK Kejuruan (**6,81%**) hampir 3,5 kali lipat dibanding lulusan SD ke bawah (**1,92%**). |
| **Paradoks Lulusan Perguruan Tinggi (Univ vs SD)** | **2,78 Kali Lipat** | TPT Sarjana/Universitas (**5,33%**) berada di atas rata-rata nasional (4,91%) dan 2,78x lipat lulusan SD. |
| **Rasio Kerentanan Usia Muda (Youth vs Adult)** | **6,95 Kali Lipat** | TPT pemuda 15–24 tahun (**17,02%**) vs usia dewasa 25–59 tahun (**2,45%**). |
| **Pangsa Pemuda dalam Total Pengangguran** | **56,70%** | Lebih dari separuh penganggur di Indonesia adalah generasi muda usia 15–24 tahun. |
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

## 7. Rekomendasi Spesifikasi Visual untuk Tim Desain Infografis

1. **Panel 1 (The Hook):** *Kesenjangan Generasi*
   - Tipe visual: Ranked Comparison / Gauge Chart perbandingan TPT Pemuda 15–24 tahun (**17,02%**) vs TPT Dewasa 25–59 tahun (**2,45%**), dihiasi angka penekanan **6,95x LIPAT**.
2. **Panel 2 (The Paradox):** *Paradoks Ijazah*
   - Tipe visual: Divergent Horizontal Bar Chart mengurutkan TPT dari SD ke Bawah (1,92%) hingga SMK Kejuruan (6,81%) dan Universitas (5,33%). Highlight warna kontras pada SMK dan Universitas.
3. **Panel 3 (The Spatial Trade-Off):** *Peta Anatomi Disparitas Regional*
   - Tipe visual: Scatterplot / Quadrant Chart (Sumbu X: Tingkat Informalitas, Sumbu Y: TPT Total 2024), menampilkan korelasi $r = -0,782$. Peta choropleth Indonesia dengan pewarnaan 3 Klaster Wilayah.
4. **Panel 4 (Longitudinal Shock & Recovery):** *Guncangan COVID & Tren Pemulihan*
   - Tipe visual: Area Chart / Sparkline 2017–2024 yang menyorot lonjakan tajam 7,07% (2020) dan tren penurunan menuju 4,91% (2024).
5. **Panel 5 (Actionable Opportunity):** *Matriks Kebijakan Berbasis Klaster*
   - Tipe visual: 3 Kartu Kebijakan Terarah (Klaster 1: *Urban Link-and-Match*, Klaster 2: *Formalisasi Agraris*, Klaster 3: *Penguatan Ekosistem Digital Pemuda*).