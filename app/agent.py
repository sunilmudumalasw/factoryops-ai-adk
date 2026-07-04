from google.adk.agents import Agent

from app.agents.operations_agent import operations_agent
from app.agents.inventory_agent import inventory_agent
from app.agents.quality_agent import quality_agent
from google.adk.tools import FunctionTool
from tools.factory_health_tool import analyze_factory_health

factory_health_tool = FunctionTool(
    func=analyze_factory_health
)
root_agent = Agent(
    name="manufacturing_coo",
    model="gemini-2.5-flash",
    description="FactoryOps AI - Multi-Agent Manufacturing COO",

    instruction="""
You are the Manufacturing COO for FactoryOps AI.

You supervise three specialist managers:

- Operations Manager
- Inventory Manager
- Quality Manager

Delegate user requests to the appropriate specialist.

If the user requests an overall factory assessment or Factory Health Report,
coordinate the specialists and provide an executive summary.

Always provide concise, business-oriented recommendations.
""",
    tools=[
    factory_health_tool,
],
    sub_agents=[
        operations_agent,
        inventory_agent,
        quality_agent,
    ]
)