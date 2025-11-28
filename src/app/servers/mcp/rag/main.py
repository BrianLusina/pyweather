import logging
from app.servers.mcp.rag.server import mcp


if __name__ == "__main__":
    logging.getLogger("rag-mcp-server").setLevel(logging.WARNING)
    # The server will run and listen for requests from the client over stdio
    mcp.run(transport="stdio")
