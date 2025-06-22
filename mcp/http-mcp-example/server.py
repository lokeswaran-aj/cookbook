from fastmcp import FastMCP

mcp = FastMCP("Calculator")  # define host and port


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8080,
    )  # set the transport to streamable-http
