"""Export final tables to CSV for Power BI."""

from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "transformed_data"


def export_tables(tables: dict[str, pd.DataFrame], output_dir: Path = OUTPUT_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, df in tables.items():
        df.to_csv(output_dir / filename, index=False)
        print(f"Exported {filename} ({df.shape[0]:,} rows)")
