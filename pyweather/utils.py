"""
Utility functions
"""
from typing import Dict
from dataclasses import dataclass
from pathlib import Path
from configparser import ConfigParser

_SECRETS_FILE = Path(__file__).parent / "secrets.ini"


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


def get_api_config(secrets_file: Path = _SECRETS_FILE) -> ApiConfig:
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

    return ApiConfig(
        base_url=base_url,
        api_key=api_key
    )
