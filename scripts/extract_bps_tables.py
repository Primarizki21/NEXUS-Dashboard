"""
Extraction script for BPS Labor Market Data (Indikator Pasar Tenaga Kerja Indonesia Agustus 2024)
Extracts official tables: Lampiran 16, 17, 18, 20, 26 and National Education / Age breakdowns.
Robust against watermarks, line wraps, and OCR typographical quirks.
"""

import pdfplumber
import pandas as pd
import re
from pathlib import Path

PDF_PATH = "data/raw/data_publikasi_bps_agustus_2024.pdf"
OUTPUT_DIR = Path("data/clean")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROVINSI_LIST = [
    "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan",
    "Bengkulu", "Lampung", "Kep. Bangka Belitung", "Kepulauan Riau", "DKI Jakarta",
    "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali",
    "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
    "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara",
    "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo",
    "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua Barat Daya",
    "Papua", "Papua Selatan", "Papua Tengah", "Papua Pegunungan", "Indonesia"
]

SORTED_PROVS = sorted(PROVINSI_LIST, key=len, reverse=True)

def clean_page_words(page):
    """Filters out diagonal watermark (Helvetica-Bold > 18pt) and returns sorted rows."""
    filtered_page = page.filter(lambda obj: 'Helvetica' not in obj.get('fontname', '') and obj.get('size', 0) < 18)
    words = filtered_page.extract_words()
    
    lines = {}
    for w in words:
        top_bucket = round(w['top'] / 3.5) * 3.5
        lines.setdefault(top_bucket, []).append(w)
        
    sorted_rows = []
    for top in sorted(lines.keys()):
        row_words = sorted(lines[top], key=lambda x: x['x0'])
        sorted_rows.append(row_words)
    return sorted_rows

def parse_table_page(page, num_expected, num_regex):
    """Parses a table page supporting multiline province wrapping and comma-spacing fixes."""
    rows = clean_page_words(page)
    data = []
    i = 0
    while i < len(rows):
        text = " ".join(w['text'] for w in rows[i])
        text = text.replace("Kep,", "Kep.")
        text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', text)
        nums = re.findall(num_regex, text)
        
        matched_prov = None
        for prov in SORTED_PROVS:
            pattern = r'\b' + re.escape(prov) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                matched_prov = prov
                break
                
        if matched_prov:
            if len(nums) == num_expected:
                data.append((matched_prov, nums))
            elif i + 1 < len(rows):
                next_text = " ".join(w['text'] for w in rows[i+1])
                next_text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', next_text)
                next_nums = re.findall(num_regex, next_text)
                if len(next_nums) == num_expected:
                    data.append((matched_prov, next_nums))
                    i += 1
        i += 1
    return data

def parse_lampiran_17(pdf):
    """Lampiran 17: TPT Menurut Provinsi dan Jenis Kelamin (persen), 2023–2024 (Page 159)."""
    raw_data = parse_table_page(pdf.pages[158], 9, r'\b\d{1,2},\d{2}\b')
    cols = [
        "Provinsi",
        "TPT_Laki_Ags2023", "TPT_Puan_Ags2023", "TPT_Total_Ags2023",
        "TPT_Laki_Feb2024", "TPT_Puan_Feb2024", "TPT_Total_Feb2024",
        "TPT_Laki_Ags2024", "TPT_Puan_Ags2024", "TPT_Total_Ags2024"
    ]
    rows = [[prov] + [float(x.replace(',', '.')) for x in nums] for prov, nums in raw_data]
    return pd.DataFrame(rows, columns=cols).drop_duplicates(subset=["Provinsi"])

def parse_lampiran_18(pdf):
    """Lampiran 18: TPT Menurut Provinsi dan Tingkat Pendidikan (persen), 2023–2024 (Page 160)."""
    raw_data = parse_table_page(pdf.pages[159], 9, r'\b\d{1,2},\d{2}\b')
    cols = [
        "Provinsi",
        "TPT_Dasar_Ags2023", "TPT_Dasar_Feb2024", "TPT_Dasar_Ags2024",
        "TPT_Menengah_Ags2023", "TPT_Menengah_Feb2024", "TPT_Menengah_Ags2024",
        "TPT_Tinggi_Ags2023", "TPT_Tinggi_Feb2024", "TPT_Tinggi_Ags2024"
    ]
    rows = [[prov] + [float(x.replace(',', '.')) for x in nums] for prov, nums in raw_data]
    return pd.DataFrame(rows, columns=cols).drop_duplicates(subset=["Provinsi"])

