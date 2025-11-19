import shlex


async def list_prompts(session):
    """
    Fetches the list of available prompts from the connected server
    and prints them in a user-friendly format.
    """
    try:
        prompt_response = await session.list_prompts()

        if not prompt_response or not prompt_response.prompts:
            print("\nNo prompts were found on the server.")
            return

        print("\nAvailable Prompts and Their Arguments:")
        print("---------------------------------------")
        for p in prompt_response.prompts:
            print(f"Prompt: {p.name}")
            if p.arguments:
                arg_list = [f"<{arg.name}>" for arg in p.arguments]
                print(f"  Arguments: {' '.join(arg_list)}")
            else:
                print("  Arguments: None")

        print("\nUsage: /prompt <prompt_name> \"arg1\" \"arg2\" ...")
        print("---------------------------------------")

    except Exception as e:
        print(f"Error fetching prompts: {e}")


async def handle_prompt(session, command: str) -> str | None:
    """
    Parses a user command to invoke a specific prompt from the server,
    then returns the generated prompt text.
    """
    try:
        parts = shlex.split(command.strip())
        if len(parts) < 2:
            print("\nUsage: /prompt <prompt_name> \"arg1\" \"arg2\" ...")
            return None

        prompt_name = parts[1]
        user_args = parts[2:]

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
        prompt_response = await session.get_prompt(prompt_name, arg_dict)

        # Extract the text content from the response
        prompt_text = prompt_response.messages[0].content.text

        print("\n--- Prompt loaded successfully. Preparing to execute... ---")
        # Return the fetched text to be used by the agent
        return prompt_text

    except Exception as e:
        print(f"\nAn error occurred during prompt invocation: {e}")
        return None