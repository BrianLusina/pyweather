import logging
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server with a descriptive name
mcp = FastMCP("TaskManagementAssistant")

if __name__ == "__main__":
    logging.getLogger("task-mcp-server").setLevel(logging.WARNING)
    mcp.run(transport="stdio")
