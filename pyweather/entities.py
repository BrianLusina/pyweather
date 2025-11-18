"""
Contains structured models wrapping functionality around data obtained from Weather API
"""
import sys
from typing import Dict, Any
from dataclasses import dataclass


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
    feels_like: int
    humidity: int
    wind_speed: int
    use_imperial: bool = False
    weather_id: int = 0

    def __str__(self) -> str:
        return (
            f"ID: {self.weather_id}, City: {self.city}, description: {self.description} "
            f"({self.temperature}°{'F' if self.use_imperial else 'C'})"
        )

    def to_json(self) -> Dict[str, str]:
        return dict(
            location=self.city,
            description=self.description,
            temperature=self.temperature,
            use_imperial=self.use_imperial,
            weather_id=self.weather_id,
            feels_like_celsius=f"{self.feels_like}°C",
            humidity=f"{self.humidity}%",
            wind_speed_mps=f"{self.wind_speed} m/s",
        )

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "WeatherData":
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
            weather_id = data["weather"][0]["id"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return WeatherData(
                city=city,
                description=weather_description,
                temperature=temperature,
                weather_id=weather_id,
                feels_like=feels_like,
                humidity=humidity,
                wind_speed=wind_speed,
            )
        # pylint: disable=broad-exception-caught
        except Exception as e:
            sys.exit(f"Could not parse weather data. Error: {e}")
