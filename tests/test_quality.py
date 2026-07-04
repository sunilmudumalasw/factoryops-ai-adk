import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from skills.quality_analysis import analyze_quality_data

csv_file = (
    PROJECT_ROOT
    / "datasets"
    / "quality"
    / "manufacturing_defects.csv"
)

summary = analyze_quality_data(csv_file)

print(summary)