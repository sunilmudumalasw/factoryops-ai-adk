from pathlib import Path

from skills.inventory_analysis import analyze_inventory_data


def analyze_factory_inventory():
    """
    Analyze the default FactoryOps inventory dataset.
    """

    project_root = Path(__file__).resolve().parents[1]

    csv_file = (
        project_root
        / "datasets"
        / "inventory"
        / "inventory.csv"
    )

    return analyze_inventory_data(csv_file)