from typing import Dict, List
import shlex
from langchain_mcp_adapters.client import MultiServerMCPClient


async def list_resources(
    client: MultiServerMCPClient, server_configs: Dict[str, Dict[str, str | List[str]]]
):
    """
    Fetches the list of available resources from the connected server
    and prints them in a user-friendly format.
    """
    print("\nAvailable Resources from all servers:")
    print("--------------------")
    any_resources_found = False

    for server_name in server_configs.keys():
        try:
            async with client.session(server_name) as session:
                resource_response = await session.list_resources()

                if resource_response and resource_response.resources:
                    any_resources_found = True
                    print(f"\n-- Server: {server_name} --")
                    for r in resource_response.resources:
                        # The URI is the unique identifier for the resource
                        print(f"  Resource URI: {r.uri}")
                        # The description comes from the resource function's docstring
                        if r.description:
                            print(f"    Description: {r.description.strip()}")

        except Exception as e:
            print(f"Error fetching resources from server {server_name} : {e}")

    print(f"\nUse: /resource <server_name> <resource_uri>")
    print("------------")

    if not any_resources_found:
        print("\nNo resources found on any connected servers.")


async def handle_resource(client: MultiServerMCPClient, command: str) -> str | None:
    """
    Parses a user command to fetch a specific resource from the server
    and returns its content as a single string.
    """
    try:
        # The command format is "/resource <resource_uri>"
        parts = shlex.split(command.strip())

        if len(parts) != 3:
            print("\nUsage: /resource <server_name> <resource_uri>")
            return None

        server_name = parts[1]
        resource_uri = parts[2]
        print(
            f"\n--- Fetching resource '{resource_uri}' from server '{server_name}'... ---"
        )

        # Use the session's `read_resource` method with the provided URI
        blobs = await client.get_resources(server_name=server_name, uris=[resource_uri])

        if not blobs:
            print("Error: Resource not found or content is empty.")
            return None

        # converting LangChain blobs into string content
        resource_content = blobs[0].as_string()

        print("--- Resource loaded successfully. ---")
        return resource_content

    except Exception as e:
        print(f"\nAn error occurred while fetching the resource: {e}")
        return None
