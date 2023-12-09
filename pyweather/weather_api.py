"""
Contains the weather API logic
"""
from typing import Dict, Any
from urllib import parse, request, error
import json
import sys
from pyweather.utils import get_api_config


def _build_weather_url(city: str, imperial: bool = False) -> str:
    """
    Build the URL for an API request to OpenWeather API
    Args:
        city (str): City name to query weather information for
        imperial (bool): Whether to use imperial units or not, defaulted to False

    Returns:
        str: Built API weather URL
    """
    api_config = get_api_config()

    city_name = " ".join(city)
    url_encoded_city = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = f"{api_config.base_url}?q={url_encoded_city}&units={units}&appid={api_config.api_key}"
    return url


def get_weather_data(city: str, imperial: bool = False) -> Dict[str, Any]:
    """Makes an API request to a URL and returns the data as a Python object.

    Args:
        city (str): City name to query weather information for
        imperial (bool): Whether to use imperial units or not, defaulted to False

    Returns:
        dict: Weather information for a specific city
    """
    try:
        query_url = _build_weather_url(city, imperial)
        response = request.urlopen(query_url)
    except error.HTTPError as e:
        if e.code == 401:
            sys.exit(f"Access denied. Check that your API Key is correct")
        if e.code == 404:
            sys.exit(f"Can't find the weather data for city {city}. It does not seem to exist...")
        else:
            sys.exit(f"Something terrible has happened. Error: {e}")

    data = response.read()

    try:
        return json.loads(data)
    except json.JSONDecodeError as jde:
        sys.exit(f"Could not read server response. Error: {jde}")
