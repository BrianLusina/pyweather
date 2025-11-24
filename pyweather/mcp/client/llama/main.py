import asyncio
from typing import List

# LlamaIndex imports for the agent, LLM, and MCP tools
# This is a powerful, general-purpose agent class provided by LlamaIndex. It follows a “Reason and Act” loop, where it
# uses an LLM to reason about a problem, choose an appropriate tool, act by executing it, and then observe the result
# to continue the process.
from llama_index.core.agent.workflow import ReActAgent
# This class is the specific connector that allows our LlamaIndex agent to use a Google generative AI model
# (like Gemini) as its underlying “brain” or reasoning engine.
from llama_index.llms.google_genai import GoogleGenAI
# These are the essential adapter classes from the llama-index-tools-mcp library. BasicMCPClient manages the low-level
# connection to our server, while McpToolSpec acts as a high-level wrapper that makes the server’s tools discoverable
# and usable within the LlamaIndex framework.
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

async def main():
    """
    Main function to set up and run the LlamaIndex agent.
    """
    print("Initializing LlamaIndex agent...")

    # 1. Set up the LLM
    # Using a placeholder for the API key
    # Replace "YOUR_GOOGLE_AI_API_KEY" with your actual key
    llm = GoogleGenAI(
        model_name="gemini-1.5-flash",
        api_key="{{GOOGLE_GEMINI_API_KEY}}"
    )
    # 2. Set up the MCP client and tools
    # We pass the stdio configuration dictionary directly to the client
    mcp_client = BasicMCPClient("python", args=["mcp/servers/weather/server.py"])

    # McpToolSpec is a LlamaIndex-native way to wrap MCP tools
    tool_spec = McpToolSpec(client=mcp_client)

    # The agent will use the tools loaded from the MCP server
    # We use the async method to fetch the tool definitions
    mcp_tools: List = await tool_spec.to_tool_list_async()
    print(f"Successfully loaded {len(mcp_tools)} tool(s) from the MCP server.")

    # 3. Create the LlamaIndex Agent
    # We use a ReActAgent, a standard and powerful agent type in LlamaIndex
    # It will use the Gemini LLM to reason about when to use the loaded MCP tools
    agent = ReActAgent(tools=mcp_tools, llm=llm, verbose=False)

    print("\nWeather MCP agent is ready. Ask for the weather (e.g., 'What is the weather in London?').")

    # 4. Start the conversation loop
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting.")
            break

        if not user_input:
            continue

        try:
            # The agent's chat method handles the full reasoning and tool-calling loop
            response = await agent.run(user_input)
            print("AI:", str(response))
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure you have a running asyncio event loop
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
