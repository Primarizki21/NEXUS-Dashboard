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

---

## Bab E: Kesimpulan & Rekomendasi Solusi Kebijakan

### 1. Kesimpulan
1. Penurunan angka TPT nasional ke 4,91% pada Agustus 2024 menyembunyikan dua retakan struktural besar: **krisis pengangguran generasi muda (17,02%)** dan **paradoks pengangguran terdidik lulusan SMK (6,81%) serta universitas (5,33%)**.
2. Angka pengangguran rendah di berbagai provinsi luar Jawa merupakan ilusi statistik yang didorong oleh tingginya penyerapan sektor informal rentan (*informal shelter*), bukan lapangan kerja berkualitas.
3. Kebijakan ketenagakerjaan nasional memerlukan pergeseran dari pendekatan seragam (*one-size-fits-all*) menuju strategi diferensiasi berbasis klaster daerah.

### 2. Rekomendasi Kebijakan (*Turning Insight into Opportunity*)
* **Untuk Klaster 1 (Urban-Industrial):**
  - Implementasi *Vocational Dual-System*: Penyelarasan kurikulum SMK dan perguruan tinggi secara langsung bersama asosiasi industri manufaktur dan IT (*co-creation curriculum*).
  - Insentif *Tax Superdeduction* bagi industri yang menyerap lulusan baru dan menyelenggarakan program magang bersertifikat dengan upah layak.
* **Untuk Klaster 2 (Agraris-Informal):**
  - Hilirisasi komoditas pertanian dan perikanan lokal berbasis koperasi dan UMKM untuk mentransformasi pekerja informal menjadi wirausaha semi-formal produktif.
  - Penguatan jaring pengaman sosial melalui subsidi iuran kepesertaan BPJS Ketenagakerjaan bagi pekerja sektor informal rentan.
* **Untuk Klaster 3 (Transisi Berimbang):**
  - Pembangunan *Youth Creative-Tech Hub* di kota-kota sekunder untuk memfasilitasi talenta digital, industri kreatif, dan akses modal kerja berbunga rendah (KUR Klaster).

---

## Bab F: Daftar Pustaka

1. Badan Pusat Statistik. (2024). *Indikator Pasar Tenaga Kerja Indonesia Agustus 2024*. Jakarta: BPS RI. (Katalog: 2102007).
2. Badan Pusat Statistik. (2024). *Keadaan Ketenagakerjaan Indonesia Agustus 2024*. Berita Resmi Statistik No. 81/11/Th. XXVII, 5 November 2024. Jakarta: BPS RI.
3. Badan Pusat Statistik. (2023). *Profil Pengangguran Indonesia Agustus 2023*. Jakarta: BPS RI.
4. Badan Pusat Statistik. (2022). *Indikator Ketenagakerjaan Indonesia 2017–2021*. Jakarta: BPS RI.
5. Kementerian Ketenagakerjaan RI & Satu Data Indonesia. (2024). *Data Statistik Ketenagakerjaan dan Produktivitas Tenaga Kerja Daerah*. Jakarta: SDI.

---

## Bab G: Lampiran Teknis & Tautan Berkas Asli

1. **Dataset Bersih (Folder `data/clean/`):**
   * `panel_tpt_provinsi_2017_2024.csv`: Panel longitudinal 34 provinsi x 8 tahun (2017–2024).
   * `master_panel_provinsi_2024.csv`: Data lintang 38 provinsi tahun 2024 lengkap (TPT, pendidikan, formal/informal, upah, underemployment).
   * `hasil_klaster_provinsi.csv`: Hasil segmentasi 3 klaster provinsi berbasis K-Means.
   * `tpt_nasional_pendidikan_detail_2022_2024.csv`: Rincian 6 jenjang pendidikan nasional.
   * `tpt_kelompok_umur_youth_adult.csv`: Komparasi umur muda vs dewasa.
2. **Kode Reproduktif (Folder `scripts/`):**
   * `extract_bps_tables.py`: Ekstraksi presisi tabel lampiran PDF BPS.
   * `build_panel_tpt_2017_2024.py`: Pembentukan panel seimbang longitudinal 2017–2024.
   * `run_statistical_analysis.py`: Script kalkulasi statistik deskriptif, korelasi, dan klasterisasi.
   * `populate_template_masalah.py`: Generator template dokumen kerja tim desain.
3. **Tautan Berkas Cloud Storage:**
   * *(Tautan Google Drive penyimpanan berkas asli, font, dan kode program akan disematkan di sini saat pengumpulan final sesuai pedoman).*
