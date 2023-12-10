"""
Utility functions
"""
from typing import Tuple
from pathlib import Path
from configparser import ConfigParser
from pyweather.entities import ApiConfig, WeatherData
from pyweather.style import change_color, RESET, WHITE, BLUE, RED, CYAN, YELLOW, REVERSE

_SECRETS_FILE = Path(__file__).parent / "secrets.ini"
_THUNDERSTORM = range(200, 300)
_DRIZZLE = range(300, 400)
_RAIN = range(500, 600)
_SNOW = range(600, 700)
_ATMOSPHERE = range(700, 800)
_CLEAR = range(800, 801)
_CLOUDY = range(801, 900)


def get_api_config(secrets_file: str = "secrets.ini") -> ApiConfig:
    """
    Retrieves the API config such as API key and base url from the secret file and returns a dictionary

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        base_url=http://api.openweathermap.org/data/2.5/weather
        api_key=<YOUR-OPENWEATHER-API-KEY>
    Args:
        secrets_file (Path): path to a secret file.
    Returns:
        ApiConfig: API config
    """
    config = ConfigParser()
    config.read(secrets_file)
    api_key = config["openweather"]["api_key"]
    base_url = config["openweather"]["base_url"]

    return ApiConfig(base_url=base_url, api_key=api_key)


def _select_weather_display_params(weather_id: int) -> Tuple[str, str]:
    """Selects a weather symbol and a display color for a weather state.

    Args:
        weather_id (int): Weather condition code from the OpenWeather API

    Returns:
        tuple[str]: Contains a weather symbol and a display color
    """
    if weather_id in _THUNDERSTORM:
        display_params = ("💥", RED)
    elif weather_id in _DRIZZLE:
        display_params = ("💧", CYAN)
    elif weather_id in _RAIN:
        display_params = ("💦", BLUE)
    elif weather_id in _SNOW:
        display_params = ("⛄️", WHITE)
    elif weather_id in _ATMOSPHERE:
        display_params = ("🌀", BLUE)
    elif weather_id in _CLEAR:
        display_params = ("🔆", YELLOW)
    elif weather_id in _CLOUDY:
        display_params = ("💨", WHITE)
    else:  # In case the API adds new weather codes
        display_params = ("🌈", RESET)
    return display_params


def display_weather_info(weather_data: WeatherData, padding: int = 20) -> None:
    """Selects a weather symbol and a display color for a weather state.

    Args:
        weather_data (WeatherData): Weather data
        padding (int): padding
    """
    city = weather_data.city
    weather_id = weather_data.weather_id
    weather_description = weather_data.description
    temperature = weather_data.temperature
    imperial = weather_data.use_imperial

    change_color(REVERSE)
    print(f"{city:^{padding}}", end="")
    change_color(RESET)

    weather_symbol, color = _select_weather_display_params(weather_id)
    change_color(color)

    print(f"\t{weather_symbol}", end=" ")
    print(
        f"\t{weather_description.capitalize():^{padding}}",
        end=" ",
    )
    change_color(RESET)

    print(f"({temperature}°{'F' if imperial else 'C'})")
