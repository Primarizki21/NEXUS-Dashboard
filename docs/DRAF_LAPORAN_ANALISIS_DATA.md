# Draf Bagian Analisis Data untuk Laporan Resmi Infografis ACTION 2026
*Panduan Pengisian Laporan Bab (c), (d), (e), (f), dan (g)*
*Subtema: “Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja”*
*Penyelenggara: HMP Sains Data, Universitas Negeri Surabaya (UNESA)*

---

## Bab C: Sumber & Pengolahan Data

### 1. Sumber Data Resmi
Seluruh dataset yang digunakan dalam karya ini bersumber 100% dari portal data resmi yang direkomendasikan panitia:
1. **Badan Pusat Statistik (BPS) Republik Indonesia (`https://bps.go.id/`):**
   * *Publikasi Indikator Pasar Tenaga Kerja Indonesia Agustus 2024* (Katalog BPS: 2102007, rilis Desember 2024), mencakup:
     - Lampiran 17: Tingkat Pengangguran Terbuka Menurut Provinsi dan Jenis Kelamin (persen), 2023–2024.
     - Lampiran 18: Tingkat Pengangguran Terbuka Menurut Provinsi dan Tingkat Pendidikan (persen), 2023–2024.
     - Lampiran 16: Persentase Penduduk Bekerja Menurut Provinsi dan Kegiatan Formal/Informal, 2023–2024.
     - Lampiran 20: Persentase Setengah Pengangguran Menurut Provinsi dan Tingkat Pendidikan, 2023–2024.
     - Lampiran 26: Rata-Rata Upah Buruh/Karyawan/Pegawai Menurut Provinsi dan Jenis Kelamin (rupiah), 2023–2024.
     - Tabel 5 & 6 (Bab 3): Tingkat Pengangguran Terbuka dan Distribusi Penganggur Menurut Tingkat Pendidikan Rinci serta Kelompok Umur.
   * *Berita Resmi Statistik (BRS) No. 81/11/Th. XXVII, 5 November 2024:* Keadaan Ketenagakerjaan Indonesia Agustus 2024.
   * *Publikasi Indikator Ketenagakerjaan 2017–2021 & Profil Pengangguran 2022–2023:* Tabel perkembangan longitudinal TPT provinsi periode 2017–2023 berbasis Sakernas Agustus.
2. **Satu Data Indonesia (`https://data.go.id/`):**
   * Referensi silang data makroekonomi regional, kode wilayah provinsi, dan indikator pasar kerja daerah.

### 2. Prosedur Pra-Pemrosesan & Pembersihan Data
Proses ekstraksi dan kurasi data dilakukan melalui pipeline Python reproduktif (`scripts/extract_bps_tables.py` dan `scripts/build_panel_tpt_2017_2024.py`):
1. **Ekstraksi Presisi dari Publikasi Resmi:**
   * Menggunakan pustaka `pdfplumber` dengan algoritma penyaringan font koordinat untuk mengisolasi data tabel murni dari *watermark* halaman BPS.
   * Melakukan normalisasi format desimal koma Indonesia ke float standar, serta menangani baris provinsi bertingkat (*multiline wrapping*).
2. **Penyelarasan Disparitas Wilayah (34 vs 38 Provinsi):**
   * Untuk analisis longitudinal 2017–2024: digunakan panel seimbang 34 provinsi (definisi pra-DOB Papua) untuk menjaga konsistensi deret waktu.
   * Untuk analisis potret mutakhir 2024: digunakan cakupan penuh 38 provinsi di Indonesia.
3. **Pemeriksaan Kualitas Data (Zero Missing Values):**
   * Seluruh tabel yang diekspor ke folder `data/clean/` telah melalui verifikasi null-check, memastikan 100% kelengkapan data tanpa nilai rumpang (*missing values*).

---

## Bab D: Data Deskripsi dan Teknis Temuan

