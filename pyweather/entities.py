"""
Contains structured models wrapping functionality around data obtained from Weather API
"""
import sys
from typing import Dict, Any
from dataclasses import dataclass

REVERSE = "\033[;7m"
RESET = "\033[0m"


@dataclass
class ApiConfig:
    """
    ApiConfig that contains information for setting up connection to Weather API
    Args:
        api_key (str): API Key used to authenticate with API
        base_url (str): Base URL of API
    """
    api_key: str
    base_url: str


@dataclass
class WeatherData:
    """
    WeatherData that contains information for weather data as obtained from the Weather API
    Args:
        city (str): Name of the city
        description (str): Description of weather information
        temperature (float): Temperature information
        use_imperial (bool): Whether to use imperial units or metric units. Defaults to False using metric units
    """
    city: str
    description: str
    temperature: float
    use_imperial: bool = False

    def display(self, padding: int = 20) -> str:
        return f"{REVERSE}{self.city:{padding}{RESET}} \t{self.description.capitalize():^{padding}} ({self.temperature}°{'F' if self.use_imperial else 'C'})"

    @staticmethod
    def from_json(data: Dict[str, Any]) -> 'WeatherData':
        """
        Factory method to create WeatherData instance from passed in dictionary data
        Args:
            data (dict):
        Returns:
            WeatherData: weather data
        """
        try:
            city = data["name"]
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]

            return WeatherData(
                city=city,
                description=weather_description,
                temperature=temperature
            )
        except Exception as e:
            sys.exit(f"Could not parse weather data. Error: {e}")
