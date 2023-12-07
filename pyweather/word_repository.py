"""
Used for selecting words from a list of possible words. Could be from a file or an external source
"""
from random import choice
from pathlib import Path

WORDS_FILE = Path(__file__).parent / "words.txt"


def select_word(filename: Path = WORDS_FILE) -> str:
    """
    Selects a word at random from a given file

    Args:
          filename (Path): path to a pattern file to load
    Return:
        str: randomly selected word
    """
    with open(filename, mode="r", encoding="utf-8") as words:
        word_list = words.readlines()
    return choice(word_list).strip()
