"""
Gets player input and validates it
"""
from typing import Set

import string


def get_player_input(guessed_letters: Set[str]) -> str:
    """
    Retrieves the player's input from an input prompt and loops until the data provided is valid
    Args:
        guessed_letters (List): list of already guessed letters from the player

    Returns:
        str: The player's input that has been lower-cased and validated
    """
    while True:
        player_input = input("Guess a letter: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input


def validate_input(player_input: str, guessed_letters: Set[str]) -> bool:
    """
    Validates a player's input against already guessed letters
    Args:
        player_input (str): the player's input
        guessed_letters (list): list of guessed letters from the player

    Returns:
        bool: True if the player input is valid, false otherwise
    """
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )
