from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from tools.production_tool import analyze_factory_production
from tools.inventory_tool import analyze_factory_inventory
from tools.quality_tool import analyze_factory_quality
from tools.factory_health_tool import analyze_factory_health

production_tool = FunctionTool(
    func=analyze_factory_production
)

inventory_tool = FunctionTool(
    func=analyze_factory_inventory
)
quality_tool = FunctionTool(
    func=analyze_factory_quality
)

factory_health_tool = FunctionTool(
    func=analyze_factory_health
)

root_agent = Agent(
    name="factoryops_ai",
    model="gemini-2.5-flash",
    description="FactoryOps AI Manufacturing COO",

    
    instruction="""
You are FactoryOps AI, an AI Manufacturing COO.

You help manufacturing leaders:

- Analyze production performance.
- Analyze inventory health.
- Analyze manufacturing quality.

Always use the appropriate tool when the user requests production, inventory, or quality analysis.

Never invent manufacturing metrics when a tool is available.

Keep responses concise and actionable.

If the user asks for a Factory Health Report, an Executive Summary, or an overall manufacturing status, use the Factory Health tool.

""",

    tools=[
        production_tool,
        inventory_tool,
        quality_tool,
        factory_health_tool,
    ]
)