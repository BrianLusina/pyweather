"""
Utility functions
"""
from typing import Set


def join_guessed_letters(guessed_letters: Set[str]) -> str:
    """
    Joins the guessed letters and returns a string
    Args:
        guessed_letters (set): guessed letters
    Returns:
        str: joined letters as a string separated by a space delimiter
    """
    return " ".join(sorted(guessed_letters))


def build_guessed_word(target_word: str, guessed_letters: Set[str]) -> str:
    """
    Build the word to show the player. This takes in the target word and a set of guessed letters. If any of the letters
    in the target word exist in the guessed letters, the are added to the output. If not, an underscore is added in its
    place.
    Args:
        target_word (str): Target word to build from guessed letters
        guessed_letters (set): set of guessed letters

    Returns:
        str: returns the guessed word

    """
    current_letters = []

    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")

    return " ".join(current_letters)