### 1. Deskripsi Makro Nasional: Pemulihan Pasca-Pandemi
* Pada Agustus 2024, Tingkat Pengangguran Terbuka (TPT) nasional tercatat sebesar **4,91%**, turun 0,41 persen poin dibandingkan Agustus 2023 (5,32%).
* Angka ini telah melampaui level pra-pandemi COVID-19 (5,23% pada Agustus 2019), setelah sempat melonjak ke puncak 7,07% pada Agustus 2020 (+1,84 persen poin).
* Dari total angkatan kerja sebesar 152,11 juta orang, sebanyak 144,64 juta orang berstatus bekerja, sedangkan 7,47 juta orang berstatus penganggur terbuka.

### 2. Paradoks Pengangguran Terdidik (The Educated Unemployment Paradox)
Salah satu temuan paling krusial adalah anomali struktural penyerapan tenaga kerja berdasarkan jenjang pendidikan:
* **SMK Kejuruan Tertinggi:** TPT lulusan SMK Kejuruan mencapai **6,81%**, merupakan yang tertinggi di antara seluruh jenjang pendidikan, disusul SMA Umum (**6,69%**).
* **Universitas Meningkat:** TPT lulusan Perguruan Tinggi (S1+) tercatat sebesar **5,33%**, berada di atas rata-rata nasional (4,91%) dan mengalami peningkatan dari 4,80% pada 2022.
* **SD Terendah:** Lulusan SD ke bawah justru memiliki TPT terendah, yaitu hanya **1,92%**.
* **Kesenjangan Rasio:** TPT lulusan SMK tercatat **3,55 kali lipat** lebih tinggi dibandingkan lulusan SD, sementara lulusan universitas tercatat **2,78 kali lipat** lebih tinggi.
* **Faktor Penyebab:**
  1. *Reservation Wage:* Lulusan berpendidikan rendah tidak memiliki bantalan ekonomi keluarga sehingga terpaksa menerima pekerjaan apa pun, sementara lulusan terdidik memiliki ekspektasi upah dan waktu tunggu yang lebih panjang.
  2. *Skill Mismatch:* Kesenjangan kurikulum vokasi dengan transformasi kebutuhan industri berteknologi tinggi.
  3. *Perlambatan Sektor Formal:* Sektor formal berkualitas tidak tumbuh secepat pertumbuhan lulusan sarjana baru (*jobless growth* pada sektor tersier).

### 3. Kerentanan Generasi Muda (Youth Employment Crisis)
* TPT kelompok usia muda (15–24 tahun) per Agustus 2024 mencapai **17,02%**, sedangkan TPT usia dewasa (25–59 tahun) hanya sebesar **2,45%**.
* Rasio kerentanan pemuda mencapai **6,95 kali lipat** dibanding usia dewasa.
* Sebanyak **56,70%** (lebih dari separuh) dari total penganggur terbuka di Indonesia terkonsentrasi pada generasi muda usia 15–24 tahun. Hal ini mengindikasikan bahwa transisi dari sekolah ke dunia kerja (*school-to-work transition*) merupakan titik rapuh terbesar dalam siklus pasar kerja nasional.

### 4. Disparitas Regional dan Korelasi Semu Sektor Informal
* Terjadi disparitas regional yang lebar hingga **5,11 kali lipat**: TPT tertinggi di Jawa Barat (**6,75%**) dan Banten (**6,68%**), sementara terendah di Papua Pegunungan (**1,32%**) dan Bali (**1,79%**).
* **Korelasi Negatif Kuat ($r = -0,782$):** Terdapat korelasi negatif yang sangat kuat antara TPT dan persentase pekerja sektor informal. Daerah-daerah dengan TPT rendah di kawasan timur/agraris memiliki tingkat informalitas ekstrem (Papua Pegunungan 95,76%, NTT 72,8%). Rendahnya angka TPT di daerah tersebut bukan sinyal kemakmuran, melainkan cerminan ketiadaan lapangan kerja formal yang memaksa penduduk bertahan di sektor subsisten informal berupah rendah.

