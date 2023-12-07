import unittest
from string import ascii_uppercase
from hangman.player_input import validate_input


class PlayerInputTestCase(unittest.TestCase):
    def test_validate_input(self):
        """should return false if the player input is more than 1 character long"""
        actual = validate_input("ab", set())
        self.assertFalse(actual)

    def test_validate_upper_cased_input(self):
        """should return false if the player input is not a lower cased letter"""
        for letter in ascii_uppercase:
            actual = validate_input(letter, set())
            self.assertFalse(actual)

    def test_validate_already_guessed_input(self):
        """should return false if the player input is an already guessed letter"""
        guessed_letters = {"a", "b", "c"}
        letter = "a"
        actual = validate_input(letter, guessed_letters)
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
