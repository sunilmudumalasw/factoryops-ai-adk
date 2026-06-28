from google.adk.agents import Agent

root_agent = Agent(
    name="factoryops_hello",
    model="gemini-2.5-flash",
    description="A simple hello world agent.",
    instruction="""
    You are the FactoryOps AI assistant.

    If the user greets you, respond:

    "Hello! Welcome to FactoryOps AI. I'm your Manufacturing COO assistant."

    Keep responses short.
    """
)