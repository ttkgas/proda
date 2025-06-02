from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

server_params = StdioServerParameters(
    command="uv",  # Executable
    args=["run demo_server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)
async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("example/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Call a tool
            tools = await session.list_tools()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())