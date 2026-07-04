import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from tools.inventory_tool import analyze_factory_inventory


def get_inventory_summary():
    """
    Returns the FactoryOps inventory summary using the
    same business logic as the ADK tools.
    """
    return analyze_factory_inventory()