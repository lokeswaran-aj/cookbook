import requests
from fastmcp import FastMCP

mcp = FastMCP("F1 Race")


@mcp.tool
def get_race_results(round: int = 1, year: int = 2025) -> dict:
    """Get the results of a F1 race"""
    response = requests.get(f"https://f1api.dev/api/{year}/{round}/race")
    return response.json()


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",  # set the transport to streamable-http
        host="127.0.0.1",
        port=8080,
    )
