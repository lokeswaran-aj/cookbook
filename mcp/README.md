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

Alternatively, you can add to your host MCP configurationsfile:

```json
"addition-mcp": {
  "command": "uv",
  "args": [
    "--directory",
    "/PATH/TO/cookbook/mcp/stdio-mcp-example",
    "run",
    "server.py"
  ],
  "disabled": false
}
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

### 3. Simple MCP

This simple MCP server has tools, resources, and prompts. To run the MCP in Simple mode, run the following command:

```bash
make simple-mcp-example
```

This will start the MCP server under the `simple-mcp-example` directory. Then open the MCP inspector link in the terminal.

Alternatively, you can use the following MCP configuration to use the MCP in Cluade desktop or Cursor:

```json
{
  "mcpServers": {
    "simple-mcp-example": {
      "command": "/PATH/TO/uv", # you can find the path to uv in the terminal by running `which uv`(macOS) or `where uv`(Windows). For eg: '/opt/homebrew/bin/uv'
      "args": [
        "--directory",
        "/PATH/TO/cookbook/mcp/simple-mcp-example",
        "run",
        "server.py"
      ]
    }
  }
}
```
