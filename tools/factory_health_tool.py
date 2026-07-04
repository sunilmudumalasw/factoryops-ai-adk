from tools.production_tool import analyze_factory_production
from tools.inventory_tool import analyze_factory_inventory
from tools.quality_tool import analyze_factory_quality


def analyze_factory_health():
    """
    Generate a complete Factory Health Report.
    """

    production = analyze_factory_production()
    inventory = analyze_factory_inventory()
    quality = analyze_factory_quality()

    # Determine Overall Status
    statuses = [
        production["status"],
        inventory["status"],
        quality["status"],
    ]

    if "Critical" in statuses:
        overall_status = "Critical"
    elif "Warning" in statuses or "Attention Required" in statuses:
        overall_status = "Warning"
    else:
        overall_status = "Optimal"

    # Determine Highest Priority
    if quality["status"] == "Critical":
        top_priority = "Quality"
    elif inventory["status"] == "Attention Required":
        top_priority = "Inventory"
    else:
        top_priority = "Production"

    executive_summary = (
        f"Overall Factory Status: {overall_status}. "
        f"Highest Priority: {top_priority}. "
        f"Production status is {production['status']}. "
        f"Inventory status is {inventory['status']}. "
        f"Quality status is {quality['status']}."
    )

    return {
        "overall_status": overall_status,
        "top_priority": top_priority,
        "executive_summary": executive_summary,
        "production": production,
        "inventory": inventory,
        "quality": quality,
    }