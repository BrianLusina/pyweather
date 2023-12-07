"""
Contains draw utilities to draw the hangman
"""
_hanged_man = [
    r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
    r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
]


def draw_hanged_man(wrong_guesses: int) -> None:
    """
    Draws the hanged-man on the screen. Takes in the number of wrong guesses to obtain an index of the hanged man to
    draw.
    Args:
        wrong_guesses (int): number of wrong guesses

    Returns:
        None
    """
    print(_hanged_man[wrong_guesses])
