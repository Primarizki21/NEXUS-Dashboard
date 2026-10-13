"""
Builds the complete longitudinal panel of TPT (Tingkat Pengangguran Terbuka)
per province in Indonesia across 2017-2024 (Sakernas Agustus).
Combines:
- 2017-2021: data_tpt_prov_2017_2021.pdf (Tabel 5.6)
- 2022-2023: data_tpt_prov_2022_2023.pdf (Tabel 3.1)
- 2023-2024: data/clean/tpt_provinsi_gender_2023_2024.csv (Lampiran 17)
"""

import pdfplumber
import pandas as pd
import re
from pathlib import Path

OUTPUT_DIR = Path("data/clean")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROV_34_CANONICAL = [
    "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan",
    "Bengkulu", "Lampung", "Kep. Bangka Belitung", "Kepulauan Riau", "DKI Jakarta",
    "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali",
    "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
    "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara",
    "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo",
    "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua", "Indonesia"
]

SORTED_CANONICAL = sorted(PROV_34_CANONICAL, key=len, reverse=True)

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

def parse_2017_2021():
    pdf_path = "data_tpt_prov_2017_2021.pdf"
    with pdfplumber.open(pdf_path) as pdf:
        p138 = pdf.pages[137]
        rows = clean_page_words(p138)
        
    name_map = {
        "Nanggroe Aceh Darussalam": "Aceh",
        "Bangka Belitung": "Kep. Bangka Belitung",
        "D.I. Yogyakarta": "DI Yogyakarta",
        "Nusa Tenggara Batrat": "Nusa Tenggara Barat",
        "Nusa Tenggarha Timur": "Nusa Tenggara Timur",
        "Sulawesi selatan": "Sulawesi Selatan"
    }
    
    data = {}
    i = 0
    while i < len(rows):
        text = " ".join(w['text'] for w in rows[i])
        for k, v in name_map.items():
            text = text.replace(k, v)
        text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', text)
        nums = re.findall(r'\b\d{1,2}[.,]\d{2}\b', text)
        
        matched_prov = None
        for canon in SORTED_CANONICAL:
            if re.search(r'\b' + re.escape(canon) + r'\b', text, re.IGNORECASE):
                matched_prov = canon
                break
                
        if matched_prov:
            if len(nums) == 5:
                data[matched_prov] = [float(x.replace(',', '.')) for x in nums]
            elif i + 1 < len(rows):
                next_text = " ".join(w['text'] for w in rows[i+1])
                next_text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', next_text)
                next_nums = re.findall(r'\b\d{1,2}[.,]\d{2}\b', next_text)
                if len(next_nums) == 5:
                    data[matched_prov] = [float(x.replace(',', '.')) for x in next_nums]
                    i += 1
        i += 1
                    
    df = pd.DataFrame.from_dict(data, orient='index', columns=['TPT_2017', 'TPT_2018', 'TPT_2019', 'TPT_2020', 'TPT_2021'])
    df.index.name = 'Provinsi'
    return df.reset_index()

def parse_2022_2023():
    pdf_path = "data_tpt_prov_2022_2023.pdf"
    with pdfplumber.open(pdf_path) as pdf:
        p33 = pdf.pages[32]
        rows = clean_page_words(p33)
        
    name_map = {
        "Bangka Belitung": "Kep. Bangka Belitung",
        "D.I. Yogyakarta": "DI Yogyakarta",
        "Bantebn": "Banten",
        "uNusa Tenggara Timur": "Nusa Tenggara Timur"
    }
    
    data = {}
    i = 0
    while i < len(rows):
        text = " ".join(w['text'] for w in rows[i])
        for k, v in name_map.items():
            text = text.replace(k, v)
        text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', text)
        nums = re.findall(r'\b\d{1,2}[.,]\d{2}\b', text)
        
        matched_prov = None
        for canon in SORTED_CANONICAL:
            if re.search(r'\b' + re.escape(canon) + r'\b', text, re.IGNORECASE):
                matched_prov = canon
                break
                
        if matched_prov:
            if len(nums) == 2:
                data[matched_prov] = [float(x.replace(',', '.')) for x in nums]
            elif i + 1 < len(rows):
                next_text = " ".join(w['text'] for w in rows[i+1])
                next_text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', next_text)
                next_nums = re.findall(r'\b\d{1,2}[.,]\d{2}\b', next_text)
                if len(next_nums) == 2:
                    data[matched_prov] = [float(x.replace(',', '.')) for x in next_nums]
                    i += 1
        i += 1
                    
    df = pd.DataFrame.from_dict(data, orient='index', columns=['TPT_2022', 'TPT_2023_ref'])
    df.index.name = 'Provinsi'
    return df.reset_index()

def main():
    print("Extracting 2017-2021 series...")
    df_17_21 = parse_2017_2021()
    print(f"2017-2021 matched: {len(df_17_21)} provinces.")
    
    print("Extracting 2022-2023 series...")
    df_22_23 = parse_2022_2023()
    print(f"2022-2023 matched: {len(df_22_23)} provinces.")
    
    print("Loading 2023-2024 clean dataset...")
    df_23_24 = pd.read_csv("data/clean/tpt_provinsi_gender_2023_2024.csv")
    df_23_24_sub = df_23_24[["Provinsi", "TPT_Total_Ags2023", "TPT_Total_Ags2024"]].rename(
        columns={"TPT_Total_Ags2023": "TPT_2023", "TPT_Total_Ags2024": "TPT_2024"}
    )
    
    # Merge all into balanced longitudinal panel 2017-2024
    merged = df_17_21.merge(df_22_23[["Provinsi", "TPT_2022"]], on="Provinsi", how="left")
    merged = merged.merge(df_23_24_sub, on="Provinsi", how="left")
    
    # Check consistency
    print("\nMerged Panel Shape:", merged.shape)
    missing = [p for p in PROV_34_CANONICAL if p not in set(merged['Provinsi'])]
    print("Missing provinces:", missing)
    print("\nNull count per column:")
    print(merged.isnull().sum())
    
    # Save clean balanced longitudinal panel
    output_path = OUTPUT_DIR / "panel_tpt_provinsi_2017_2024.csv"
    merged.to_csv(output_path, index=False)
    print(f"\nLongitudinal Panel 2017-2024 successfully saved to: {output_path}")

if __name__ == "__main__":
    main()
