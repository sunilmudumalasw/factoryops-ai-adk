from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from tools.quality_tool import analyze_factory_quality

quality_tool = FunctionTool(
    func=analyze_factory_quality
)

quality_agent = Agent(
    name="quality_agent",
    model="gemini-2.5-flash",
    description="Manufacturing Quality Specialist",

    instruction="""
You are the Quality Manager.

You are responsible for:

- Product quality
- Defect analysis
- Inspection results
- Repair costs

Always use the quality analysis tool whenever a user asks about quality.

Provide concise quality recommendations.
""",

    tools=[
        quality_tool
    ]
)