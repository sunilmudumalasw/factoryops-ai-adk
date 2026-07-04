import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from skills.inventory_analysis import analyze_inventory_data

csv_file = (
    PROJECT_ROOT
    / "datasets"
    / "inventory"
    / "inventory.csv"
)

summary = analyze_inventory_data(csv_file)

print(summary)