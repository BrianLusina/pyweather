import unittest
from hangman.game import game_over


class GameTestCase(unittest.TestCase):
    def test_returns_true_for_incorrect_guesses(self):
        """should return True if the wrong guesses equals the maximum allowed wrong guesses"""
        wrong_guesses = 6
        actual = game_over(wrong_guesses, "airplane", {"a"})
        self.assertTrue(actual)

    def test_returns_true_if_target_word_is_in_guessed_letters(self):
        """should return True if the letters in the target word are in the guessed letters"""
        wrong_guesses = 3
        target_word = "airplane"
        guessed_letters = {"a", "i", "r", "p", "l", "n", "e"}
        actual = game_over(wrong_guesses, target_word, guessed_letters)
        self.assertTrue(actual)

    def test_returns_true_if_wrong_guesses_is_more_than_allowed_maximum(self):
        """should return True if the number of wrong guesses is more than allowed maximum"""
        wrong_guesses = 7
        target_word = "airplane"
        guessed_letters = {"a", "i", "r", "p", "l", "n"}
        actual = game_over(wrong_guesses, target_word, guessed_letters)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
