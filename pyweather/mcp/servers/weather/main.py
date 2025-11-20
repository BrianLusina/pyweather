from pyweather.mcp.servers.weather.server import mcp_server


if __name__ == "__main__":
    mcp_server.run(transport="stdio")
