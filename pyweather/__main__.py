"""
Entry point of the game
"""
from typing import Set
from pyweather.cli import get_command_line_args


def main() -> None:
    """Entry point of the weather application. Gets the command line arguments"""
    args = get_command_line_args()


if __name__ == "__main__":
    main()