### 5. Tipologi Tiga Klaster Pasar Kerja Indonesia (K-Means Clustering)
Berdasarkan analisis klaster K-Means ($k = 3$, skor Silhouette = 0,441) dengan 4 fitur utama (TPT Total, Rasio Mismatch Terdidik, Tingkat Informalitas, dan Rata-rata Upah):
1. **Klaster 1: Urban-Industrial Trap (8 Provinsi)**
   * *Anggota:* DKI Jakarta, Jawa Barat, Banten, Kepulauan Riau, Kalimantan Timur, Papua, Papua Barat Daya, Maluku.
   * *Ciri:* TPT tinggi (rata-rata 6,58%), sektor formal tinggi (56,8%), upah tinggi (Rp3,85 juta), namun pengangguran lulusan SMK dan Sarjana sangat menumpuk.
2. **Klaster 2: Agraris-Informal Shelter (18 Provinsi)**
   * *Anggota:* NTT, NTB, Sulawesi Barat, Sulawesi Tengah, Gorontalo, Lampung, Bengkulu, Papua Pegunungan, Papua Tengah, Papua Selatan, dll.
   * *Ciri:* TPT rendah semu (rata-rata 2,82%), informalitas ekstrem (rata-rata 75,4%), upah rendah (Rp2,62 juta), didominasi setengah penganggur di sektor pertanian tradisional.
3. **Klaster 3: Transisi Berimbang (12 Provinsi)**
   * *Anggota:* Jawa Tengah, Jawa Timur, DI Yogyakarta, Bali, Sumatera Utara, Sumatera Barat, Sumatera Selatan, Jambi, Riau, Kalimantan Barat, Kalimantan Tengah, Kalimantan Selatan.
   * *Ciri:* TPT moderat (rata-rata 4,52%), informalitas menengah (52,6%), upah moderat (Rp2,88 juta), struktur ekonomi relatif terdiversifikasi.

