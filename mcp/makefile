.PHONY: install stdio-mcp-example http-mcp-example

install:
	uv sync

stdio-mcp-example:
	fastmcp dev stdio-mcp-example/server.py

http-mcp-server:
	uv run http-mcp-example/server.py

http-mcp-example:
	fastmcp dev http-mcp-example/server.py