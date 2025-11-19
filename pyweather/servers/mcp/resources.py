from pathlib import Path
from pyweather.servers.mcp.server import mcp_server


@mcp_server.resource("file://delivery_log")
def delivery_log_resource() -> list[str]:
    """
    Reads a delivery log file and returns its contents as a list of lines.
    Each line contains an order number and a delivery location.
    """
    try:
        log_file = Path("delivery_log.txt")
        if not log_file.exists():
            return ["Error: The delivery_log.txt file was not found on the server."]

        # Read the file, remove leading/trailing whitespace, and split into lines
        return log_file.read_text(encoding="utf-8").strip().splitlines()

    except Exception as e:
        return [f"An unexpected error occurred while reading the delivery log: {str(e)}"]
