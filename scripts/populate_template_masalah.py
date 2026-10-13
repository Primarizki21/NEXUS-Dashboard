"""
Populates template_masalah.docx with data findings, research questions,
storyline breakdown (5 Bagian), and visualization specifications for the design team.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pathlib import Path

INPUT_DOCX = "template_masalah.docx"
OUTPUT_DOCX = "template_masalah_terisi.docx"
OUTPUT_MD = "DRAFT_TEMPLATE_MASALAH.md"

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
            "Mengapa tingkat pengangguran terbuka pada lulusan SMK Kejuruan (6,81%) dan Perguruan Tinggi (5,33%) secara persisten jauh melampaui lulusan SD (1,92%)—apa faktor pendorong 'Educated Unemployment Paradox' di Indonesia?",
            "Sejauh mana krisis ketenagakerjaan terkonsentrasi pada generasi muda (15–24 tahun) dan bagaimana dampaknya terhadap ancaman kegagalan pemanfaatan jendela bonus demografi menuju Indonesia Emas 2045?",
            "Bagaimana tipologi klaster ketenagakerjaan daerah di Indonesia, dan instrumen kebijakan afirmatif apa yang terbukti paling berdaya guna ('Turning Insight into Opportunity') untuk mempercepat pemerataan kesempatan kerja?"
        ],
        "roadmap": [
            "Bagian I: 'The Demographic Cliff' — Krisis Ketenagakerjaan dan Jebakan Waktu Generasi Muda",
            "Bagian II: 'The Diploma Paradox' — Anomali Pengangguran Terdidik & Retaknya Jembatan Vokasi",
            "Bagian III: 'The Spatial Fracture' — Disparitas Regional dan Ilusi Pengangguran Rendah",
            "Bagian IV: 'The Recovery Drift' — Jejak Luka Pandemi dan Evaluasi Daya Pulih Lapangan Kerja",
            "Bagian V: 'Turning Insight into Opportunity' — Matriks Intervensi Kebijakan Berbasis Klaster Wilayah"
        ],
        "sections": [
            {
                "num": "Bagian I",
                "sub": "“The Demographic Cliff” — Krisis Ketenagakerjaan dan Jebakan Waktu Generasi Muda",
                "prelude": "Indonesia tengah berpacu dengan waktu dalam memanfaatkan puncak bonus demografi. Namun di balik narasi optimisme tersebut, pasar kerja nasional menyimpan retakan tajam: lebih dari separuh penganggur di Indonesia adalah generasi muda. Transisi dari bangku sekolah menuju dunia kerja (school-to-work transition) berubah menjadi jurang pemisah, di mana angkatan kerja muda menghadapi dinding ketidakpastian yang berisiko memicu efek luka permanen (scarring effect) pada prospek pendapatan seumur hidup mereka.",
                "data": "• TPT Usia Muda (15–24 tahun) per Agustus 2024 mencapai 17,02%, sedangkan TPT Usia Dewasa (25–59 tahun) hanya 2,45%.\n• Rasio pengangguran muda terhadap dewasa adalah 6,95 kali lipat.\n• Pangsa pemuda dalam total pengangguran terbuka nasional mencapai 56,70% (lebih dari 1 dari setiap 2 penganggur adalah pemuda).\n• TPT nasional per Agustus 2024 berada pada level 4,91% (152,11 juta angkatan kerja; 144,64 juta bekerja).",
                "link": "https://www.bps.go.id/id/pressrelease/2024/11/05/2373/unemployment-rate-was-4-91-percent-.html (BPS: Berita Resmi Statistik Ketenagakerjaan Agustus 2024)\nhttps://www.bps.go.id/id/publication/2024/12/16/d96c70fc6be192f04edf7fe0 (BPS: Indikator Pasar Tenaga Kerja Indonesia)",
                "viz": "• Visualisasi Utama: Ranked Split-Bar Chart / Comparison Gauge membandingkan TPT Pemuda (17,02%) vs TPT Dewasa (2,45%).\n• Callout Elemen: Angka tipografi raksasa '6,95x LIPAT' dan '56,7% GENERASI MUDA' sebagai hook pembuka visual di sepertiga atas infografis.\n• Palet Rekomendasi: Deep Navy untuk dasar, Amber Coral untuk menyorot angka krisis generasi muda."
            },
            {
                "num": "Bagian II",
                "sub": "“The Diploma Paradox” — Anomali Pengangguran Terdidik & Retaknya Jembatan Vokasi",
                "prelude": "Asumsi umum menyatakan bahwa semakin tinggi jenjang pendidikan, semakin mudah seseorang terserap di dunia kerja. Data resmi Sakernas BPS meruntuhkan asumsi ini secara telak. Lulusan SMK yang didesain siap kerja justru konsisten menyandang tingkat pengangguran tertinggi di Indonesia, disusul SMA umum dan universitas. Di sisi sebaliknya, lulusan SD ke bawah memiliki pengangguran terendah bukan karena keunggulan produktivitas, melainkan karena ketiadaan jaring pengaman finansial yang memaksa mereka menyerap pekerjaan apa saja, sementara lulusan berpendidikan tinggi terjebak dalam upah reservasi (reservation wage) dan ketidaksesuaian keterampilan (skill mismatch).",
                "data": "• TPT SMK Kejuruan (Agustus 2024): 6,81% (Tertinggi di antara seluruh jenjang pendidikan, 3,55x lipat TPT SD).\n• TPT SMA Umum: 6,69%.\n• TPT Universitas (S1+): 5,33% (Mengalami kenaikan dari 4,80% pada 2022 dan berada di atas rata-rata nasional 4,91%).\n• TPT Diploma I/II/III: 4,27%.\n• TPT SMP: 4,10%.\n• TPT SD ke Bawah: 1,92% (Terendah).\n• Lulusan pendidikan menengah (SMA & SMK) menyumbang 55,37% dari total penganggur di Indonesia.",
                "link": "https://web-api.bps.go.id/download.php?f=Q8zHxSFXa%2FNJceG%2FMTOFZlJ1OEMyLy9RRlhYTldnelRLR1JiaDlUaVlMWFN0dDdiRjhmZmFIYnhyUHhUZEpNRk1ReVNOM01hNUEvNzBjelNGcWR1MG1lNWRSaDBGclBlU01qL0hiRDBJc2lvWXE2Y2d5REJtcWNHd2RQUkppLzZ0U3hWVU42cVZTZzgzNTlRTGhuT2pNSTVXREpMUERpazB0MnZRSDRla0ZKRklRVUkwZXdIU1ZKUWdsd0VZdEJKNGM1RHRvQ3pXZXNmUTZIRzU5NEl4UnBMRmRzLzVJZWFoR0srRlNaVk1nZ3hUTkt3U2crTTBuR0d1NUdNNkszNFJ3V2J4RnB3T2ZhZ3dXcUFNT1dWNk5Kei9LelJ6NGhhMDNsQzFBPT0%3D (BPS: Lampiran 18 & Tabel 5)",
                "viz": "• Visualisasi Utama: Horizontal Ranked Bar Chart dengan pengurutan tangga pendidikan (SD 1,92% -> SMK 6,81%).\n• Aksen Visual: Bar SMK dan Universitas diberi warna kontras (Warning Crimson/Amber), sedangkan bar SD diberi warna netral dengan anotasi penjelas 'Terpaksa Bekerja di Sektor Apa Saja'.\n• Visual Pendukung: Donut chart komposisi penganggur menurut pendidikan (55,37% menengah, 30,89% dasar, 13,74% tinggi)."
            },
            {
                "num": "Bagian III",
                "sub": "“The Spatial Fracture” — Disparitas Regional dan Ilusi Pengangguran Rendah",
                "prelude": "Melihat pengangguran hanya dari rata-rata nasional ibarat mengukur kedalaman sungai dari rata-ratanya: mengabaikan palung yang mematikan. Terdapat disparitas regional ekstrem hingga 5,11 kali lipat antar-provinsi di Indonesia. Ironisnya, provinsi dengan angka TPT terendah bukanlah pusat kemakmuran, melainkan daerah dengan tingkat informalitas ekstrem (hingga 95%) di mana masyarakat bekerja subsisten tanpa upah layak. Sebaliknya, pusat industri berupah tinggi seperti Jawa Barat dan Banten justru menjadi magnet pengangguran terbuka karena derasnya urbanisasi dan selektivitas industri padat modal.",
                "data": "• Disparitas Rasio: 5,11 Kali Lipat (Jawa Barat 6,75% vs Papua Pegunungan 1,32%).\n• Top 5 TPT Tertinggi: Jawa Barat (6,75%), Banten (6,68%), Papua Barat Daya (6,48%), Papua (6,48%), Kepulauan Riau (6,39%).\n• Top 5 TPT Terendah: Papua Pegunungan (1,32%), Bali (1,79%), Sulawesi Barat (2,68%), NTB (2,73%), Papua Tengah (2,75%).\n• Korelasi Negatif Kuat: r = -0,782 antara TPT Total dan Persentase Pekerja Informal (daerah TPT rendah adalah perangkap informalitas).\n• Korelasi Positif: r = +0,641 antara TPT dan Rata-rata Upah Buruh (provinsi upah tinggi memiliki antrean pencari kerja formal yang padat).",
                "link": "https://www.bps.go.id/id/publication/2024/12/16/d96c70fc6be192f04edf7fe0 (Lampiran 16: Formal/Informal & Lampiran 17: TPT Provinsi)",
                "viz": "• Visualisasi Utama: Peta Choropleth Indonesia tematik 38 provinsi yang mengombinasikan kuadran spasial (Choropleth bivariate atau peta klaster wilayah).\n• Grafik Pendukung: Scatterplot Korelasi (Sumbu X: % Pekerja Informal, Sumbu Y: TPT %) dengan garis tren negatif r = -0,782 yang membuktikan ilusi TPT rendah di kawasan agraris/timur Indonesia."
            },
            {
                "num": "Bagian IV",
                "sub": "“The Recovery Drift” — Jejak Luka Pandemi dan Evaluasi Daya Pulih Lapangan Kerja",
                "prelude": "Dinamika 8 tahun terakhir (2017–2024) mencatat guncangan struktural terbesar dalam sejarah ketenagakerjaan modern: pandemi COVID-19 pada 2020 yang melambungkan TPT nasional ke angka 7,07%. Meski pada Agustus 2024 angka TPT nasional telah pulih ke 4,91% (di bawah pra-pandemi 2019), trajektori pemulihan di tingkat daerah berlangsung dengan dua kecepatan yang sangat berbeda. Beberapa provinsi manufaktur pulih pesat, sementara daerah lain mengalami efek luka persisten (hysteresis) di mana lapangan kerja formal berkualitas belum sepenuhnya kembali.",
                "data": "• Trajektori TPT Nasional: 2017 (5,50%) -> 2018 (5,30%) -> 2019 (5,23%) -> 2020 Lonjakan Pandemi (7,07%) -> 2021 (6,49%) -> 2022 (5,86%) -> 2023 (5,32%) -> 2024 (4,91%).\n• Besaran Guncangan: +1,84 persen poin pada tahun 2020 (+2,67 juta penganggur baru akibat pembatasan mobilitas).\n• Provinsi Pemulihan Terpesat (2019 vs 2024): Riau (-2,06 poin), Banten (-1,43 poin), Jawa Barat (-1,29 poin), Kepulauan Riau (-1,11 poin).\n• Provinsi yang Mengalami Pemulihan Lambat / Kenaikan TPT: Papua (+2,97 poin), Jawa Timur (+0,37 poin), DI Yogyakarta (+0,30 poin).",
                "link": "https://web-api.bps.go.id/download.php?f=BGTg1p02Du9WXu5Fccj77mxaZDlYODZwWlpxV0p4TUNrMjZucWQ1L3NSc01KNFU0T0tjU3pWTFFGQStIVHNsd3BnYlUwUVpjTWdXN3d5ekxaL1hDK2VsY3NsOUFWRTJSemFQZk0xbEFEQWFMS3F1TXBQWk5UNit4aFkyUXU2c0ErZHNpR1JVN2p6RHNUeDhuVkh1N0NNaktYNFpma0NEckRGTFBaNkhKTGJOeXlXbHJ1R3dwMUZ1TklrQ0NXR3U1RCtLN3dIZGxzUFBpcHp1bnpoWk41Z3JDcHdtUXhvYkhTVHBVYVhVYS9VN0pMNXNMSWV1QTFXc2kvVXBQVVFoZ3lzVlVWQ09KNCtNZ1Fmc3Y1cUpaQVlIMTdrVFBsU242TFdyaVJiY1NoZDJOV0pXWHZGRGN3dnJUTzQrOGFHK1BjZHZBdW5QRWppOHVaMy9M (Tabel 5.6 & Profil Pengangguran BPS)",
                "viz": "• Visualisasi Utama: Area Timeline Chart (2017–2024) yang menonjolkan puncak patahan struktural 2020 dengan shading 'Guncangan Pandemi' dan garis tren proyeksi melandai ke 4,91% di 2024.\n• Mini-Sparklines: Perbandingan trajektori pemulihan provinsi kontras (Jabar & Riau pulih tajam vs Jatim & Papua melambat)."
            },
            {
                "num": "Bagian V",
                "sub": "“Turning Insight into Opportunity” — Matriks Intervensi Kebijakan Berbasis Klaster Wilayah",
                "prelude": "Kebijakan ketenagakerjaan 'satu ukuran untuk semua' (one-size-fits-all) telah terbukti usang. Berdasarkan hasil analisis data BPS, Indonesia terbagi ke dalam 3 tipologi pasar kerja yang memiliki akar permasalahan berbeda secara fundamental. Untuk mewujudkan pemerataan kesempatan kerja yang nyata, solusi kebijakan harus ditargetkan secara presisi sesuai klaster wilayah: menghubungkan lulusan vokasi dengan industri berteknologi di kawasan urban, melakukan transformasi formalitas di kawasan agraris, dan mempercepat ekonomi digital di kawasan transisi.",
                "data": "Hasil Klasterisasi K-Means (k = 3, Evaluasi Silhouette = 0,441):\n\n1. KLASTER 1: URBAN-INDUSTRIAL TRAP (8 Provinsi — DKI, Jabar, Banten, Kepri, Kaltim, Papua, Papua Barat Daya, Maluku)\n   • Karakteristik: TPT Tinggi (rata-rata 6,58%), Formal Tinggi (56,8%), Upah Tinggi (Rp3,85 jt), Mismatch Vokasi Akut.\n   • Solusi Konkret: 'Vocational Dual-System & Tax Superdeduction' — Kurikulum co-creation industri manufaktur/IT, insentif pajak penyerapan pemuda lokal, dan standardisasi upah magang bersertifikat.\n\n2. KLASTER 2: AGRARIS-INFORMAL SHELTER (18 Provinsi — NTT, NTB, Sulbar, Sulteng, Gorontalo, Lampung, Bengkulu, Papua Pegunungan, Papua Tengah, Papua Selatan, dll.)\n   • Karakteristik: TPT Rendah Semu (2,82%), Informalitas Ekstrem (75,4%), Upah Rendah (Rp2,62 jt), Setengah Penganggur Tinggi.\n   • Solusi Konkret: 'Agro-Downstreaming & Formalization Safety Net' — Hilirisasi komoditas pertanian/perikanan lokal skala UMKM, subsidi iuran jaminan sosial BPJS Ketenagakerjaan bagi pekerja rentan, dan digitalisasi rantai pasok daerah.\n\n3. KLASTER 3: TRANSISI BERIMBANG (12 Provinsi — Jateng, Jatim, DIY, Bali, Sumut, Sumbar, Sumsel, Jambi, Riau, Kalbar, Kalteng, Kalsel)\n   • Karakteristik: TPT Moderat (4,52%), Pasar Kerja Terdiversifikasi, Informalitas 52,6%, Upah Rp2,88 jt.\n   • Solusi Konkret: 'Youth Creative-Tech Hub & Micro-Capital' — Inkubasi wirausaha digital pemuda, fasilitasi akses modal kerja berbunga rendah (KUR Klaster), dan sertifikasi talenta gig-economy.",
                "link": "https://data.go.id/ & https://bps.go.id/ (Dataset Olahan Klaster Provinsi ACTION 2026)",
                "viz": "• Visualisasi Utama: 3-Pillar Solution Architecture Matrix (Tiga kolom/kartu kebijakan berdampingan sesuai nama klaster, memuat ikon strategi, target provinsi, dan indikator dampak keberhasilan).\n• Penutup Callout: Rekomendasi Roadmap Aksi Nasional Menuju Pemerataan Kesempatan Kerja 2029."
            }
        ],
        "matriks": [
            {"kriteria": "Kreativitas & Orisinalitas (30%)", "strategi": "Mengangkat sudut pandang unik 'Educated Unemployment Paradox' dan membongkar mitos 'TPT Rendah = Makmur' melalui korelasi informalitas (r = -0,782). Bebas AI generatif."},
            {"kriteria": "Kualitas Visual & Tata Letak (25%)", "strategi": "Hierarki visual A3 Portrait mengalir dari Hook Generasi Muda -> Paradoks Pendidikan -> Peta Disparitas -> Tren Waktu -> Matriks Solusi 3 Klaster. Pilihan warna terukur, tipografi terbaca."},
            {"kriteria": "Akurasi & Kedalaman Informasi (20%)", "strategi": "100% data resmi Sakernas BPS 2017–2024 dan publikasi resmi panitia. Perhitungan statistik panel, dekomposisi disparitas, dan K-Means teruji."},
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
    # Paragraph mapping based on earlier inspection
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
    # Keep up to paragraph 21 ("Isi Infografis")
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
