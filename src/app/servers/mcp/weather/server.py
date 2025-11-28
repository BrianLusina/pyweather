import logging
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("WeatherAssistant")

if __name__ == "__main__":
    logging.getLogger("weather-mcp-server").setLevel(logging.WARNING)
    mcp.run(transport="stdio")
