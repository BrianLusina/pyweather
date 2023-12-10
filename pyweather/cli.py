"""
Defines the CLI command arguments
"""
import argparse
from argparse import Namespace


def get_command_line_args() -> Namespace:
    """
    Creates a parser and adds arguments for the parser returning the namespace for the argument parser to use in a CLI
    Returns:
        Namespace: populated namespace object
    """
    parser = argparse.ArgumentParser(
        prog="pyweather",
        description="Gets weather and temperature information for a city",
    )

    # Argument to get the city name, allows users to pass in city names made up of more than 1 word, e.g. New York
    parser.add_argument(
        "-c",
        "--city",
        nargs="+",
        type=str,
        help="Enter the city name",
    )

    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display daily temperatures in imperial units",
    )

    return parser.parse_args()
