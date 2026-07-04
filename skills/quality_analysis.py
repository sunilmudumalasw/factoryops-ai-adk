import pandas as pd


def analyze_quality_data(csv_path):
    df = pd.read_csv(csv_path)

    summary = {
        "total_defects": len(df),
        "critical_defects": len(df[df["severity"] == "Critical"]),
        "average_repair_cost": float(round(df["repair_cost"].mean(), 2)),
        "defect_types": df["defect_type"].value_counts().to_dict(),
    }

    if summary["critical_defects"] > 20:
        summary["status"] = "Critical"
        summary["recommendation"] = (
            "Immediate quality review required. Investigate critical defects."
        )
    elif summary["critical_defects"] > 5:
        summary["status"] = "Warning"
        summary["recommendation"] = (
            "Monitor quality trends and increase inspections."
        )
    else:
        summary["status"] = "Healthy"
        summary["recommendation"] = (
            "Quality performance is within acceptable limits."
        )

    return summary