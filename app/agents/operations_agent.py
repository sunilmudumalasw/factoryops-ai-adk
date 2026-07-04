from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from tools.production_tool import analyze_factory_production

production_tool = FunctionTool(
    func=analyze_factory_production
)

operations_agent = Agent(
    name="operations_agent",
    model="gemini-2.5-flash",
    description="Manufacturing Operations Specialist",

    instruction="""
You are the Operations Manager.

You are responsible for:

- Production performance
- Machine efficiency
- Manufacturing throughput

Always use the production analysis tool whenever a user asks about production.

Provide concise manufacturing recommendations.
""",

    tools=[
        production_tool
    ]
)