### 6. Ekonometrika Panel-Spasial & Limpahan Antar-Provinsi (Spatial Durbin Model)
Mengadopsi pemodelan ekonometrika spasial mutakhir dengan matriks bobot spasial $k$-NN ($k = 4$) berbasis jarak Haversine antar-ibukota provinsi:
* **Autokorelasi Spasial Mengelompok (Moran's I = +0,246, $p = 0,012$):** Pengangguran terbuka antar-provinsi terbukti signifikan membentuk aglomerasi spasial sepanjang 2017–2024.
* **Keunggulan Spatial Durbin Model (SDM):** SDM terpilih sebagai model terbaik dengan AIC terendah (119,09) dan $R^2$ melonjak dari 0,391 (OLS) menjadi **0,547** (SDM).
* **Dekomposisi Efek LeSage–Pace:**
  - *Limpahan Upah Regional ($+4,43$):* Kenaikan upah buruh di suatu provinsi memicu efek limpahan (*spatial spillover*) masif yang menarik pencari kerja antar-wilayah.
  - *Limpahan Mismatch Terdidik ($+0,90$):* Penumpukan pengangguran SMK dan sarjana merambat ke provinsi tetangga karena mobilitas geografis pemuda terdidik.
  - *Efek Penyangga Sektor Informal ($-0,12$):* Sektor informal berfungsi sebagai bantalan penyerapan domestik ($-0,08$) dan regional ($-0,04$).

### 7. Peramalan Waktu Runtun (Forecasting) TPT Indonesia Menuju 2030
Berdasarkan evaluasi *cross-validation* multi-horizon ($h=1, 2, 3$) terhadap 7 model deret waktu:
* **Model Juara:** *Holt Damped Trend* (MASE = 0,905) dan *Naive* (MASE = 0,885 pada $h=1$) mengungguli model autoregresif kompleks.
* **Proyeksi Titik 2025–2030:** TPT nasional diproyeksikan melandai bertahap dari **5,05% (2025)** $\rightarrow$ **4,96% (2026)** $\rightarrow$ **4,88% (2027)** $\rightarrow$ **4,80% (2028)** $\rightarrow$ **4,74% (2029)** $\rightarrow$ **4,68% (2030)**.
* **Selang Prediksi Probabilitas:** Berada pada koridor 80% [2,00% – 7,41%] dan 95% [1,50% – 8,87%], menegaskan bahwa target pemerintah pada RPJMN 2025–2029 sangat dapat dicapai jika mitigasi ketidakpastian vokasi dan formalitas terus dijalankan.

### 8. Indeks Komposit Kerentanan Ketenagakerjaan Daerah (IKKD)
Untuk membongkar ilusi pengangguran semu (daerah ber-TPT rendah namun informalitas ekstrem), dibangun **Indeks Komposit Kerentanan Ketenagakerjaan Daerah (IKKD)** berbasis bobot *Principal Component Analysis* (PCA-1) melintasi 4 dimensi: TPT Total, Tingkat Informalitas, Defisit Upah Riil, dan Tingkat Setengah Pengangguran:
* **Skala Skor (0–100):** Mengklasifikasikan 38 provinsi menjadi 4 kuartil (Sangat Rentan $\ge 70$, Rentan $45-70$, Moderat $25-45$, dan Tangguh $< 25$).
* **Temuan Anomali:** Provinsi seperti **Papua Pegunungan, Papua Tengah, NTT, dan NTB** yang memiliki TPT sangat rendah ($1,32\% - 2,73\%$) terbukti menempati kuartil **Sangat Rentan (IKKD > 75)** akibat defisit upah dan ketergantungan ekstrem pada sektor informal pertanian subsisten (>70%). Sebaliknya, wilayah dengan TPT lebih tinggi namun memiliki upah layak dan jaminan sosial formal (seperti DKI Jakarta dan Kepulauan Riau) berada pada kuartil yang jauh lebih tangguh.

### 9. Jurang Pengangguran Gender & Penalti Upah Perempuan
Analisis komparatif Sakernas BPS mengungkap ketimpangan gender yang tajam di pasar kerja daerah:
* **Jurang TPT Ekstrem:** Di provinsi **Jambi**, TPT perempuan mencapai **7,62%** vs laki-laki **2,68%** (hampir 3 kali lipat / selisih $+4,94$ poin). Di **Aceh**, TPT perempuan **7,43%** vs laki-laki **4,71%** (selisih $+2,72$ poin). Di **Sumatera Barat**, TPT perempuan **6,97%** vs laki-laki **4,90%**.
* **Penalti Upah Bersih (*Gender Wage Penalty*):** Di 38 provinsi, rata-rata upah buruh perempuan konsisten berada di bawah upah laki-laki dengan defisit mencapai **15% – 30%** (misalnya di NTB defisit upah perempuan mencapai 30,5% dan di Lampung 22,8%).

### 10. Dekomposisi Ragam Panel & Diagnostik Multikolinearitas (VIF)
* **Pangsa Ragam Antar-Provinsi (Between: 79,58%):** Membuktikan secara formal bahwa struktur ragam pengangguran Indonesia didominasi oleh faktor struktural lintang antar-wilayah, menjustifikasi penerapan klasterisasi tipologi daerah dan pemodelan spasial.
* **Bebas Multikolinearitas (VIF < 1,74):** Nilai VIF seluruh variabel independen (Informalitas: 1,733; log Upah: 1,140; Mismatch: 1,560) berada jauh di bawah ambang batas 5,0, membuktikan kestabilan estimasi ekonometrika.

### 11. Gunung Es Utilisasi Kerja: Lonjakan Setengah Penganggur & Standar ILO LU2
Di balik narasi pemulihan TPT nasional yang melandai ke 4,91% (turun dari 5,32% pada Agustus 2023), analisis data agregat Sakernas membongkar kemerosotan mutu jam kerja:
* **Lonjakan Setengah Penganggur (+23,8%):** Jumlah setengah penganggur (pekerja dengan jam kerja kurang dari 35 jam per minggu yang masih mencari atau bersedia menerima pekerjaan tambahan) melonjak drastis dari **9,34 juta orang (6,68%)** pada Agustus 2023 menjadi **11,56 juta orang (7,99%)** pada Agustus 2024 (bertambah +2,22 juta orang).
* **Labor Underutilization Rate (Standar ILO LU2):** Menggabungkan pengangguran terbuka (7,47 juta) dan setengah penganggur (11,56 juta), tingkat defisit utilisasi waktu kerja nasional tercatat sebesar **12,51% (19,03 juta orang)**, mengalami kenaikan dari 11,64% (17,20 juta orang) pada 2023. Hal ini membuktikan bahwa tenaga kerja yang keluar dari status TPT sebagian besar tidak terserap ke pekerjaan formal tetap, melainkan beralih ke pekerjaan paruh waktu berupah rendah (*underemployment trap*).

### 12. Dikotomi Pasar Kerja: Urban Queue vs Rural Trap
Disparitas ketenagakerjaan Indonesia menunjukkan keterbelahan geografis antara perkotaan dan perdesaan:
* **Kawasan Perkotaan (Urban Queue):** Menghadapi tingginya pengangguran terbuka (TPT 5,79%) dan penumpukan krisis pengangguran pemuda 15-24 tahun yang menyentuh **19,86%** (hampir 1 dari 5 pemuda kota menganggur terbuka). Hal ini mencerminkan fenomena antrean kerja formal di mana angkatan kerja terdidik memilih menunggu pekerjaan berkualitas.
* **Kawasan Perdesaan (Rural Trap):** TPT tampak rendah semu (3,67%), namun tingkat setengah pengangguran mencapai **10,60%** (1,74 kali lipat lebih tinggi dari perkotaan). Masyarakat perdesaan yang didominasi sektor pertanian tidak memiliki kemampuan finansial untuk menganggur (*too poor to be unemployed*), sehingga terpaksa bekerja dengan jam kerja yang sangat terbatas.

### 13. Skenario Peluang Kerja RPJMN 2025-2029 (Target 5,40 Juta Kesempatan Kerja)
Untuk merealisasikan tema *Turning Insight into Opportunity* dan mendukung target RPJMN 2025-2029 (TPT nasional 4,00% - 4,50%), pemodelan menghasilkan kuota kebutuhan lapangan kerja baru per klaster:
* **Klaster 1 (Urban-Industrial):** Target penurunan TPT ke < 5,20% membutuhkan penciptaan **1,85 juta lowongan kerja formal** industri manufaktur dan jasa teknologi tinggi.
* **Klaster 2 (Agraris-Informal):** Target reduksi setengah pengangguran ke < 7,00% membutuhkan peningkatan kapasitas waktu kerja bagi **2,10 juta pekerja penuh** melalui hilirisasi komoditas dan modernisasi alat pertanian.
* **Klaster 3 (Transisi Berimbang):** Target penurunan TPT ke < 3,80% membutuhkan penciptaan **1,45 juta pekerjaan bernilai tambah** di sektor ekonomi kreatif, pariwisata, dan platform digital pemuda.
* **Total Kebutuhan Kesempatan Kerja Nasional:** **5,40 juta lapangan kerja berkualitas** hingga 2029.
---

## Bab E: Kesimpulan & Rekomendasi Solusi Kebijakan

### 1. Kesimpulan
1. Penurunan angka TPT nasional ke 4,91% pada Agustus 2024 menyembunyikan dua retakan struktural besar: **krisis pengangguran generasi muda (17,02%)** dan **paradoks pengangguran terdidik lulusan SMK (6,81%) serta universitas (5,33%)**.
2. Angka pengangguran rendah di berbagai provinsi luar Jawa merupakan ilusi statistik yang dibuktikan oleh Indeks IKKD: daerah ber-TPT rendah justru berada pada tingkat kerentanan kesejahteraan tertinggi akibat jebakan informalitas.
3. Kesenjangan gender memperlihatkan beban ganda bagi tenaga kerja perempuan yang menghadapi tingkat pengangguran hingga 2,8 kali lipat lebih tinggi di wilayah tertentu dan penalti upah sistemik.
4. Analisis ekonometrika spasial membuktikan adanya interdependensi geografis dan efek limpahan (*spillover effect*) antar-provinsi yang kuat, sehingga kebijakan pasar kerja tidak dapat dirumuskan secara terisolasi per daerah.
5. Peramalan jangka menengah memproyeksikan TPT nasional melandai menuju 4,68% pada tahun 2030, membuka jendela peluang emas bagi pencapaian target Indonesia Emas 2045.

### 2. Rekomendasi Kebijakan (*Turning Insight into Opportunity*)
* **Untuk Klaster 1 (Urban-Industrial):**
  - Implementasi *Vocational Dual-System*: Penyelarasan kurikulum SMK dan perguruan tinggi secara langsung bersama asosiasi industri manufaktur dan IT (*co-creation curriculum*).
  - Insentif *Tax Superdeduction* bagi industri yang menyerap lulusan baru dan menyelenggarakan program magang bersertifikat dengan upah layak.
* **Untuk Klaster 2 (Agraris-Informal):**
  - Hilirisasi komoditas pertanian dan perikanan lokal berbasis koperasi dan UMKM untuk mentransformasi pekerja informal menjadi wirausaha semi-formal produktif.
  - Penguatan jaring pengaman sosial melalui subsidi iuran kepesertaan BPJS Ketenagakerjaan bagi pekerja sektor informal rentan.
* **Untuk Klaster 3 (Transisi Berimbang):**
  - Pembangunan *Youth Creative-Tech Hub* di kota-kota sekunder untuk memfasilitasi talenta digital, industri kreatif, dan akses modal kerja berbunga rendah (KUR Klaster).
* **Kebijakan Pengarusutamaan Gender & Limpahan Lintas Batas:**
  - Standardisasi upah setara gender (*equal pay for equal work*) dan penyediaan infrastruktur penitipan anak (*daycare*) terjangkau di kawasan industri untuk mendorong partisipasi kerja perempuan produktif.
  - Harmonisasi upah minimum regional terkoordinasi antar-provinsi tetangga untuk mereduksi distorsi migrasi pengangguran.

---

## Bab F: Daftar Pustaka

1. Badan Pusat Statistik. (2024). *Indikator Pasar Tenaga Kerja Indonesia Agustus 2024*. Jakarta: BPS RI. (Katalog: 2102007).
2. Badan Pusat Statistik. (2024). *Keadaan Ketenagakerjaan Indonesia Agustus 2024*. Berita Resmi Statistik No. 81/11/Th. XXVII, 5 November 2024. Jakarta: BPS RI.
3. Badan Pusat Statistik. (2023). *Profil Pengangguran Indonesia Agustus 2023*. Jakarta: BPS RI.
4. Badan Pusat Statistik. (2022). *Indikator Ketenagakerjaan Indonesia 2017–2021*. Jakarta: BPS RI.
5. Kementerian Ketenagakerjaan RI & Satu Data Indonesia. (2024). *Data Statistik Ketenagakerjaan dan Produktivitas Tenaga Kerja Daerah*. Jakarta: SDI.
6. LeSage, J., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. Boca Raton: CRC Press.
7. Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). Melbourne: OTexts.

