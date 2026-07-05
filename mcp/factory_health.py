import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from tools.factory_health_tool import analyze_factory_health


def get_factory_health_summary():
    """
    Returns the complete Factory Health Report.
    """
    return analyze_factory_health()