import pandas as pd


def analyze_inventory_data(csv_path):
    df = pd.read_csv(csv_path)

    # Materials below reorder level
    low_stock = df[df["CurrentStock"] < df["ReorderLevel"]]

    summary = {
        "total_materials": len(df),
        "low_stock_count": len(low_stock),
        "low_stock_materials": low_stock["Material"].tolist(),
        "average_lead_time": float(round(df["LeadTime"].mean(), 2)),
    }

    if len(low_stock) == 0:
        summary["status"] = "Healthy"
        summary["recommendation"] = "Inventory levels are sufficient."
    else:
        summary["status"] = "Attention Required"
        summary["recommendation"] = (
            "Reorder low stock materials to avoid production delays."
        )

    return summary