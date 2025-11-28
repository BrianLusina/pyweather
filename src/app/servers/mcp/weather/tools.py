from typing import Dict
from mcp.server.fastmcp import Context
from app.servers.mcp.weather.server import mcp
from app.api import get_weather_data


@mcp.tool()
async def get_weather(location: str, ctx: Context) -> Dict[str, str]:
    """
    Fetches the current weather for a specified location using the OpenWeatherMap API.
    Args:
        location: The city name and optional country code (e.g., "London,uk").

    Returns:
        A dictionary containing weather information or an error message.
    """
    await ctx.info(f"Received request to fetch weather for '{location}'.")
    try:
        await ctx.debug(f"Fetching weather data for '{location}'.")
        weather = get_weather_data(city=location)
        await ctx.debug(f"Successfully fetched weather data for '{location}'.")
        return weather.to_json()
    except Exception as e:
        await ctx.error(f"Failed to fetch weather for '{location}': {str(e)}")
        return {"error": str(e)}
