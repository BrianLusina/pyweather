"""
Contains structured models wrapping functionality around configuration for the application
"""
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