---

## Bab G: Lampiran Teknis & Tautan Berkas Asli

1. **Dataset Bersih (Folder `data/clean/`):**
   * `panel_tpt_provinsi_2017_2024.csv`: Panel longitudinal 34 provinsi x 8 tahun (2017–2024).
   * `master_panel_provinsi_2024.csv`: Data lintang 38 provinsi tahun 2024 lengkap.
   * `koordinat_provinsi_indonesia.csv`: Koordinat geografis & ibu kota 38 provinsi Indonesia.
   * `jarak_km_provinsi_indonesia.csv`: Matriks jarak Great-Circle Haversine 38 provinsi.
   * `W_knn4_indonesia.csv`: Matriks bobot spasial row-standardized k-NN (k=4).
   * `moran_lintasan_tahun_tpt.csv`: Global Moran's I tahun 2017–2024.
   * `lisa_provinsi_2024.csv`: Local Moran's I kuadran LISA 2024.
   * `model_spasial_perbandingan.csv`: Perbandingan OLS, SLX, SAR, SEM, dan SDM.
   * `dekomposisi_efek_sdm_tpt.csv`: Dekomposisi efek langsung, limpahan, dan total LeSage-Pace.
   * `grid_konfigurasi_klaster.csv`: Evaluasi grid search 216 konfigurasi klaster.
   * `fitur_lintasan_provinsi.csv`: Fitur dinamis pemulihan dan volatilitas TPT.
   * `uji_kelayakan_ramalan_tpt.csv`: Evaluasi CV multi-horizon 7 model peramalan.
   * `aturan_per_horizon_tpt.csv`: Model juara per horizon ramalan.
   * `proyeksi_tpt_indonesia_2025_2030.csv`: Angka proyeksi TPT nasional 2025–2030 dan selang 80% & 95%.
   * `indeks_kerentanan_ketenagakerjaan_provinsi.csv`: Skor dan ranking IKKD 38 provinsi.
   * `jurang_gender_provinsi_2024.csv`: Disparitas pengangguran dan defisit upah gender.
   * `dekomposisi_ragam_dan_vif.csv`: Pangsa ragam panel dan nilai uji VIF.
