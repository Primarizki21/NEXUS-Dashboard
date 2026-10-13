#!/usr/bin/env python3
"""
Bundle and export a clean ZIP package of the action-infografis-2026 project.
Excludes .venv, .git, references/, cache, and checkpoints.
"""

import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_ZIP = ROOT_DIR / "action-infografis-2026-bundle.zip"

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "ENV",
    "env",
    "__pycache__",
    ".ipynb_checkpoints",
    "references",
}

EXCLUDE_EXTS = {
    ".pyc",
    ".pyo",
    ".pyd",
    ".zip",
    ".Identifier",
}

def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    if path.suffix in EXCLUDE_EXTS:
        return True
    if ":Zone.Identifier" in path.name:
        return True
    return False

def make_bundle():
    print(f"Creating clean bundle: {OUTPUT_ZIP.name}...")
    file_count = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in ROOT_DIR.rglob("*"):
            if p.is_dir():
                continue
            rel_path = p.relative_to(ROOT_DIR)
            if is_excluded(rel_path):
                continue
            zf.write(p, arcname=rel_path)
            file_count += 1
            total_uncompressed_bytes += p.stat().st_size

    zip_size_mb = OUTPUT_ZIP.stat().st_size / (1024 * 1024)
    print(f"Bundle created successfully!")
    print(f"- Total files included: {file_count}")
    print(f"- Compressed ZIP size : {zip_size_mb:.2f} MB")
    print(f"- Output path         : {OUTPUT_ZIP}")

if __name__ == "__main__":
    make_bundle()
