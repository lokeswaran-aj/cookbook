from fastmcp import Context, FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent

mcp = FastMCP(name="Calculator")


@mcp.tool(
    name="multiply",
    description="Multiplies two numbers together",
    annotations={
        "title": "Multiply two numbers",  # Human-readable title for the tool
        "readOnlyHint": False,  # Whether the tool is modifying its environment
        "openWorldHint": True,  # Whether the tool interacts with the internet
        "destructiveHint": False,  # Whether the tool is performing destructive actions
        "idempotentHint": True,  # Whether repeated calls to the tool will have the same effect
    },
)
def multiply_integers(a: int, b: int) -> int:
    return a * b


@mcp.resource(
    name="get_config",
    description="Provides the application configuration",
    uri="data://config",  # The URI of the resource
)
async def get_config(ctx: Context) -> dict:
    return {"theme": "dark", "version": "1.0", "request_id": ctx.request_id}


@mcp.resource(
    name="get_user_profile",
    description="Retrieves a user's profile by ID",
    uri="users://{user_id}/profile",  # The dynamic URI of the resource
)
def get_user_profile(user_id: int) -> dict:
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}


@mcp.prompt(
    name="multiple_integers",
    description="Creates a prompt asking for analysis of numerical data",
)
def multiple_integers(a: int, b: int) -> PromptMessage:
    content = f"Please multiply these data points:{a} and {b}"
    return PromptMessage(role="user", content=TextContent(type="text", text=content))


@mcp.prompt(
    name="generate_code_request",
    description="Generates a user message requesting code generation",
)
def generate_code_request(language: str, task_description: str) -> PromptMessage:
    content = f"Write a {language} function that performs the following task: {task_description}"
    return PromptMessage(role="user", content=TextContent(type="text", text=content))


if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()
