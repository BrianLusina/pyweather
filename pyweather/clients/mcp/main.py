import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pyweather.clients.mcp.weather_agent import create_graph
from pyweather.clients.mcp.prompts_handler import list_prompts, handle_prompt
from pyweather.clients.mcp.resource_handler import list_resources, handle_resource


# MCP server launch config
server_params = StdioServerParameters(
    command="python",
    args=["../servers/mcp/server.py"]
)

# Entry point
async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            agent = await create_graph(session)

            print("Weather MCP agent is ready.")
            # Add instructions for the new prompt commands
            print("Type a question, or use one of the following commands:")
            print("  /prompts                           - to list available prompts")
            print("  /prompt <prompt_name> \"args\"...  - to run a specific prompt")
            print("  /resources                       - to list available resources")
            print("  /resource <resource_uri>         - to load a resource for the agent")

            while True:
                # This variable will hold the final message to be sent to the agent
                message_to_agent = ""

                user_input = input("\nYou: ").strip()
                if user_input.lower() in {"exit", "quit", "q"}:
                    break

                # --- Command Handling Logic ---

                if user_input.lower() == "/resources":
                    await list_resources(session)
                    continue  # Command is done, loop back for next input
                elif user_input.lower() == "/resource":
                    resource_content = await handle_resource(session, user_input)
                    if resource_content:
                        # Ask the user what action to take on the loaded content
                        action_prompt = input(
                            "Resource loaded. What should I do with this content? (Press Enter to just save to context)\n> ").strip()
                        if action_prompt:
                            message_to_agent = f"""
                            CONTEXT from a loaded resource:
                            ---
                            {resource_content}
                            ---
                            TASK: {action_prompt}
                            """
                        # If user provides no action, create a default message to save the context
                        else:
                            print("No action specified. Adding resource content to conversation memory...")
                            message_to_agent = f"""
                            Please remember the following context for our conversation. Just acknowledge that you have received it.
                            ---
                            CONTEXT:
                            {resource_content}
                            ---
                            """
                    else:
                        # If resource loading failed, loop back for next input
                        continue
                elif user_input.lower() == "/prompts":
                    await list_prompts(session)
                    continue  # Command is done, loop back for next input
                elif user_input.startswith("/prompt"):
                    # The handle_prompt function now returns the prompt text or None
                    prompt_text = await handle_prompt(session, user_input)
                    if prompt_text:
                        message_to_agent = prompt_text
                    else:
                        # If prompt fetching failed, loop back for next input
                        continue
                else:
                    # For a normal chat message, the message is just the user's input
                    message_to_agent = user_input

                # Final agent invocation
                # All paths (regular chat or successful prompt) now lead to this single block
                if message_to_agent:
                    try:
                        # LangGraph expects a list of messages
                        response = await agent.ainvoke(
                            {"messages": [("user", message_to_agent)]},
                            config={"configurable": {"thread_id": "weather-session"}}
                        )
                        print("AI:", response["messages"][-1].content)
                    except Exception as e:
                        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())