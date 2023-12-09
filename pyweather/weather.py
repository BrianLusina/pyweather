"""
Contains the weather API logic
"""
from configparser import ConfigParser


def _get_api_key(wrong_guesses: int, target_word: str, guessed_letters: Set[str]) -> bool:
    """
    Checks if the game is over based on the number of wrong guesses, target word and the guessed letters. It returns
    True if the number of wrong guesses is equal to the maximum allowed incorrect guesses, which is defaulted to 6.
    Also, it returns true if the set of the target word is a member of every letter in the guessed letters
    Args:
        wrong_guesses (int): number of incorrect guesses
        target_word (str): the target word
        guessed_letters (set): set of alredy guessed letters by the player.

    Returns:
        bool: True indicating the game is over, false indicating that the game is still ongoing
    """
    if wrong_guesses >= MAX_INCORRECT_GUESSES:
        return True

    # checks if every item on the left-hand side set is a member of the right-hand side set. In other words, are the
    # letters in the target word in the guessed letters set from the player?
    if set(target_word) <= guessed_letters:
        return True

    return False
