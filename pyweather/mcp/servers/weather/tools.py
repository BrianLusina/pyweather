from typing import Dict
from pyweather.mcp.servers.weather.server import mcp
from pyweather.api import get_weather_data


@mcp.tool()
def get_weather(location: str) -> Dict[str, str]:
    """
    Fetches the current weather for a specified location using the OpenWeatherMap API.
    Args:
        location: The city name and optional country code (e.g., "London,uk").

    Returns:
        A dictionary containing weather information or an error message.
    """
    try:
        weather = get_weather_data(city=location)
        return weather.to_json()
    except Exception as e:
        return {"error": str(e)}
