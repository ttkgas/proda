from mcp.server.fastmcp import FastMCP


mcp = FastMCP("demo", port=8001)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    return f"Good day, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")