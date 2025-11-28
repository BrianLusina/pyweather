import logging
from app.servers.mcp.tasks.server import mcp


if __name__ == "__main__":
    print("Starting MCP Task Server...")
    logging.getLogger("task-mcp-server").setLevel(logging.WARNING)
    # The server will run and listen for requests from the client over stdio
    mcp.run(transport="stdio")
