from pathlib import Path

from skills.quality_analysis import analyze_quality_data


def analyze_factory_quality():
    """
    Analyze the default FactoryOps quality dataset.
    """

    project_root = Path(__file__).resolve().parents[1]

    csv_file = (
        project_root
        / "datasets"
        / "quality"
        / "manufacturing_defects.csv"
    )

    return analyze_quality_data(csv_file)