from tools.production_tool import analyze_factory_production
from tools.inventory_tool import analyze_factory_inventory
from tools.quality_tool import analyze_factory_quality


def analyze_factory_health():
    """
    Generate a complete Factory Health Report.
    """

    return {
        "production": analyze_factory_production(),
        "inventory": analyze_factory_inventory(),
        "quality": analyze_factory_quality(),
    }