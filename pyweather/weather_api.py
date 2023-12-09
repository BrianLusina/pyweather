"""
Contains the weather API logic
"""
from urllib import parse
from pyweather.utils import get_api_config


def build_weather_url(city: str, imperial: bool = False) -> str:
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
