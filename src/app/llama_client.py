import os
import sys

# Ensure the project `src` directory is on sys.path so `from app...` imports
# work when running this file directly (for example: `python src/app/main.py`).
# This is a minimal, local fix to make the package importable without requiring
# the user to set PYTHONPATH or install the package.
_SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

import asyncio
from dotenv import load_dotenv
from app.clients.mcp.llama import llama_client

load_dotenv()

if __name__ == "__main__":
    # Ensure you have a running asyncio event loop
    try:
        asyncio.run(llama_client())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
