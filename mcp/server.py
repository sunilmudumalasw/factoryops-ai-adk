from mcp.server.fastmcp import FastMCP

from production import get_production_summary
from inventory import get_inventory_summary
from quality import get_quality_summary
from factory_health import get_factory_health_summary

# Create the Manufacturing MCP Server
mcp = FastMCP("FactoryOps Manufacturing MCP")


@mcp.tool()
def production_summary() -> dict:
    """Returns the production summary."""
    return get_production_summary()


@mcp.tool()
def inventory_summary() -> dict:
    """Returns the inventory summary."""
    return get_inventory_summary()


@mcp.tool()
def quality_summary() -> dict:
    """Returns the quality summary."""
    return get_quality_summary()

@mcp.tool()
def factory_health_summary() -> dict:
    """Returns the complete factory health report."""
    return get_factory_health_summary()

if __name__ == "__main__":
    mcp.run(transport="stdio")