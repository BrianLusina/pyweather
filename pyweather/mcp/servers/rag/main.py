from pyweather.mcp.servers.rag.server import mcp
import logging


if __name__ == "__main__":
    logging.getLogger("mcp").setLevel(logging.WARNING)
    # The server will run and listen for requests from the client over stdio
    mcp.run(transport="stdio")
