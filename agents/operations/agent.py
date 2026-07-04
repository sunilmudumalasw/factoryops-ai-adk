from pathlib import Path

from skills.production_analysis import analyze_production_data


class OperationsAgent:
    """
    Operations Agent for FactoryOps AI.
    Responsible for analyzing production performance.
    """

    def analyze(self):
        project_root = Path(__file__).resolve().parents[2]

        csv_file = (
            project_root
            / "datasets"
            / "production"
            / "intelligent_manufacturing.csv"
        )

        return analyze_production_data(csv_file)