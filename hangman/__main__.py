"""
Entry point of the game
"""
from typing import Set
from hangman.word_repository import select_word
from hangman.utils import build_guessed_word, join_guessed_letters
from hangman.game import game_over, MAX_INCORRECT_GUESSES
from hangman.draw import draw_hanged_man
from hangman.player_input import get_player_input


def main() -> None:
    """Entry point of the game. Gets the command line arguments and shows either all patterns of the game or a single
    pattern based on the user input from the command line"""
    target_word = select_word()
    guessed_letters: Set[str] = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman")

    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            f"Current guessed letters: word is: {join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats, You did it!")
    print(f"Your word was {target_word}")


if __name__ == "__main__":
    main()
