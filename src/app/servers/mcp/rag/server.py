import logging
from mcp.server.fastmcp import FastMCP


# Initialize the FastMCP server with a descriptive name
mcp = FastMCP("RAGAssistant")

if __name__ == "__main__":
    logging.getLogger("rag-mcp-server").setLevel(logging.WARNING)
    mcp.run(transport="stdio")
