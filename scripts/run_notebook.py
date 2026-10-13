#!/usr/bin/env python3
"""
Headless runner for Jupyter Notebooks.
Executes notebooks/analisis_ketenagakerjaan_action2026.ipynb end-to-end
and saves all executed cells, outputs, and embedded visualizations in-place.
"""

import sys
import time
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_NOTEBOOK = ROOT_DIR / "notebooks" / "analisis_ketenagakerjaan_action2026.ipynb"

def run_notebook(notebook_path: Path = DEFAULT_NOTEBOOK, output_path: Path = None):
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

    # Verify generated assets
    charts_dir = ROOT_DIR / "assets" / "charts"
    charts = sorted(list(charts_dir.glob("*.png")))
    print(f"\n📊 Verified {len(charts)} exported charts in {charts_dir.relative_to(ROOT_DIR)}:")
    for chart in charts:
        size_kb = chart.stat().st_size / 1024
        print(f"   - {chart.name} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_NOTEBOOK
    run_notebook(target)
