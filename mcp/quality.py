import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from tools.quality_tool import analyze_factory_quality


def get_quality_summary():
    """
    Returns the FactoryOps quality summary using the
    same business logic as the ADK tools.
    """
    return analyze_factory_quality()