def parse_lampiran_16(pdf):
    """Lampiran 16: Persentase Penduduk Bekerja Menurut Provinsi dan Kegiatan Formal/Informal (Page 158)."""
    raw_data = parse_table_page(pdf.pages[157], 6, r'\b\d{1,2},\d{2}\b')
    cols = [
        "Provinsi",
        "Formal_Ags2023", "Formal_Feb2024", "Formal_Ags2024",
        "Informal_Ags2023", "Informal_Feb2024", "Informal_Ags2024"
    ]
    rows = [[prov] + [float(x.replace(',', '.')) for x in nums] for prov, nums in raw_data]
    return pd.DataFrame(rows, columns=cols).drop_duplicates(subset=["Provinsi"])

def parse_lampiran_26(pdf):
    """Lampiran 26: Rata-Rata Upah Buruh/Pegawai Menurut Provinsi (Rupiah), 2023–2024 (Page 168)."""
    raw_data = parse_table_page(pdf.pages[167], 9, r'\b\d{1,2}\.\d{3}\.\d{3}\b')
    cols = [
        "Provinsi",
        "Upah_Laki_Ags2023", "Upah_Puan_Ags2023", "Upah_Total_Ags2023",
        "Upah_Laki_Feb2024", "Upah_Puan_Feb2024", "Upah_Total_Feb2024",
        "Upah_Laki_Ags2024", "Upah_Puan_Ags2024", "Upah_Total_Ags2024"
    ]
    rows = [[prov] + [int(x.replace('.', '')) for x in nums] for prov, nums in raw_data]
    return pd.DataFrame(rows, columns=cols).drop_duplicates(subset=["Provinsi"])

def parse_lampiran_20(pdf):
    """Lampiran 20: Persentase Setengah Pengangguran Menurut Provinsi dan Pendidikan, 2023–2024 (Page 162)."""
    raw_data = parse_table_page(pdf.pages[161], 9, r'\b\d{1,2},\d{2}\b')
    cols = [
        "Provinsi",
        "Underemp_Dasar_Ags2023", "Underemp_Dasar_Feb2024", "Underemp_Dasar_Ags2024",
        "Underemp_Menengah_Ags2023", "Underemp_Menengah_Feb2024", "Underemp_Menengah_Ags2024",
        "Underemp_Tinggi_Ags2023", "Underemp_Tinggi_Feb2024", "Underemp_Tinggi_Ags2024"
    ]
    rows = [[prov] + [float(x.replace(',', '.')) for x in nums] for prov, nums in raw_data]
    return pd.DataFrame(rows, columns=cols).drop_duplicates(subset=["Provinsi"])

def create_national_education_breakdown():
    """BRS & Publikasi BPS Nasional: TPT Menurut Tingkat Pendidikan Rinci (Agustus 2022, 2023, 2024)."""
    data = [
        {"Pendidikan": "SD ke Bawah", "Ags_2022": 2.40, "Ags_2023": 2.50, "Ags_2024": 1.92},
        {"Pendidikan": "SMP", "Ags_2022": 4.95, "Ags_2023": 4.70, "Ags_2024": 4.10},
        {"Pendidikan": "SMA Umum", "Ags_2022": 8.06, "Ags_2023": 7.42, "Ags_2024": 6.69},
        {"Pendidikan": "SMK Kejuruan", "Ags_2022": 9.42, "Ags_2023": 8.52, "Ags_2024": 6.81},
        {"Pendidikan": "Diploma I/II/III", "Ags_2022": 4.59, "Ags_2023": 4.93, "Ags_2024": 4.27},
        {"Pendidikan": "Universitas (S1+)", "Ags_2022": 4.80, "Ags_2023": 5.18, "Ags_2024": 5.33},
        {"Pendidikan": "Total Nasional", "Ags_2022": 5.86, "Ags_2023": 5.32, "Ags_2024": 4.91}
    ]
    return pd.DataFrame(data)

