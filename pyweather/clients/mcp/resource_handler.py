import shlex


async def list_resources(session):
    """
    Fetches the list of available resources from the connected server
    and prints them in a user-friendly format.
    """
    try:
        resource_response = await session.list_resources()

        if not resource_response or not resource_response.resources:
            print("\nNo resources found on the server.")
            return

        print("\nAvailable Resources:")
        print("--------------------")
        for r in resource_response.resources:
            # The URI is the unique identifier for the resource
            print(f"  Resource URI: {r.uri}")
            # The description comes from the resource function's docstring
            if r.description:
                print(f"    Description: {r.description.strip()}")

        print("\nUsage: /resource <resource_uri>")
        print("--------------------")

    except Exception as e:
        print(f"Error fetching resources: {e}")


async def handle_resource(session, command: str) -> str | None:
    """
    Parses a user command to fetch a specific resource from the server
    and returns its content as a single string.
    """
    try:
        # The command format is "/resource <resource_uri>"
        parts = shlex.split(command.strip())
        if len(parts) != 2:
            print("\nUsage: /resource <resource_uri>")
            return None

        resource_uri = parts[1]

        print(f"\n--- Fetching resource '{resource_uri}'... ---")

        # Use the session's `read_resource` method with the provided URI
        response = await session.read_resource(resource_uri)

        if not response or not response.contents:
            print("Error: Resource not found or content is empty.")
            return None

        # Extract text from all TextContent objects and join them
        # This handles cases where a resource might be split into multiple parts
        text_parts = [
            content.text for content in response.contents if hasattr(content, "text")
        ]

        if not text_parts:
            print("Error: Resource content is not in a readable text format.")
            return None

        resource_content = "\n".join(text_parts)

        print("--- Resource loaded successfully. ---")
        return resource_content

    except Exception as e:
        print(f"\nAn error occurred while fetching the resource: {e}")
        return None
