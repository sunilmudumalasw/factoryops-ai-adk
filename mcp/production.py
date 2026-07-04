import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from tools.production_tool import analyze_factory_production


def get_production_summary():
    """
    Returns the FactoryOps production summary using the
    same business logic as the ADK tools.
    """
    return analyze_factory_production()