from agents.operations.agent import OperationsAgent
from agents.inventory.agent import InventoryAgent
from agents.quality.agent import QualityAgent


class ManufacturingCOOAgent:
    """
    FactoryOps AI Coordinator.
    Combines the results from all specialist agents.
    """

    def analyze_factory(self):

        operations = OperationsAgent().analyze()
        inventory = InventoryAgent().analyze()
        quality = QualityAgent().analyze()

        report = f"""
=========================================
        FACTORY HEALTH REPORT
=========================================

PRODUCTION
----------
Status              : {operations['status']}
Machines            : {operations['total_machines']}
Average Speed       : {operations['average_speed']} units/hr
Recommendation      : {operations['recommendation']}

INVENTORY
---------
Status              : {inventory['status']}
Low Stock Items     : {", ".join(inventory['low_stock_materials'])}
Recommendation      : {inventory['recommendation']}

QUALITY
-------
Status              : {quality['status']}
Critical Defects    : {quality['critical_defects']}
Average Repair Cost : ${quality['average_repair_cost']}
Recommendation      : {quality['recommendation']}
"""

        return report