#!/usr/bin/env python3
"""
Headless runner for Jupyter Notebooks.
Executes all notebooks in notebooks/ (or a targeted notebook) end-to-end
and saves all executed cells, outputs, and embedded visualizations in-place.
"""

import sys
import time
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT_DIR = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
DEFAULT_NOTEBOOK = NOTEBOOKS_DIR / "analisis_ketenagakerjaan_action2026.ipynb"

def run_notebook(notebook_path: Path = DEFAULT_NOTEBOOK, output_path: Path = None, verify_assets: bool = False) -> dict:
    if output_path is None:
        output_path = notebook_path
        
    print(f"📖 Reading notebook: {notebook_path.relative_to(ROOT_DIR)}")
    if not notebook_path.exists():
        print(f"❌ Error: Notebook not found at {notebook_path}")
        sys.exit(1)

    nb = nbformat.read(notebook_path, as_version=4)
    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    print(f"⚙️  Found {len(nb.cells)} total cells ({len(code_cells)} code cells).")
    print(f"🚀 Executing notebook with kernel 'python3'...")

    start_time = time.time()
    
    # Execute notebook within its parent directory to ensure relative path resolution
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(notebook_path.parent)}}
    )
    
    try:
        client.execute()
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        raise e

    elapsed = time.time() - start_time
    print(f"✅ Execution finished in {elapsed:.2f} seconds.")

    # Save executed notebook
    nbformat.write(nb, output_path)
    print(f"💾 Saved executed notebook with all outputs to: {output_path.relative_to(ROOT_DIR)}")
    if verify_assets:
        charts_dir = ROOT_DIR / "assets" / "charts"
        charts = sorted(list(charts_dir.glob("*.png")))
        print(f"\n📊 Verified {len(charts)} exported charts in {charts_dir.relative_to(ROOT_DIR)}:")
        for chart in charts:
            size_kb = chart.stat().st_size / 1024
            print(f"   - {chart.name} ({size_kb:.1f} KB)")
            
    return {
        "notebook": notebook_path.name,
        "total_cells": len(nb.cells),
        "code_cells": len(code_cells),
        "elapsed": elapsed,
        "status": "success"
    }

def main():
    args = sys.argv[1:]
    if args and args[0] not in ("--all", "-a"):
        target = Path(args[0])
        if not target.is_absolute():
            candidate = NOTEBOOKS_DIR / target.name
            if candidate.exists():
                target = candidate
            elif (ROOT_DIR / target).exists():
                target = ROOT_DIR / target
        run_notebook(target, verify_assets=True)
        return

    # Default / --all: run all notebooks in notebooks/
    notebooks = sorted(list(NOTEBOOKS_DIR.glob("*.ipynb")))
    if not notebooks:
        print(f"⚠️  No notebooks found in {NOTEBOOKS_DIR}")
        return

    print(f"==================================================")
    print(f"🚀 Running all {len(notebooks)} notebooks in {NOTEBOOKS_DIR.relative_to(ROOT_DIR)}/")
    print(f"==================================================")
    
    results = []
    total_start = time.time()
    for idx, nb_path in enumerate(notebooks, 1):
        print(f"\n>>> [{idx}/{len(notebooks)}] Executing: {nb_path.name}")
        res = run_notebook(nb_path, verify_assets=False)
        results.append(res)
        
    total_elapsed = time.time() - total_start
    print(f"\n==================================================")
    print(f"🏁 Execution Summary ({total_elapsed:.2f}s total):")
    print(f"==================================================")
    for r in results:
        print(f" ✅ {r['notebook']}: {r['code_cells']} code cells, {r['elapsed']:.2f}s")
        
    # Final asset check
    charts_dir = ROOT_DIR / "assets" / "charts"
    charts = sorted(list(charts_dir.glob("*.png")))
    print(f"\n📊 Verified {len(charts)} exported charts in {charts_dir.relative_to(ROOT_DIR)}:")
    for chart in charts:
        size_kb = chart.stat().st_size / 1024
        print(f"   - {chart.name} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
