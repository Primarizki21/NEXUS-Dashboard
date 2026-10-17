"""
Generates the complete Official Support Report (Laporan Pendukung Karya Infografis)
for ACTION 2026 covering Bab A through Bab G.
Outputs:
1. docs/LAPORAN_LENGKAP_INFOGRAFIS_ACTION2026.md
2. docs/laporan_pendukung_infografis_action2026.docx

Strictly compliant with:
- BPS Sakernas 2017-2024 official data
- Antislop R-02 (Zero em dashes)
- ACTION 2026 guidebook format (Bab A-G)
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / "docs"

OUTPUT_MD = DOCS_DIR / "LAPORAN_LENGKAP_INFOGRAFIS_ACTION2026.md"
OUTPUT_DOCX = DOCS_DIR / "laporan_pendukung_infografis_action2026.docx"

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def build_full_report_content():
    return {
        "title": "LAPORAN LENGKAP PENDUKUNG KARYA INFOGRAFIS",
        "competition": "ACTION 2026 (Annual Competition of Data Science 2026)",
        "organizer": "Himpunan Mahasiswa Program Studi Sains Data (HMP Sains Data), Universitas Negeri Surabaya",
        "subtheme": "Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja",
        "team_name": "[Nama Tim Peserta]",
        "work_title": "Paradoks Ijazah di Negeri Zamrud: Menyingkap Peta Retak Pengangguran Terbuka dan Merajut Peluang Kerja Inklusif Indonesia",
        
        # BAB A
        "bab_a_title": "Bab A: Latar Belakang Masalah",
        "bab_a_paragraphs": [
            "Perekonomian Indonesia saat ini berada pada persimpangan sejarah yang krusial. Momentum jendela bonus demografi, di mana proporsi penduduk usia produktif melampaui penduduk non-produktif, diproyeksikan mencapai puncaknya pada rentang 2025 sampai 2035 sebelum akhirnya mulai menua menuju visi Indonesia Emas 2045. Dalam wacana publik, penurunan angka Tingkat Pengangguran Terbuka (TPT) nasional menjadi 4,91% pada Agustus 2024 (turun dari 5,32% pada Agustus 2023 dan telah berada di bawah tingkat pra-pandemi 2019 sebesar 5,23%) kerap dirayakan sebagai sinyal pemulihan ekonomi penuh. Namun, pembacaan data statistik makro tunggal berisiko mengaburkan kerentanan mendasar di dalam struktur ketenagakerjaan Indonesia.",
            "Bedah data mikro dan agregat Survei Angkatan Kerja Nasional (Sakernas) Badan Pusat Statistik (BPS) mengungkap empat retakan sistemik yang mengancam pemerataan kesempatan kerja dan produktivitas nasional:",
            "1. Krisis Ketenagakerjaan Generasi Muda (Youth Unemployment Crisis): Sebanyak 56,70% (lebih dari satu dari setiap dua penganggur di Indonesia) terkonsentrasi pada kelompok umur muda 15-24 tahun. TPT pemuda mencapai 17,02%, atau 6,95 kali lipat lebih tinggi dibandingkan TPT usia dewasa 25-59 tahun (2,45%). Transisi dari bangku sekolah ke dunia kerja (school-to-work transition) mengalami kemacetan parah yang berisiko meninggalkan efek luka permanen (scarring effect) pada kapasitas penghasilan masa depan angkatan kerja muda.",
            "2. Paradoks Pengangguran Terdidik (The Educated Unemployment Paradox): Bertentangan dengan teori modal manusia konvensional, lulusan Sekolah Menengah Kejuruan (SMK) yang secara kurikulum didesain siap kerja justru konsisten mencatatkan TPT tertinggi di Indonesia sebesar 6,81%, disusul SMA Umum (6,69%) dan Perguruan Tinggi/Universitas (5,33%). Sebaliknya, penduduk berpendidikan SD ke bawah mencatatkan TPT terendah (1,92%). Fenomena ini dipicu oleh ketiadaan jaring pengaman finansial bagi pekerja berpendidikan rendah sehingga mereka terpaksa bekerja di sektor apa saja, serta diperparah oleh stagnasi kapasitas penyerapan sektor industri manufaktur formal yang tertahan di angka 13,83%.",
            "3. Disparitas Regional Ekstrem dan Ilusi Pengangguran Semu: Terdapat jurang ketimpangan TPT hingga 5,11 kali lipat antar-provinsi di Indonesia, berkisar dari 6,75% di Jawa Barat hingga 1,32% di Papua Pegunungan. Analisis spasial membuktikan korelasi negatif yang sangat kuat (r = -0,782) antara TPT dan proporsi pekerja informal. Daerah dengan angka TPT terendah di kawasan Indonesia Timur bukanlah episentrum kemakmuran, melainkan wilayah dengan tingkat informalitas ekstrem (>75%) di mana penduduk miskin tidak mampu menganggur (too poor to be unemployed) dan terperangkap dalam pekerjaan subsisten nir-upah layak.",
            "4. Fenomena Gunung Es Utilisasi Kerja (Underutilization Iceberg): Di balik penurunan TPT, jumlah setengah penganggur (underemployed) yang bekerja kurang dari 35 jam seminggu dan masih membutuhkan pekerjaan tambahan justru melonjak drastis +23,8% dalam setahun, dari 9,34 juta orang menjadi 11,56 juta orang (7,99% dari total pekerja). Berdasarkan standar International Labour Organization (ILO LU2), defisit utilisasi waktu kerja nasional sesungguhnya mencapai 12,51% atau mencakup 19,03 juta orang.",
            "Berdasarkan persoalan di atas, karya infografis ini dihadirkan untuk mendemokratisasi dan mentransformasikan kompleksitas data sains ketenagakerjaan menjadi narasi visual yang tajam, edukatif, dan solutif. Dengan prinsip 'Turning Insight into Opportunity', karya ini mengusung peta jalan intervensi berbasis klaster wilayah guna mendukung pencapaian target Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2025-2029."
        ],

        # BAB B
        "bab_b_title": "Bab B: Tujuan Penulisan dan Karya",
        "bab_b_paragraphs": [
            "Tujuan utama dari penyusunan karya analisis dan infografis ini meliputi:",
            "1. Menyingkap Realitas Struktural Pasar Kerja: Membongkar mitos bahwa penurunan TPT semata mencerminkan peningkatan kesejahteraan, dengan memvisualisasikan fenomena gunung es setengah pengangguran (11,56 juta orang) dan dikotomi perkotaan-perdesaan.",
            "2. Menganalisis Faktor Determinan Paradoks Vokasi dan Kerentanan Pemuda: Mengidentifikasi transmisi struktural yang menyebabkan lulusan SMK Kejuruan (6,81%) dan kelompok usia muda (17,02%) menghadapi hambatan serapan kerja formal tertinggi di Indonesia.",
            "3. Memetakan Pola Interdependensi Spasial Regional: Mengelompokkan 38 provinsi di Indonesia ke dalam 3 tipologi pasar kerja teruji melalui algoritma K-Means dan mengevaluasi dampak limpahan geografis (spatial spillover) mobilitas tenaga kerja.",
            "4. Merumuskan Rekomendasi Kebijakan yang Terukur dan Aplikatif: Menyusun matriks kebutuhan penciptaan 5,40 juta kesempatan kerja berkualitas menuju 2029 yang terbagi secara proporsional ke dalam tiga klaster wilayah, guna mengonversi pekerja paruh waktu rentan menjadi pekerja penuh waktu produktif."
        ],

        # BAB C
        "bab_c_title": "Bab C: Sumber & Prosedur Pengolahan Data",
        "bab_c_subsections": [
            {
                "subtitle": "1. Sumber Data Resmi",
                "content": "Karya ini mengandalkan 100% data resmi yang dipublikasikan oleh Badan Pusat Statistik (BPS) Republik Indonesia dan Satu Data Indonesia (data.go.id):\n"
                           "• Publikasi Indikator Pasar Tenaga Kerja Indonesia Agustus 2024 (Katalog BPS: 2102007, rilis Desember 2024): Lampiran 13 (Pekerja Paruh Waktu), Lampiran 16 (Pekerja Formal/Informal), Lampiran 17 (TPT Provinsi & Gender), Lampiran 18 (TPT Pendidikan), Lampiran 20 (Setengah Pengangguran), Lampiran 26 (Upah Buruh Bulanan), serta Tabel 5 & 6 Bab 3.\n"
                           "• Berita Resmi Statistik (BRS) No. 81/11/Th. XXVII, 5 November 2024: Keadaan Ketenagakerjaan Indonesia Agustus 2024.\n"
                           "• Publikasi Indikator Ketenagakerjaan 2017-2021 & Profil Pengangguran 2022-2023: Untuk deret panel longitudinal TPT tahunan.\n"
                           "• Data Geospasial: Koordinat lintang dan bujur 38 ibukota provinsi Indonesia untuk penghitungan jarak Great-Circle Haversine dan matriks bobot spasial."
            },
            {
                "subtitle": "2. Pipeline Pengolahan dan Pembersihan Data",
                "content": "Pengolahan data dilakukan menggunakan pipeline Python yang sepenuhnya reproduktif (reproducible scripts):\n"
                           "• Ekstraksi Presisi PDF: Skrip scripts/extract_bps_tables.py memanfaatkan pustaka pdfplumber dengan penyaringan koordinat font untuk mengekstrak tabel tanpa terganggu tanda air halaman.\n"
                           "• Penyelarasan Disparitas Wilayah (34 vs 38 Provinsi): Analisis panel dinamis 2017-2024 menggunakan panel seimbang 34 provinsi konsisten. Analisis mutakhir potret 2024 mencakup keseluruhan 38 provinsi di Indonesia.\n"
                           "• Standarisasi Nilai: Pembersihan karakter koma desimal Indonesia menjadi float standar internasional dan audit integritas (zero missing values) pada folder data/clean/."
            }
        ],

        # BAB D
        "bab_d_title": "Bab D: Data Deskripsi dan Teknis Karya",
        "bab_d_sections": [
            {
                "head": "1. Potret Makro: Pemulihan TPT dan Realitas Angkatan Kerja",
                "text": "Pada Agustus 2024, angkatan kerja Indonesia mencapai 152,11 juta orang, bertambah 4,79 juta orang dibanding Agustus 2023. Dari jumlah tersebut, penduduk bekerja mencapai 144,64 juta orang (95,09%) dan pengangguran terbuka tercatat 7,47 juta orang (4,91%). Tingkat Partisipasi Angkatan Kerja (TPAK) tercatat naik menjadi 70,06%."
            },
            {
                "head": "2. Paradoks Pengangguran Terdidik (Educated Unemployment Paradox)",
                "text": "Data Sakernas mencatat anomali struktural menurut tingkat pendidikan:\n"
                        "• SMK Kejuruan: TPT 6,81% (Tertinggi nasional, 3,55 kali lipat lulusan SD).\n"
                        "• SMA Umum: TPT 6,69%.\n"
                        "• Universitas (S1+): TPT 5,33% (Mengalami kenaikan dari 4,80% pada 2022).\n"
                        "• Diploma I/II/III: TPT 4,27%.\n"
                        "• SMP: TPT 4,10%.\n"
                        "• SD ke Bawah: TPT 1,92% (Terendah).\n"
                        "Lulusan pendidikan menengah (SMA dan SMK) mendominasi 55,37% dari total penganggur terbuka di Indonesia. Fenomena ini dipicu oleh keterbatasan penciptaan kerja di sektor industri pengolahan/pabrik yang stagnan di angka 13,83% penyerapan tenaga kerja nasional (2023 vs 2024)."
            },
            {
                "head": "3. Kerentanan Generasi Muda (Youth Employment Crisis)",
                "text": "Kelompok usia muda (15-24 tahun) mengalami TPT sebesar 17,02%, berbanding terbalik dengan usia dewasa (25-59 tahun) yang hanya 2,45% (rasio kerentanan 6,95 kali lipat). Sebanyak 56,70% dari seluruh penganggur di Indonesia adalah pemuda. Lamanya masa transisi dari sekolah ke dunia kerja dan maraknya sistem kerja temporer tanpa kepastian karir menjadi penghambat utama kemandirian ekonomi generasi muda."
            },
            {
                "head": "4. Disparitas Regional dan Mitos TPT Rendah",
                "text": "Disparitas TPT antar-provinsi mencapai rentang 5,11 kali lipat. Jawa Barat mencatat TPT tertinggi (6,75%) disusul Banten (6,68%), Papua Barat Daya (6,48%), Papua (6,48%), dan Kepulauan Riau (6,39%). Sebaliknya, TPT terendah berada di Papua Pegunungan (1,32%), Bali (1,79%), Sulawesi Barat (2,68%), NTB (2,73%), dan Papua Tengah (2,75%).\n"
                        "Korelasi negatif yang sangat kuat antara TPT dan pekerja informal (r = -0,782) serta korelasi positif dengan rata-rata upah (r = +0,641) membuktikan bahwa TPT rendah di provinsi timur merupakan cerminan ilusi pengangguran semu. Di daerah tersebut, informalitas mencapai 70% sampai 95,76%, di mana ketiadaan kesempatan kerja formal memaksa masyarakat bekerja paruh waktu atau subsisten."
            },
            {
                "head": "5. Gunung Es Utilisasi Kerja: Lonjakan Setengah Penganggur",
                "text": "Penurunan TPT ke 4,91% menutupi kemerosotan kualitas jam kerja. Jumlah setengah penganggur (pekerja jam rendah <35 jam seminggu yang masih membutuhkan kerja tambahan) melonjak drastis +23,8% dalam setahun, bertambah dari 9,34 juta orang (6,68%) pada 2023 menjadi 11,56 juta orang (7,99%) pada 2024. Mengacu standar ILO LU2, defisit utilisasi waktu kerja nasional berada pada level 12,51% atau mencakup 19,03 juta orang angkatan kerja."
            },
            {
                "head": "6. Dikotomi Dua Wajah: Antrean Kota vs Perangkap Desa",
                "text": "Pasar kerja terbelah tajam secara geografis:\n"
                        "• Kawasan Perkotaan (Urban Queue): TPT mencapai 5,79% dan TPT usia muda menembus 19,86% (hampir 1 dari 5 pemuda kota menganggur). Karakteristik terdidik dan keberadaan tabungan keluarga memfasilitasi masa tunggu pencarian kerja formal.\n"
                        "• Kawasan Perdesaan (Rural Trap): TPT tampak rendah (3,67%), namun tingkat setengah pengangguran mencapai 10,60% (1,74 kali lipat lebih tinggi dari perkotaan). Sebanyak 6,46 juta dari 11,56 juta setengah penganggur nasional berada di pedesaan, terjebak dalam pekerjaan pertanian paruh waktu."
            },
            {
                "head": "7. Tipologi Tiga Klaster Pasar Kerja Indonesia (K-Means, k=3)",
                "text": "Berdasarkan evaluasi grid search 216 kombinasi dan uji stabilitas bootstrap (skor Silhouette = 0,441; ARI = 1,000), 38 provinsi terkelompok menjadi 3 klaster strategis:\n"
                        "• Klaster 1: Urban-Industrial Trap (8 Provinsi: DKI Jakarta, Jawa Barat, Banten, Kepulauan Riau, Kalimantan Timur, Papua, Papua Barat Daya, Maluku). Karakteristik: TPT tinggi (rata-rata 6,58%), sektor formal tinggi (56,8%), upah rata-rata tinggi (Rp3,85 juta), namun pengangguran SMK dan sarjana menumpuk.\n"
                        "• Klaster 2: Agraris-Informal Shelter (18 Provinsi: NTT, NTB, Sulbar, Sulteng, Gorontalo, Lampung, Bengkulu, Papua Pegunungan, Papua Tengah, Papua Selatan, dll.). Karakteristik: TPT rendah semu (rata-rata 2,82%), informalitas sangat tinggi (rata-rata 75,4%), upah rendah (Rp2,62 juta), didominasi setengah penganggur pertanian subsisten.\n"
                        "• Klaster 3: Transisi Berimbang (12 Provinsi: Jawa Tengah, Jawa Timur, DI Yogyakarta, Bali, Sumatera Utara, Sumatera Barat, Sumatera Selatan, Jambi, Riau, Kalbar, Kalteng, Kalsel). Karakteristik: TPT moderat (rata-rata 4,52%), struktur kerja seimbang antara jasa, industri kreatif, dan perdagangan."
            },
            {
                "head": "8. Ekonometrika Spasial dan Efek Limpahan Migrasi Tenaga Kerja",
                "text": "Uji autokorelasi spasial global membuktikan pengelompokan geografis TPT yang signifikan sepanjang 2017-2024 (Moran's I = +0,246, p = 0,012). Melalui Spatial Durbin Model (SDM, AIC = 119,09, Pseudo-R2 = 0,547), terungkap dekomposisi efek LeSage-Pace:\n"
                        "• Efek Limpahan Upah (+4,43): Kenaikan upah buruh di pusat industri memicu limpahan migrasi pencari kerja antar-wilayah tetangga sehingga meningkatkan konsentrasi pencari kerja di pusat urban.\n"
                        "• Efek Limpahan Mismatch (+0,90): Pengangguran terdidik merambat ke provinsi penyangga akibat mobilitas lulusan vokasi dan perguruan tinggi."
            },
            {
                "head": "9. Peramalan Deret Waktu TPT Indonesia Menuju 2030",
                "text": "Berdasarkan cross-validation multi-horizon (h=1, 2, 3), model Holt Damped Trend terpilih sebagai model terbaik (MASE = 0,905). TPT nasional diproyeksikan melandai bertahap dari 5,05% (2025) menuju 4,68% pada 2030, berada pada koridor pencapaian target RPJMN 2025-2029 (4,00% - 4,50%)."
            },
            {
                "head": "10. Spesifikasi Desain dan Alokasi Komposisi Poster A3",
                "text": "Untuk memastikan keterbacaan optimal pada ukuran cetak A3 Portrait (300 dpi, batas pandang 1-2 meter), karya infografis menyaring temuan secara ketat menjadi empat pilar visual:\n"
                        "1. Chart 1 (Hero Hook Atas): Ranked Split-Bar Chart TPT Pemuda (17,02%) vs Dewasa (2,45%).\n"
                        "2. Chart 2 (Tengah Kiri): Tangga Horisontal Paradoks Pengangguran Terdidik (SD 1,92% s.d. SMK 6,81%).\n"
                        "3. Chart 3 (Tengah Kanan): Waterfall Gunung Es Utilisasi Kerja (TPT 4,91% vs Setengah Penganggur 7,99% vs LU2 12,51%).\n"
                        "4. Chart 4 (Bawah Kiri): Peta Koroplet Indonesia 3 Klaster Wilayah.\n"
                        "5. Elemen Pendukung: Stat Callout tipografi raksasa (6,95x Lipat, 56,7% Pemuda, +23,8% Lonjakan Setengah Penganggur), Tabel Komparasi Bersih Kota vs Desa, dan Matriks Solusi 3 Kolom."
            }
        ],

        # BAB E
        "bab_e_title": "Bab E: Kesimpulan dan Rekomendasi Solusi Kebijakan",
        "bab_e_conclusions": [
            "1. Penurunan angka TPT nasional ke level 4,91% menutupi dua krisis struktural utama: lonjakan setengah pengangguran paruh waktu (+23,8% hingga mencapai 11,56 juta orang) dan kerentanan ekstrem generasi muda yang mencakup 56,70% dari seluruh penganggur di Indonesia.",
            "2. Paradoks pengangguran terdidik berakar dari disonansi antara pasokan lulusan vokasi (SMK 6,81%) dengan daya serap industri manufaktur formal yang mengalami stagnasi penyerapan di angka 13,83%.",
            "3. Angka pengangguran rendah di provinsi timur dan perdesaan merupakan ilusi pengangguran semu (korelasi informalitas r = -0,782), di mana ketiadaan lapangan kerja formal memaksa masyarakat bekerja di sektor informal berupah minim.",
            "4. Pola pengangguran terbukti memiliki interdependensi spasial (Moran's I = +0,246) dengan efek limpahan upah yang kuat (+4,43), menegaskan perlunya kebijakan ketenagakerjaan berbasis klaster wilayah yang terkoordinasi lintas batas administratif."
        ],
        "bab_e_policies": [
            "Rekomendasi Kebijakan 'Turning Insight into Opportunity' (Target 5,40 Juta Kesempatan Kerja Berkualitas Menuju 2029):",
            "1. Klaster 1: Urban-Industrial Trap (Target 1,85 Juta Lapangan Kerja Formal)\n"
            "   • Revitalisasi Vocational Dual-System: Standardisasi kurikulum SMK dan perguruan tinggi yang dirancang bersama asosiasi industri manufaktur, otomotif, dan teknologi informasi.\n"
            "   • Insentif Pajak Superdeduction: Fasilitas pengurangan pajak penghasilan hingga 200% bagi korporasi yang menyerap lulusan baru dan menyelenggarakan program magang bersertifikat dengan upah layak.\n"
            "   • Jembatan Transisi Karir Pemuda: Pembentukan bursa kerja terintegrasi (National Youth Employment Portal) untuk mereduksi durasi tunggu pencarian kerja.",
            "2. Klaster 2: Agraris-Informal Shelter (Target 2,10 Juta Peningkatan Jam Kerja Penuh)\n"
            "   • Hilirisasi Komoditas Pertanian dan Maritim Lokal: Pembangunan sentra pengolahan pascapanen berbasis koperasi tani untuk mengonversi setengah penganggur menjadi pekerja industri pengolahan desa berkala penuh waktu.\n"
            "   • Perlindungan Jamsostek bagi Pekerja Rentan: Subsidi iuran program Jaminan Kecelakaan Kerja (JKK) dan Jaminan Kematian (JKM) BPJS Ketenagakerjaan bagi petani gurem dan pekerja informal perdesaan.\n"
            "   • Program Formalisasi Bertahap UMKM: Penyederhanaan legalitas usaha dan pendampingan akses pasar digital bagi usaha mikro subsisten.",
            "3. Klaster 3: Transisi Berimbang (Target 1,45 Juta Pekerjaan Bernilai Tambah)\n"
            "   • Pembangunan Youth Creative-Tech Hub di Kota Sekunder: Pusat inkubasi ekonomi kreatif, animasi, perangkat lunak, dan agroteknologi bagi talenta muda daerah.\n"
            "   • Pembiayaan KUR Klaster Produktif: Penyaluran Kredit Usaha Rakyat (KUR) berbunga rendah tanpa agunan tambahan untuk kelompok wirausaha muda terdidik.\n"
            "4. Kebijakan Pengarusutamaan Gender dan Tata Kelola Lintas Wilayah\n"
            "   • Harmonisasi Upah Minimum Terkoordinasi: Penyelarasan formulasi UMR antar-daerah tetangga guna memitigasi distorsi migrasi tenaga kerja yang membebani kota-kota industri.\n"
            "   • Penutupan Jurang Gender (Gender Pay Gap): Penegakan regulasi upah setara (equal pay for equal work) serta penyediaan fasilitas tempat penitipan anak (daycare) ramah keluarga di kawasan industri."
        ],

        # BAB F
        "bab_f_title": "Bab F: Daftar Pustaka",
        "bab_f_items": [
            "Badan Pusat Statistik. (2024). Indikator Pasar Tenaga Kerja Indonesia Agustus 2024. Jakarta: BPS RI. (Katalog BPS: 2102007).",
            "Badan Pusat Statistik. (2024). Keadaan Ketenagakerjaan Indonesia Agustus 2024. Berita Resmi Statistik No. 81/11/Th. XXVII, 5 November 2024. Jakarta: BPS RI.",
            "Badan Pusat Statistik. (2023). Profil Pengangguran Indonesia Agustus 2023. Jakarta: BPS RI.",
            "Badan Pusat Statistik. (2022). Indikator Ketenagakerjaan Indonesia 2017-2021. Jakarta: BPS RI.",
            "Kementerian PPN/Bappenas. (2024). Rancangan Awal Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2025-2029: Sasaran dan Arah Kebijakan Ketenagakerjaan Nasional. Jakarta: Kementerian PPN/Bappenas.",
            "International Labour Organization. (2023). Resolution concerning statistics of work, employment and labour underutilization. Geneva: ILO.",
            "LeSage, J. P., & Pace, R. K. (2009). Introduction to Spatial Econometrics. Boca Raton: CRC Press Taylor & Francis Group.",
            "Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice (3rd ed.). Melbourne: OTexts.",
            "Anselin, L. (1995). Local Indicators of Spatial Association: LISA. Geographical Analysis, 27(2), 93-115."
        ],

        # BAB G
        "bab_g_title": "Bab G: Lampiran Teknis & Tautan Berkas",
        "bab_g_tables": [
            {
                "title": "Tabel G1: Inventaris Dataset Bersih Resmi (Folder data/clean/)",
                "headers": ["Nama File Dataset", "Cakupan Observasi", "Variabel Kunci"],
                "rows": [
                    ["master_panel_provinsi_2024.csv", "38 Provinsi (Ags 2024)", "TPT, Informal, Upah, Setengah Penganggur, Mismatch"],
                    ["panel_tpt_provinsi_2017_2024.csv", "34 Provinsi x 8 Tahun (272 obs)", "Deret waktu TPT longitudinal pra & pasca pandemi"],
                    ["indikator_utilisasi_tenaga_kerja_nasional.csv", "Nasional (2023-2024)", "TPT (LU1), Setengah Pengangguran, LU2, Jam Kerja"],
                    ["dikotomi_urban_rural_ketenagakerjaan_2024.csv", "Perkotaan vs Perdesaan (2024)", "TPT Kota/Desa, Setengah Penganggur, TPT Pemuda"],
                    ["hasil_klaster_provinsi.csv", "38 Provinsi (2024)", "Label Klaster (1, 2, 3), Koordinat PCA, Jarak Centroid"],
                    ["W_knn4_indonesia.csv", "Matriks 38 x 38", "Bobot spasial k-NN (k=4) row-standardized"],
                    ["model_spasial_perbandingan.csv", "5 Model (OLS, SLX, SAR, SEM, SDM)", "Log-Likelihood, AIC, R2, Koefisien Spasial"],
                    ["proyeksi_tpt_indonesia_2025_2030.csv", "Tahunan (2025-2030)", "Titik Proyeksi, Selang Prediksi 80% & 95%"]
                ]
            },
            {
                "title": "Tabel G2: Repositori Kode Analisis Reproduktif (Folder scripts/)",
                "headers": ["Skrip Python", "Tujuan Analisis", "Keluaran Utama"],
                "rows": [
                    ["extract_bps_tables.py", "Ekstraksi PDF Sakernas BPS", "Tabel bersih TPT, Upah, Formal, Pendidikan"],
                    ["run_statistical_analysis.py", "EDA & Matriks Korelasi", "Korelasi Informal r=-0,782, Disparitas Wilayah"],
                    ["run_spatial_econometrics.py", "Moran's I, LISA, SDM", "Peta LISA, Dekomposisi Efek LeSage-Pace"],
                    ["run_cluster_grid_search.py", "Grid Search Klaster & Bootstrap", "Konfigurasi k=3 optimum (Silhouette=0,441)"],
                    ["run_forecasting_analysis.py", "Cross-Validation Deret Waktu", "Holt Damped Trend (MASE=0,905), Fan Chart"],
                    ["extract_underemployment_urban_rural.py", "Kalkulasi Utilisasi & Urban-Rural", "Dataset LU2 & Dikotomi Kota-Desa 2024"],
                    ["generate_infographic_enrichment_charts.py", "Pembuatan Chart Infografis", "15 Chart PNG & SVG resolusi 300 dpi"]
                ]
            }
        ]
    }

def generate_full_markdown(c):
    lines = []
    lines.append(f"# {c['title']}")
    lines.append(f"### {c['competition']}")
    lines.append(f"**Penyelenggara:** {c['organizer']}")
    lines.append(f"**Subtema:** {c['subtheme']}")
    lines.append(f"**Nama Tim:** {c['team_name']}")
    lines.append(f"**Judul Karya:** “{c['work_title']}”\n")
    lines.append("---\n")

    # Bab A
    lines.append(f"## {c['bab_a_title']}\n")
    for p in c['bab_a_paragraphs']:
        lines.append(f"{p}\n")
    lines.append("---\n")

    # Bab B
    lines.append(f"## {c['bab_b_title']}\n")
    for p in c['bab_b_paragraphs']:
        lines.append(f"{p}\n")
    lines.append("---\n")

    # Bab C
    lines.append(f"## {c['bab_c_title']}\n")
    for sub in c['bab_c_subsections']:
        lines.append(f"### {sub['subtitle']}\n")
        lines.append(f"{sub['content']}\n")
    lines.append("---\n")

    # Bab D
    lines.append(f"## {c['bab_d_title']}\n")
    for sec in c['bab_d_sections']:
        lines.append(f"### {sec['head']}\n")
        lines.append(f"{sec['text']}\n")
    lines.append("---\n")

    # Bab E
    lines.append(f"## {c['bab_e_title']}\n")
    lines.append("### 1. Kesimpulan Temuan Data\n")
    for con in c['bab_e_conclusions']:
        lines.append(f"{con}\n")
    lines.append("### 2. Rekomendasi Solusi Kebijakan Terukur\n")
    for pol in c['bab_e_policies']:
        lines.append(f"{pol}\n")
    lines.append("---\n")

    # Bab F
    lines.append(f"## {c['bab_f_title']}\n")
    for i, ref in enumerate(c['bab_f_items'], 1):
        lines.append(f"{i}. {ref}")
    lines.append("\n---\n")

    # Bab G
    lines.append(f"## {c['bab_g_title']}\n")
    for tbl in c['bab_g_tables']:
        lines.append(f"### {tbl['title']}\n")
        lines.append(f"| {' | '.join(tbl['headers'])} |")
        lines.append(f"|{'|'.join([':---' if i==0 else ':---:' if i==1 else '---' for i in range(len(tbl['headers']))])}|")
        for r in tbl['rows']:
            lines.append(f"| {' | '.join(r)} |")
        lines.append("\n")

    lines.append("### Arsip Kode & File Desain Asli\n")
    lines.append("Seluruh berkas mentah kode analisis, notebook Jupyter, data tabel BPS, dan aset grafik resolusi tinggi (PNG & SVG 300 dpi) tersimpan pada repositori proyek lokal dan siap diunggah ke tautan Google Drive publik untuk penilaian tahap penyisihan dan final.")
    return "\n".join(lines)

def generate_full_docx(c):
    doc = docx.Document()
    
    # Page setup: A4, 1 inch margins
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1)
        s.bottom_margin = Inches(1)
        s.left_margin = Inches(1)
        s.right_margin = Inches(1)

    # Styles
    title_p = doc.add_paragraph()
    title_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run(c['title'])
    title_run.bold = True
    title_run.font.size = Pt(16)
    title_run.font.color.rgb = RGBColor(0, 51, 102)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = sub_p.add_run(f"{c['competition']}\n{c['organizer']}")
    sub_run.font.size = Pt(11)
    sub_run.font.color.rgb = RGBColor(100, 100, 100)

    # Meta card table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Nama Tim", c['team_name']),
        ("Subtema", c['subtheme']),
        ("Judul Karya", f"“{c['work_title']}”"),
        ("Status Berkas", "Laporan Resmi Pendukung Karya Infografis Bab A - Bab G")
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(1.8)
        c1.width = Inches(4.5)
        c0.text = k
        c0.paragraphs[0].runs[0].bold = True
        c0.paragraphs[0].runs[0].font.size = Pt(10)
        c0.paragraphs[0].runs[0].font.color.rgb = RGBColor(0, 51, 102)
        c1.text = v
        c1.paragraphs[0].runs[0].font.size = Pt(10)
        set_cell_background(c0, "F0F4F8")
        set_cell_background(c1, "FAFAFA")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    def add_heading_1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        r = h.add_run(text)
        r.bold = True
        r.font.size = Pt(13)
        r.font.color.rgb = RGBColor(0, 51, 102)

    def add_heading_2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)
        r = h.add_run(text)
        r.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(40, 90, 140)

    def add_body(text, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.size = Pt(10.5)

    # BAB A
    add_heading_1(c['bab_a_title'])
    for p in c['bab_a_paragraphs']:
        add_body(p)

    # BAB B
    add_heading_1(c['bab_b_title'])
    for p in c['bab_b_paragraphs']:
        add_body(p)

    # BAB C
    add_heading_1(c['bab_c_title'])
    for sub in c['bab_c_subsections']:
        add_heading_2(sub['subtitle'])
        for line in sub['content'].split("\n"):
            if line.strip():
                add_body(line.strip(), space_after=4)

    # BAB D
    add_heading_1(c['bab_d_title'])
    for sec in c['bab_d_sections']:
        add_heading_2(sec['head'])
        for line in sec['text'].split("\n"):
            if line.strip():
                add_body(line.strip(), space_after=4)

    # BAB E
    add_heading_1(c['bab_e_title'])
    add_heading_2("1. Kesimpulan Temuan Data")
    for con in c['bab_e_conclusions']:
        add_body(con)
    add_heading_2("2. Rekomendasi Solusi Kebijakan Terukur")
    for pol in c['bab_e_policies']:
        for line in pol.split("\n"):
            if line.strip():
                add_body(line.strip(), space_after=4)

    # BAB F
    add_heading_1(c['bab_f_title'])
    for i, ref in enumerate(c['bab_f_items'], 1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(f"{i}. {ref}")
        r.font.size = Pt(10)

    # BAB G
    add_heading_1(c['bab_g_title'])
    for tbl in c['bab_g_tables']:
        add_heading_2(tbl['title'])
        table = doc.add_table(rows=len(tbl['rows']) + 1, cols=len(tbl['headers']))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Header row
        hdr_cells = table.rows[0].cells
        for idx, h_text in enumerate(tbl['headers']):
            hdr_cells[idx].text = h_text
            hdr_cells[idx].paragraphs[0].runs[0].bold = True
            hdr_cells[idx].paragraphs[0].runs[0].font.size = Pt(9.5)
            hdr_cells[idx].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
            set_cell_background(hdr_cells[idx], "003366")
            set_cell_margins(hdr_cells[idx], 80, 80, 100, 100)
            
        # Data rows
        for r_idx, row_data in enumerate(tbl['rows']):
            row_cells = table.rows[r_idx + 1].cells
            bg = "F9FBFD" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row_data):
                row_cells[c_idx].text = val
                row_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(9)
                set_cell_background(row_cells[c_idx], bg)
                set_cell_margins(row_cells[c_idx], 60, 60, 80, 80)
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_body("Seluruh berkas mentah kode analisis, notebook Jupyter, data tabel BPS, dan aset grafik resolusi tinggi (PNG & SVG 300 dpi) tersimpan pada repositori proyek lokal dan siap diunggah ke tautan Google Drive publik untuk penilaian tahap penyisihan dan final.")
    
    doc.save(OUTPUT_DOCX)
    print(f"Docx file saved successfully: {OUTPUT_DOCX}")

if __name__ == "__main__":
    content = build_full_report_content()
    
    md_text = generate_full_markdown(content)
    OUTPUT_MD.write_text(md_text, encoding="utf-8")
    print(f"Markdown file saved successfully: {OUTPUT_MD}")
    
    generate_full_docx(content)
