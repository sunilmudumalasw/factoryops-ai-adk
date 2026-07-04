import asyncio
import sys
from pathlib import Path

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def main():

    project_root = Path(__file__).resolve().parents[1]

    server_path = project_root / "mcp" / "server.py"

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            print("Connected to FactoryOps MCP Server")

            result = await session.call_tool(
                "production_summary",
                arguments={}
            )

            print("\nResponse from MCP Server:\n")

            for content in result.content:
                if hasattr(content, "text"):
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())