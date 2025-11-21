from typing import List
from pathlib import Path
from pyweather.mcp.servers.tasks.server import mcp


@mcp.resource("file://meeting_notes")
def meeting_notes_resource() -> List[str]:
    """
    Reads a meeting notes file and returns its contents as a list of lines.
    The notes contain discussion points and action items for an Ed Tech company.
    """
    try:
        notes_file = Path("meeting_notes.txt")
        if not notes_file.exists():
            return ["Error: The meeting_notes.txt file was not found on the server."]

        # Read the file, remove leading/trailing whitespace, and split into lines
        return notes_file.read_text(encoding="utf-8").strip().splitlines()

    except Exception as e:
        return [f"An unexpected error occurred while reading the meeting notes: {str(e)}"]
