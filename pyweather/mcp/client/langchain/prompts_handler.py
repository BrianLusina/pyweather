from typing import Dict
import shlex
from langchain_mcp_adapters.client import MultiServerMCPClient


async def list_prompts(client: MultiServerMCPClient, server_configs: Dict[str, Dict]):
    """
    Fetches the list of available prompts from the configured servers
    and prints them in a user-friendly format.
    """
    print("\nAvailable Prompts")
    print("-" * 30)

    any_prompts_found = False

    # iterate through the names of the servers defined in the server_configs
    for server_name in server_configs.keys():
        try:
            # We temporarily open a communication session with a specific server (e.g., just the “weather” server),
            # which gives us a session object to interact with it directly.
            async with client.session(server_name) as session:
                prompt_response = await session.list_prompts()

                if not prompt_response and prompt_response.prompts:
                    any_prompts_found = True
                    print(f"\nServer: {server_name} ---")
                    for p in prompt_response.prompts:
                        print(f"    Prompt: {p.name}")
                        if p.arguments:
                            arg_list = [f"<{arg.name}>" for arg in p.arguments]
                            print(f"  Arguments: {' '.join(arg_list)}")
                        else:
                            print("  Arguments: None")

        except Exception as e:
            print(f"Could not fetch prompts from server {server_name}: {e}")

    print("\nUse: /prompt <server_name> <prompt_name> \"arg1\" \"arg2\" ...")
    print("-----------------------------------")
    if not any_prompts_found:
        print("\nNo prompts were found on any connected servers.")


async def handle_prompt(client: MultiServerMCPClient, command: str) -> str | None:
    """
    Parses a user command to invoke a specific prompt from a given server,
    then returns the generated prompt text.
    """
    try:
        parts = shlex.split(command.strip())
        if len(parts) < 2:
            print("\nUsage: /prompt <server_name> <prompt_name> \"arg1\" \"arg2\" ...")
            return None

        server_name = parts[1]
        prompt_name = parts[2]
        user_args = parts[3:]

        prompt_def = None
        async with client.session(server_name) as session:
            # Get available prompts from the server to validate against
            prompt_def_response = await session.list_prompts()
            if not prompt_def_response or not prompt_def_response.prompts:
                print("\nError: Could not retrieve any prompts from the server.")
                return None

            # Find the specific prompt definition the user is asking for
            prompt_def = next((p for p in prompt_def_response.prompts if p.name == prompt_name), None)

        if not prompt_def:
            print(f"\nError: Prompt '{prompt_name}' not found on the server.")
            return None

        # Check if the number of user-provided arguments matches what the prompt expects
        if len(user_args) != len(prompt_def.arguments):
            expected_args = [arg.name for arg in prompt_def.arguments]
            print(f"\nError: Invalid number of arguments for prompt '{prompt_name}'.")
            print(f"Expected {len(expected_args)} arguments: {', '.join(expected_args)}")
            return None

        # Build the argument dictionary
        arg_dict = {arg.name: val for arg, val in zip(prompt_def.arguments, user_args)}

        # Fetch the prompt from the server using the validated name and arguments
        prompt_messages = await client.get_prompt(server_name=server_name, prompt_name=prompt_name, arguments=arg_dict)

        # Extract the text content from the response
        prompt_text = prompt_messages[0].content

        print("\n--- Prompt loaded successfully. Preparing to execute... ---")
        # Return the fetched text to be used by the agent
        return prompt_text

    except Exception as e:
        print(f"\nAn error occurred during prompt invocation: {e}")
        return None
