import logging
from app.servers.mcp.weather.server import mcp


if __name__ == "__main__":
    logging.getLogger("rag-mcp-server").setLevel(logging.WARNING)
    mcp.run(transport="stdio")
