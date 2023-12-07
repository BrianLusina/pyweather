"""
Utility functions
"""
from pathlib import Path
from configparser import ConfigParser

_SECRETS_FILE = Path(__file__).parent / "secrets.ini"


def get_api_key(secrets_file: Path = _SECRETS_FILE) -> str:
    """
    Retrieves the API key from the secret file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    Args:
        secrets_file (Path): path to a secret file.
    Returns:
        str: API Key
    """
    config = ConfigParser()
    config.read(secrets_file)
    return config["openweather"]["api_key"]
