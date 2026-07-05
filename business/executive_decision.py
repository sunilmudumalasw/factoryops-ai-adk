def make_executive_decision(factory_report):
    """
    Evaluate factory health and recommend executive action.
    """

    production_status = factory_report["production"]["status"]
    inventory_status = factory_report["inventory"]["status"]
    quality_status = factory_report["quality"]["status"]

    # Default decision
    decision = {
        "risk_level": "Low",
        "business_priority": "Low",
        "recommended_action": "Continue normal factory operations.",
        "approval_required": False,
        "estimated_business_impact": "Low",
        "reason": "Factory operating within acceptable limits."
    }

    # Highest priority: Quality
    if quality_status == "Critical":
        decision.update({
            "risk_level": "Critical",
            "business_priority": "Immediate",
            "recommended_action": "Launch immediate quality investigation.",
            "approval_required": True,
            "estimated_business_impact": "High",
            "reason": "Critical quality issues detected."
        })

    # Inventory
    elif inventory_status == "Attention Required":
        decision.update({
            "risk_level": "Medium",
            "business_priority": "High",
            "recommended_action": "Reorder critical materials.",
            "approval_required": True,
            "estimated_business_impact": "Medium",
            "reason": "Low inventory could disrupt production."
        })

    # Production
    elif production_status == "Warning":
        decision.update({
            "risk_level": "Medium",
            "business_priority": "Medium",
            "recommended_action": "Monitor production and investigate process deviations.",
            "approval_required": False,
            "estimated_business_impact": "Medium",
            "reason": "Production performance below target."
        })

    return decision