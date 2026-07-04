from pathlib import Path

from skills.quality_analysis import analyze_quality_data


class QualityAgent:
    """
    Quality Agent for FactoryOps AI.
    Responsible for analyzing manufacturing quality.
    """

    def analyze(self):
        project_root = Path(__file__).resolve().parents[2]

        csv_file = (
            project_root
            / "datasets"
            / "quality"
            / "manufacturing_defects.csv"
        )

        return analyze_quality_data(csv_file)