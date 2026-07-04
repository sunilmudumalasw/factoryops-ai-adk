from pathlib import Path
import pandas as pd


def analyze_production_data(csv_path):
    df = pd.read_csv(csv_path)

    summary = {
        "total_machines": df["Machine_ID"].nunique(),
        "average_speed": float(round(df["Production_Speed_units_per_hr"].mean(), 2)),
        "average_defect_rate": float(round(df["Quality_Control_Defect_Rate_%"].mean(), 2)),
        "average_error_rate": float(round(df["Error_Rate_%"].mean(), 2)),
        "average_predictive_score": float(round(df["Predictive_Maintenance_Score"].mean(), 2)),
        "efficiency_distribution": df["Efficiency_Status"].value_counts().to_dict(),
    }

    # Factory Health
    if summary["average_error_rate"] > 10:
        summary["status"] = "Critical"
        summary["recommendation"] = (
            "Immediate maintenance inspection recommended."
        )
    elif summary["average_defect_rate"] > 5:
        summary["status"] = "Warning"
        summary["recommendation"] = (
            "Review production quality processes."
        )
    else:
        summary["status"] = "Optimal"
        summary["recommendation"] = (
            "Factory operating normally."
        )

    return summary