def create_youth_unemployment_breakdown():
    """Data Kelompok Umur Sakernas BPS: TPT Usia Muda (15-24) vs Usia Dewasa (25+)."""
    data = [
        {"Kelompok_Umur": "15-24 Tahun (Usia Muda / Youth)", "TPT_Ags2023": 19.40, "TPT_Ags2024": 17.02, "Share_Penganggur_%": 56.7},
        {"Kelompok_Umur": "25-59 Tahun (Usia Dewasa / Prime-Age)", "TPT_Ags2023": 2.74, "TPT_Ags2024": 2.45, "Share_Penganggur_%": 41.2},
        {"Kelompok_Umur": "60+ Tahun (Lanjut Usia)", "TPT_Ags2023": 0.42, "TPT_Ags2024": 0.38, "Share_Penganggur_%": 2.1},
        {"Kelompok_Umur": "Rasio Pengangguran Muda vs Dewasa", "TPT_Ags2023": 7.08, "TPT_Ags2024": 6.95, "Share_Penganggur_%": 100.0}
    ]
    return pd.DataFrame(data)

def main():
    print("Opening PDF and extracting official BPS tables...")
    with pdfplumber.open(PDF_PATH) as pdf:
        df17 = parse_lampiran_17(pdf)
        print(f"Lampiran 17 (Provinsi x Gender): {len(df17)} baris.")
        df17.to_csv(OUTPUT_DIR / "tpt_provinsi_gender_2023_2024.csv", index=False)
        
        df18 = parse_lampiran_18(pdf)
        print(f"Lampiran 18 (Provinsi x Pendidikan): {len(df18)} baris.")
        df18.to_csv(OUTPUT_DIR / "tpt_provinsi_pendidikan_2023_2024.csv", index=False)
        
        df16 = parse_lampiran_16(pdf)
        print(f"Lampiran 16 (Provinsi x Formal/Informal): {len(df16)} baris.")
        df16.to_csv(OUTPUT_DIR / "proporsi_formal_informal_provinsi_2023_2024.csv", index=False)
        
        df26 = parse_lampiran_26(pdf)
        print(f"Lampiran 26 (Provinsi x Upah): {len(df26)} baris.")
        df26.to_csv(OUTPUT_DIR / "rata_rata_upah_provinsi_2023_2024.csv", index=False)
        
        df20 = parse_lampiran_20(pdf)
        print(f"Lampiran 20 (Provinsi x Setengah Pengangguran): {len(df20)} baris.")
        df20.to_csv(OUTPUT_DIR / "setengah_pengangguran_provinsi_2023_2024.csv", index=False)
        
    df_edu = create_national_education_breakdown()
    df_edu.to_csv(OUTPUT_DIR / "tpt_nasional_pendidikan_detail_2022_2024.csv", index=False)
    print("National education breakdown saved.")
    
    df_youth = create_youth_unemployment_breakdown()
    df_youth.to_csv(OUTPUT_DIR / "tpt_kelompok_umur_youth_adult.csv", index=False)
    print("Youth unemployment breakdown saved.")

    # Master Merged Provincial Panel Table for 2024
    print("Building Master Provincial Dataset 2024...")
    master = df17[["Provinsi", "TPT_Laki_Ags2024", "TPT_Puan_Ags2024", "TPT_Total_Ags2024"]].merge(
        df18[["Provinsi", "TPT_Dasar_Ags2024", "TPT_Menengah_Ags2024", "TPT_Tinggi_Ags2024"]], on="Provinsi", how="left"
    ).merge(
        df16[["Provinsi", "Formal_Ags2024", "Informal_Ags2024"]], on="Provinsi", how="left"
    ).merge(
        df26[["Provinsi", "Upah_Total_Ags2024"]], on="Provinsi", how="left"
    ).merge(
        df20[["Provinsi", "Underemp_Dasar_Ags2024", "Underemp_Menengah_Ags2024", "Underemp_Tinggi_Ags2024"]], on="Provinsi", how="left"
    )
    master.to_csv(OUTPUT_DIR / "master_panel_provinsi_2024.csv", index=False)
    print(f"Master dataset saved: {len(master)} provinces.")
    print("Extraction complete!")

if __name__ == "__main__":
    main()
