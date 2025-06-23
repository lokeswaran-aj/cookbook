.PHONY: install stdio-mcp-example http-mcp-example simple-mcp-example restaurant-mcp

install:
	uv sync

stdio-mcp-example:
	fastmcp dev stdio-mcp-example/server.py

http-mcp-server:
	uv run http-mcp-example/server.py

http-mcp-example:
	fastmcp dev http-mcp-example/server.py

simple-mcp-example:
	fastmcp dev simple-mcp-example/server.py


restaurant-mcp:
	fastmcp dev restaurant-mcp/server.py