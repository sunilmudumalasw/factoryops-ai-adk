import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from skills.production_analysis import analyze_production_data

# Get project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the production dataset
csv_file = PROJECT_ROOT / "datasets" / "production" / "intelligent_manufacturing.csv"

# Run the analysis
summary = analyze_production_data(csv_file)

# Print the results
print(summary)