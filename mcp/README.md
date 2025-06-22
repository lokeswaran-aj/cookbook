# MCP Examples

This is a collection of MCP examples.

## Installation

```bash
make install
```

## Examples

### 1. STDIO MCP

To run the MCP in STDIO mode, run the following command:

```bash
make stdio-mcp-example
```

This will start the MCP server under the `stdio-mcp-example` directory. Then open the MCP inspector link in the terminal.

Alternatively, you can run the following command:

```bash
fastmcp dev stdio-mcp-example/server.py
```

### 2. Streamable HTTP MCP

To run the MCP in Streamable HTTP mode, firstly run the server:

```bash
make http-mcp-server
```

Now your server is running on `http://localhost:8080/mcp`. You can set the MCP server in the Cursor settings.

```json
{
  "mcpServers": {
    "calculator": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

Optionally, you can test the server in the MCP inspector. For that, run the following command:

```bash
make http-mcp-example
```

Make sure to set the transport to `Streamable HTTP` and the URL to `http://localhost:8080/mcp`.
