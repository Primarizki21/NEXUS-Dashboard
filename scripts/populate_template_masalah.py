"""
Populates template_masalah.docx with data findings, research questions,
storyline breakdown (5 Bagian), and visualization specifications for the design team.
Updated with Labor Underutilization, Urban-Rural Disparities, and RPJMN 2029 Target Allocations.
Compliant with antislop R-02 (Zero em dashes).
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / "docs" if (ROOT_DIR / "docs").exists() else ROOT_DIR

INPUT_DOCX = DOCS_DIR / "template_masalah.docx"
OUTPUT_DOCX = DOCS_DIR / "template_masalah_terisi.docx"
OUTPUT_MD = DOCS_DIR / "DRAFT_TEMPLATE_MASALAH.md"

def build_content():
    return {
        "lomba": "ACTION 2026 (Annual Competition of Data Science 2026)",
        "penyelenggara": "HMP Sains Data, Universitas Negeri Surabaya (UNESA)",
        "tim": "[Nama Tim Peserta]",
        "tema": "Inovasi Sains Data untuk Kesejahteraan Publik dan Pembangunan Berkelanjutan",
        "subtema": "Turning Insight into Opportunity: Analisis Pengangguran Terbuka untuk Pemerataan Kesempatan Kerja",
        "judul": "Paradoks Ijazah di Negeri Zamrud: Menyingkap Peta Retak Pengangguran Terbuka dan Merajut Peluang Kerja Inklusif Indonesia",
        "rqs": [
            "Seberapa timpang distribusi pengangguran terbuka antar-provinsi di Indonesia, dan apakah daerah dengan TPT rendah benar-benar mencerminkan kemakmuran atau sekadar ilusi penyerapan sektor informal rentan?",
            "Mengapa tingkat pengangguran terbuka pada lulusan SMK Kejuruan (6,81%) dan Perguruan Tinggi (5,33%) secara persisten jauh melampaui lulusan SD (1,92%): apa faktor pendorong 'Educated Unemployment Paradox' di Indonesia?",
            "Sejauh mana krisis ketenagakerjaan terkonsentrasi pada generasi muda (15-24 tahun) dan bagaimana dampaknya terhadap ancaman kegagalan pemanfaatan jendela bonus demografi menuju Indonesia Emas 2045?",
            "Bagaimana fenomena gunung es setengah pengangguran (11,56 juta orang) dan dikotomi kota-desa memengaruhi perumusan instrumen kebijakan afirmatif ('Turning Insight into Opportunity') untuk mencapai target RPJMN 2029?"
        ],
        "roadmap": [
            "Bagian I: 'The Demographic Cliff': Krisis Ketenagakerjaan dan Jebakan Waktu Generasi Muda",
            "Bagian II: 'The Diploma Paradox': Anomali Pengangguran Terdidik & Retaknya Jembatan Vokasi",
            "Bagian III: 'The Spatial Fracture': Disparitas Regional dan Ilusi Pengangguran Rendah",
            "Bagian IV: 'The Underutilization Iceberg': Lonjakan Setengah Penganggur & Dikotomi Kota-Desa",
            "Bagian V: 'Turning Insight into Opportunity': Matriks Target 5,4 Juta Peluang Kerja Berbasis Klaster"
        ],
        "sections": [
            {
                "num": "Bagian I",
                "sub": "“The Demographic Cliff”: Krisis Ketenagakerjaan dan Jebakan Waktu Generasi Muda",
                "prelude": "Indonesia tengah berpacu dengan waktu dalam memanfaatkan puncak bonus demografi. Namun di balik narasi optimisme tersebut, pasar kerja nasional menyimpan retakan tajam: lebih dari separuh penganggur di Indonesia adalah generasi muda. Transisi dari bangku sekolah menuju dunia kerja (school-to-work transition) berubah menjadi jurang pemisah, di mana angkatan kerja muda menghadapi dinding ketidakpastian yang berisiko memicu efek luka permanen (scarring effect) pada prospek pendapatan seumur hidup mereka.",
                "data": "• TPT Usia Muda (15-24 tahun) per Agustus 2024 mencapai 17,02%, sedangkan TPT Usia Dewasa (25-59 tahun) hanya 2,45%.\n• Rasio pengangguran muda terhadap dewasa adalah 6,95 kali lipat.\n• Pangsa pemuda dalam total pengangguran terbuka nasional mencapai 56,70% (lebih dari 1 dari setiap 2 penganggur adalah pemuda).\n• TPT nasional per Agustus 2024 berada pada level 4,91% (152,11 juta angkatan kerja; 144,64 juta bekerja).",
                "link": "https://www.bps.go.id/id/pressrelease/2024/11/05/2373/unemployment-rate-was-4-91-percent-.html (BPS: Berita Resmi Statistik Ketenagakerjaan Agustus 2024)\nhttps://www.bps.go.id/id/publication/2024/12/16/d96c70fc6be192f04edf7fe0 (BPS: Indikator Pasar Tenaga Kerja Indonesia)",
                "viz": "• Visualisasi Utama: Ranked Split-Bar Chart / Comparison Gauge membandingkan TPT Pemuda (17,02%) vs TPT Dewasa (2,45%).\n• Callout Elemen: Angka tipografi raksasa '6,95x LIPAT' dan '56,7% GENERASI MUDA' sebagai hook pembuka visual di sepertiga atas infografis.\n• Palet Rekomendasi: Deep Navy untuk dasar, Amber Coral untuk menyorot angka krisis generasi muda."
            },
            {
                "num": "Bagian II",
                "sub": "“The Diploma Paradox”: Anomali Pengangguran Terdidik & Retaknya Jembatan Vokasi",
                "prelude": "Asumsi umum menyatakan bahwa semakin tinggi jenjang pendidikan, semakin mudah seseorang terserap di dunia kerja. Data resmi Sakernas BPS meruntuhkan asumsi ini secara telak. Lulusan SMK yang didesain siap kerja justru konsisten menyandang tingkat pengangguran tertinggi di Indonesia, disusul SMA umum dan universitas. Di sisi sebaliknya, lulusan SD ke bawah memiliki pengangguran terendah bukan karena keunggulan produktivitas, melainkan karena ketiadaan jaring pengaman finansial yang memaksa mereka menyerap pekerjaan apa saja, sementara lulusan berpendidikan tinggi terjebak dalam upah reservasi (reservation wage) dan ketidaksesuaian keterampilan (skill mismatch).",
                "data": "• TPT SMK Kejuruan (Agustus 2024): 6,81% (Tertinggi di antara seluruh jenjang pendidikan, 3,55x lipat TPT SD).\n• TPT SMA Umum: 6,69%.\n• TPT Universitas (S1+): 5,33% (Mengalami kenaikan dari 4,80% pada 2022 dan berada di atas rata-rata nasional 4,91%).\n• TPT Diploma I/II/III: 4,27%.\n• TPT SMP: 4,10%.\n• TPT SD ke Bawah: 1,92% (Terendah).\n• Lulusan pendidikan menengah (SMA & SMK) menyumbang 55,37% dari total penganggur di Indonesia.\n• Stagnasi Sektor Manufaktur: Penyerapan tenaga kerja sektor pabrik pengolahan formal stagnan di 13,83% (2023 vs 2024).",
                "link": "https://web-api.bps.go.id/download.php?f=Q8zHxSFXa%2FNJceG%2FMTOFZlJ1OEMyLy9RRlhYTldnelRLR1JiaDlUaVlMWFN0dDdiRjhmZmFIYnhyUHhUZEpNRk1ReVNOM01hNUEvNzBjelNGcWR1MG1lNWRSaDBGclBlU01qL0hiRDBJc2lvWXE2Y2d5REJtcWNHd2RQUkppLzZ0U3hWVU42cVZTZzgzNTlRTGhuT2pNSTVXREpMUERpazB0MnZRSDRla0ZKRklRVUkwZXdIU1ZKUWdsd0VZdEJKNGM1RHRvQ3pXZXNmUTZIRzU5NEl4UnBMRmRzLzVJZWFoR0srRlNaVk1nZ3hUTkt3U2crTTBuR0d1NUdNNkszNFJ3V2J4RnB3T2ZhZ3dXcUFNT1dWNk5Kei9LelJ6NGhhMDNsQzFBPT0%3D (BPS: Lampiran 18 & Tabel 5)",
                "viz": "• Visualisasi Utama: Horizontal Ranked Bar Chart dengan pengurutan tangga pendidikan (SD 1,92% -> SMK 6,81%).\n• Aksen Visual: Bar SMK dan Universitas diberi warna kontras (Warning Crimson/Amber), sedangkan bar SD diberi warna netral dengan anotasi penjelas 'Terpaksa Bekerja di Sektor Apa Saja'.\n• Visual Pendukung: Donut chart komposisi penganggur menurut pendidikan (55,37% menengah, 30,89% dasar, 13,74% tinggi)."
            },
            {
                "num": "Bagian III",
                "sub": "“The Spatial Fracture”: Disparitas Regional dan Ilusi Pengangguran Rendah",
                "prelude": "Melihat pengangguran hanya dari rata-rata nasional ibarat mengukur kedalaman sungai dari rata-ratanya: mengabaikan palung yang mematikan. Terdapat disparitas regional ekstrem hingga 5,11 kali lipat antar-provinsi di Indonesia. Ironisnya, provinsi dengan angka TPT terendah bukanlah pusat kemakmuran, melainkan daerah dengan tingkat informalitas ekstrem (hingga 95%) di mana masyarakat bekerja subsisten tanpa upah layak. Sebaliknya, pusat industri berupah tinggi seperti Jawa Barat dan Banten justru menjadi magnet pengangguran terbuka karena derasnya urbanisasi dan selektivitas industri padat modal.",
                "data": "• Disparitas Rasio: 5,11 Kali Lipat (Jawa Barat 6,75% vs Papua Pegunungan 1,32%).\n• Top 5 TPT Tertinggi: Jawa Barat (6,75%), Banten (6,68%), Papua Barat Daya (6,48%), Papua (6,48%), Kepulauan Riau (6,39%).\n• Top 5 TPT Terendah: Papua Pegunungan (1,32%), Bali (1,79%), Sulawesi Barat (2,68%), NTB (2,73%), Papua Tengah (2,75%).\n• Korelasi Negatif Kuat: r = -0,782 antara TPT Total dan Persentase Pekerja Informal (daerah TPT rendah adalah perangkap informalitas).\n• Korelasi Positif: r = +0,641 antara TPT dan Rata-rata Upah Buruh (provinsi upah tinggi memiliki antrean pencari kerja formal yang padat).",
                "link": "https://www.bps.go.id/id/publication/2024/12/16/d96c70fc6be192f04edf7fe0 (Lampiran 16: Formal/Informal & Lampiran 17: TPT Provinsi)",
                "viz": "• Visualisasi Utama: Peta Choropleth Indonesia tematik 38 provinsi yang mengombinasikan kuadran spasial (Choropleth bivariate atau peta klaster wilayah).\n• Grafik Pendukung: Scatterplot Korelasi (Sumbu X: % Pekerja Informal, Sumbu Y: TPT %) dengan garis tren negatif r = -0,782 yang membuktikan ilusi TPT rendah di kawasan agraris/timur Indonesia."
            },
            {
                "num": "Bagian IV",
                "sub": "“The Underutilization Iceberg”: Lonjakan Setengah Penganggur & Dikotomi Kota-Desa",
                "prelude": "Penurunan TPT nasional ke 4,91% menutupi kenyataan bahwa kualitas pekerjaan di Indonesia justru mengalami kemunduran. Standar ILO membuktikan bahwa pengangguran terbuka hanyalah puncak gunung es: jumlah setengah penganggur (pekerja jam rendah yang butuh kerja tambahan) justru meledak +23,8% dalam setahun. Terjadi keterbelahan dua wajah ketenagakerjaan: antrean kerja formal di perkotaan vs perangkap setengah penganggur paruh waktu di perdesaan.",
                "data": "• Lonjakan Setengah Penganggur: Naik dari 9,34 juta (6,68%) di 2023 menjadi 11,56 juta orang (7,99%) di 2024 (+2,22 juta orang / +23,8%).\n• Defisit Utilisasi Kerja Nasional (Standar ILO LU2): 12,51% atau 19,03 juta orang angkatan kerja mengalami kekurangan jam kerja dan pengangguran.\n• Dikotomi Kota vs Desa (Agustus 2024):\n  - TPT Total: Perkotaan 5,79% vs Perdesaan 3,67% (Kota 1,58x lebih tinggi).\n  - Setengah Penganggur: Perkotaan 6,09% vs Perdesaan 10,60% (Desa 1,74x lebih parah).\n  - TPT Usia Muda: Perkotaan 19,86% (1 dari 5 pemuda kota menganggur) vs Perdesaan 13,85%.\n  - Rasio Kerentanan Pemuda vs Dewasa: Perdesaan 7,45x lipat vs Perkotaan 5,93x lipat.",
                "link": "https://www.bps.go.id/id/publication/2024/12/16/d96c70fc6be192f04edf7fe0 (Lampiran 13: Pekerja Paruh Waktu, Lampiran 15: Jam Kerja, & KILM 12: Setengah Pengangguran)",
                "viz": "• Visualisasi Utama: Stacked Waterfall / Iceberg Chart (Chart 14) membandingkan TPT 4,91% (7,47 jt) vs Setengah Penganggur 7,99% (11,56 jt) vs LU2 12,51% (19,03 jt).\n• Visual Komparasi: Bilateral Dumbbell Plot (Chart 15) yang mengontraskan 5 indikator pasar kerja Perkotaan vs Perdesaan."
            },
            {
                "num": "Bagian V",
                "sub": "“Turning Insight into Opportunity”: Matriks Target 5,4 Juta Peluang Kerja Berbasis Klaster",
                "prelude": "Kebijakan ketenagakerjaan 'satu ukuran untuk semua' (one-size-fits-all) telah terbukti usang. Untuk mencapai target RPJMN 2025-2029 (TPT nasional 4,00% - 4,50%), Indonesia membutuhkan penciptaan 5,40 juta kesempatan kerja berkualitas yang dialokasikan secara presisi ke dalam 3 klaster pasar kerja daerah: mengatasi kemacetan vokasi industri di kawasan perkotaan, mengonversi setengah penganggur agraris menjadi pekerja penuh waktu, dan mempercepat ekonomi digital di kawasan transisi.",
                "data": "Target Penciptaan 5,40 Juta Kesempatan Kerja Berkualitas Menuju 2029:\n\n1. KLASTER 1: URBAN-INDUSTRIAL TRAP (8 Provinsi: DKI, Jabar, Banten, Kepri, Kaltim, Papua, Papua Barat Daya, Maluku)\n   • Target: TPT turun dari 6,58% menjadi < 5,20%.\n   • Alokasi: 1,85 Juta Lowongan Kerja Formal Industri Manufaktur & Jasa IT.\n   • Solusi: Vocational Dual-System, insentif Tax Superdeduction penyerapan pemuda, dan standarisasi upah magang formal.\n\n2. KLASTER 2: AGRARIS-INFORMAL SHELTER (18 Provinsi: NTT, NTB, Sulbar, Sulteng, Gorontalo, Lampung, Bengkulu, Papua Pegunungan, Papua Tengah, Papua Selatan, dll.)\n   • Target: Tingkat Setengah Pengangguran turun dari 11,2% menjadi < 7,0%.\n   • Alokasi: 2,10 Juta Peningkatan Jam Kerja Penuh melalui Hilirisasi Komoditas Pertanian.\n   • Solusi: Korporatisasi petani lokal, modernisasi alat pascapanen, dan subsidi iuran BPJS Ketenagakerjaan bagi pekerja rentan.\n\n3. KLASTER 3: TRANSISI BERIMBANG (12 Provinsi: Jateng, Jatim, DIY, Bali, Sumut, Sumbar, Sumsel, Jambi, Riau, Kalbar, Kalteng, Kalsel)\n   • Target: TPT turun dari 4,52% menjadi < 3,80%.\n   • Alokasi: 1,45 Juta Pekerjaan Bernilai Tambah di Sektor Jasa Kreatif & Digital.\n   • Solusi: Youth Creative-Tech Hub di kota sekunder, inkubasi wirausaha muda, dan pembiayaan KUR Klaster Berbunga Rendah.",
                "link": "https://data.go.id/ & https://bps.go.id/ (Dataset Olahan Klaster & Simulasi Target RPJMN ACTION 2026)",
                "viz": "• Visualisasi Utama: 3-Pillar Solution Architecture Matrix (Tiga kolom/kartu kebijakan berdampingan sesuai nama klaster, memuat target penurunan TPT, kuota lapangan kerja baru, dan strategi aksi konkret).\n• Penutup Callout: Rekomendasi Roadmap Aksi Nasional Menuju Target RPJMN 2029 (5,40 Juta Kesempatan Kerja Berkualitas)."
            }
        ],
        "matriks": [
            {"kriteria": "Kreativitas & Orisinalitas (30%)", "strategi": "Mengangkat sudut pandang unik 'Educated Unemployment Paradox', 'The Underutilization Iceberg' (+23,8% setengah penganggur), dan membongkar mitos 'TPT Rendah = Makmur' melalui korelasi informalitas (r = -0,782). Bebas AI generatif."},
            {"kriteria": "Kualitas Visual & Tata Letak (25%)", "strategi": "Hierarki visual A3 Portrait mengalir dari Hook Generasi Muda -> Paradoks Pendidikan -> Peta Disparitas -> Gunung Es Utilisasi Kerja -> Matriks Target 5,4 Juta Peluang Kerja. Pilihan warna terukur, tipografi terbaca."},
            {"kriteria": "Akurasi & Kedalaman Informasi (20%)", "strategi": "100% data resmi Sakernas BPS 2017-2024 dan publikasi resmi panitia. Standar ILO LU2, ekonometrika spasial SDM, dekomposisi disparitas, dan K-Means teruji."},
            {"kriteria": "Kesesuaian Subtema & Teknis (10%)", "strategi": "Sepenuhnya menjawab 'Turning Insight into Opportunity'. Format A3 Portrait, 300 dpi, 3 logo resmi wajib di bagian atas, watermark nama tim di bawah."},
            {"kriteria": "Laporan Pendukung Karya (15%)", "strategi": "Laporan 7 bab disusun sistematis dan transparan dengan lampiran tautan kode kalkulasi reproduktif."}
        ]
    }

def generate_markdown(c):
    md = []
    md.append(f"# {c['lomba']}")
    md.append(f"### Penyelenggara: {c['penyelenggara']}")
    md.append(f"**Nama Tim:** {c['tim']}\n")
    md.append(f"**Tema:** {c['tema']}")
    md.append(f"**Subtema:** {c['subtema']}")
    md.append(f"**Judul:** “{c['judul']}”\n")
    md.append("---\n")
    md.append("## Research Questions\n")
    for i, rq in enumerate(c['rqs'], 1):
        md.append(f"{i}. {rq}")
    md.append("\n---\n")
    md.append("## Bagian Infografis (Alur Cerita 5 Babak)\n")
    for r in c['roadmap']:
        md.append(f"- {r}")
    md.append("\n---\n")
    md.append("## Isi Infografis (Detail Naskah, Data Resmi, & Spesifikasi Visual)\n")
    for sec in c['sections']:
        md.append(f"### {sec['num']}: {sec['sub']}\n")
        md.append(f"**Prelude:**\n{sec['prelude']}\n")
        md.append(f"**Data Resmi BPS:**\n{sec['data']}\n")
        md.append(f"**Tautan Sumber:**\n{sec['link']}\n")
        md.append(f"**Rekomendasi Visualisasi Desain:**\n{sec['viz']}\n")
        md.append("---\n")
    md.append("## Matriks Penilaian Babak Penyisihan ACTION 2026\n")
    md.append("| Kriteria Penilaian | Bobot | Strategi Pemenuhan dalam Karya |")
    md.append("|---|:---:|---|")
    for m in c['matriks']:
        k_name, weight = m['kriteria'].split('(')
        weight = weight.replace(')', '')
        md.append(f"| **{k_name.strip()}** | **{weight.strip()}** | {m['strategi']} |")
    return "\n".join(md)

def update_docx(c):
    doc = docx.Document(INPUT_DOCX)
    
    # Update header metadata
    doc.paragraphs[0].text = c['lomba']
    doc.paragraphs[1].text = c['penyelenggara']
    doc.paragraphs[2].text = f"“{c['tim']}”"
    doc.paragraphs[4].text = f"Tema\t\t: {c['tema']}"
    doc.paragraphs[5].text = f"Subtema\t: {c['subtema']}"
    doc.paragraphs[6].text = f"Judul\t\t: “{c['judul']}”"
    
    # Fill Research questions (p8 to p11)
    doc.paragraphs[8].text = f"1. {c['rqs'][0]}"
    doc.paragraphs[9].text = f"2. {c['rqs'][1]}"
    doc.paragraphs[10].text = f"3. {c['rqs'][2]}"
    doc.paragraphs[11].text = f"4. {c['rqs'][3]}"
    doc.paragraphs[12].text = "" # empty placeholder
    
    # Fill Bagian Infografis (p15 to p19)
    for i in range(5):
        doc.paragraphs[15 + i].text = c['roadmap'][i]
        
    # Clear remaining template body after p21 and rebuild structured sections
    p_len = len(doc.paragraphs)
    for idx in range(p_len - 1, 21, -1):
        p_elem = doc.paragraphs[idx]._element
        p_elem.getparent().remove(p_elem)
        
    # Append structured sections
    for sec in c['sections']:
        h = doc.add_paragraph()
        h_run = h.add_run(f"\n{sec['num']}: {sec['sub']}")
        h_run.bold = True
        h_run.font.size = Pt(13)
        h_run.font.color.rgb = RGBColor(0, 51, 102)
        
        p_pre = doc.add_paragraph()
        p_pre.add_run("Prelude: ").bold = True
        p_pre.add_run(sec['prelude'])
        
        p_data = doc.add_paragraph()
        p_data.add_run("Data Resmi BPS: ").bold = True
        p_data.add_run(sec['data'])
        
        p_link = doc.add_paragraph()
        p_link.add_run("Link Sumber: ").bold = True
        p_link.add_run(sec['link'])
        
        p_viz = doc.add_paragraph()
        p_viz.add_run("Rekomendasi Visualisasi: ").bold = True
        p_viz.add_run(sec['viz'])
        
    # Add Matriks Penilaian
    h_mat = doc.add_paragraph()
    h_mat_run = h_mat.add_run("\nMatriks Penilaian Babak Penyisihan (ACTION 2026)")
    h_mat_run.bold = True
    h_mat_run.font.size = Pt(13)
    
    table = doc.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Kriteria Penilaian'
    hdr_cells[1].text = 'Bobot'
    hdr_cells[2].text = 'Strategi Pemenuhan dalam Karya'
    for cell in hdr_cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                
    for m in c['matriks']:
        row_cells = table.add_row().cells
        k_name, weight = m['kriteria'].split('(')
        weight = weight.replace(')', '')
        row_cells[0].text = k_name.strip()
        row_cells[1].text = weight.strip()
        row_cells[2].text = m['strategi']
        
    doc.save(OUTPUT_DOCX)
    print(f"Docx file saved successfully: {OUTPUT_DOCX}")

def main():
    c = build_content()
    
    # Save markdown version
    md_text = generate_markdown(c)
    with open(OUTPUT_MD, "w") as f:
        f.write(md_text)
    print(f"Markdown file saved successfully: {OUTPUT_MD}")
    
    # Update docx version
    update_docx(c)

if __name__ == "__main__":
    main()
