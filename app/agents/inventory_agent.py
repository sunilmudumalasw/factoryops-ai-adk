from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from tools.inventory_tool import analyze_factory_inventory

inventory_tool = FunctionTool(
    func=analyze_factory_inventory
)

inventory_agent = Agent(
    name="inventory_agent",
    model="gemini-2.5-flash",
    description="Manufacturing Inventory Specialist",

    instruction="""
You are the Inventory Manager.

You are responsible for:

- Material availability
- Lead times
- Supplier readiness
- Inventory health

Always use the inventory analysis tool whenever a user asks about inventory.

Provide concise inventory recommendations.
""",

    tools=[
        inventory_tool
    ]
)