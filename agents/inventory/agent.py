from pathlib import Path

from skills.inventory_analysis import analyze_inventory_data


class InventoryAgent:
    """
    Inventory Agent for FactoryOps AI.
    Responsible for analyzing inventory status.
    """

    def analyze(self):
        project_root = Path(__file__).resolve().parents[2]

        csv_file = (
            project_root
            / "datasets"
            / "inventory"
            / "inventory.csv"
        )

        return analyze_inventory_data(csv_file)