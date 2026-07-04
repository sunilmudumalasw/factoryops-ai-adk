from pathlib import Path

from skills.production_analysis import analyze_production_data


def analyze_factory_production():
    """
    Analyze the default FactoryOps production dataset.
    """

    project_root = Path(__file__).resolve().parents[1]

    csv_file = (
        project_root
        / "datasets"
        / "production"
        / "intelligent_manufacturing.csv"
    )

    return analyze_production_data(csv_file)