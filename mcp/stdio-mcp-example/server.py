import requests
from fastmcp import FastMCP

mcp = FastMCP("URL Shortener")


@mcp.tool
def shorten_url(url: str) -> str:
    """Shorten a URL"""
    base_url = "https://spoo.me/"

    payload = {
        "url": url,
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.request("POST", base_url, data=payload, headers=headers)

    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")  # set the transport to stdio
