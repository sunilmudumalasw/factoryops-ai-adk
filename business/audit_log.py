from datetime import datetime


def log_decision(action, decision):
    """
    Record executive decisions.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"[{timestamp}] "
        f"{action} | "
        f"{decision['recommended_action']} | "
        f"Risk={decision['risk_level']}"
    )