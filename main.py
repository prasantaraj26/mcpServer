from fastmcp import FastMCP

mcp = FastMCP("Learning MCP Server")


# Tool: a function the LLM can call
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

@mcp.tool()
def list_directory() -> list:
    """List the contents of current main directory."""
    import os
    try:
        return os.listdir(".")
    except Exception as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def list_files(path_of_dir: str) -> list:
    """List the contents of a files."""
    import os
    try:
        return os.listdir(path_of_dir)
    except Exception as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def get_filesize(path_of_file: str) -> int:
    """Get the size of a file."""
    import os
    try:
        return os.path.getsize(path_of_file)
    except Exception as e:
        return [f"Error: {str(e)}"]
        
@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to fastMCP."


# Resource: static or dynamic data the LLM can read
@mcp.resource("data://config")
def get_config() -> dict:
    """Return server configuration info."""
    return {"version": "0.1.0", "environment": "development"}


# Prompt: a reusable prompt template
@mcp.prompt()
def explain_tool(tool_name: str) -> str:
    """Generate a prompt asking Claude to explain an MCP tool."""
    return f"Please explain what the '{tool_name}' tool does and give an example of how to use it."


if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