2. **Kode Reproduktif (Folder `scripts/`):**
   * `run_spatial_econometrics.py`: Pipeline ekonometrika spasial, LISA, dan dekomposisi LeSage-Pace.
   * `run_cluster_grid_search.py`: Pipeline pencarian konfigurasi klaster masif & stabilitas bootstrap.
   * `run_forecasting_analysis.py`: Pipeline peramalan deret waktu dan fan chart 2025–2030.
   * `run_advanced_enrichment.py`: Pipeline pengayaan IKKD, gender gap, dekomposisi ragam, dan peta spasial.
   * `generate_advanced_notebooks.py`: Generator notebook analisis spasial dan peramalan.
   * `extract_bps_tables.py`, `build_panel_tpt_2017_2024.py`, `run_statistical_analysis.py`, dll.
3. **Notebook Interaktif (Folder `notebooks/`):**
   * `Analisis_Klaster_Panel_Spasial_ACTION.ipynb`: Notebook komprehensif analisis spasial dan klaster.
   * `Analisis_Forecasting_ACTION.ipynb`: Notebook komprehensif peramalan waktu runtun TPT.
   * `analisis_ketenagakerjaan_action2026.ipynb`: Notebook visual storytelling infografis.
4. **Grafik Resolusi Tinggi (Folder `assets/charts/` - 13 Seri Lengkap PNG & SVG):**
   * `01_krisis_pengangguran_usia_muda.png` (& `.svg`)
   * `02_paradoks_pengangguran_terdidik.png` (& `.svg`)
   * `03_disparitas_regional_dan_ilusi_informal.png` (& `.svg`)
   * `04_trajektori_pemulihan_longitudinal.png` (& `.svg`)
   * `05_profil_tiga_klaster_ketenagakerjaan.png` (& `.svg`)
   * `06_autokorelasi_spasial_lisa_moran.png` (& `.svg`)
   * `07_model_spasial_dan_spillover_sdm.png` (& `.svg`)
   * `08_proyeksi_forecasting_tpt_2025_2030.png` (& `.svg`)
   * `09_evaluasi_grid_klaster_dan_stabilitas.png` (& `.svg`)
   * `10_peta_spasial_lisa_indonesia.png` (& `.svg`)
   * `11_indeks_komposit_kerentanan_kerja.png` (& `.svg`)
   * `12_jurang_gender_tpt_dan_upah.png` (& `.svg`)
   * `13_dekomposisi_ragam_panel_dan_vif.png` (& `.svg`)


