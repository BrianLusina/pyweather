from pyweather.mcp.servers.tasks.server import mcp


if __name__ == "__main__":
    print("Starting MCP Task Server...")
    # The server will run and listen for requests from the client over stdio
    mcp.run(transport="stdio")
