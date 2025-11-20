from pyweather.mcp.servers.weather.server import mcp


if __name__ == "__main__":
    mcp.run(transport="stdio")
