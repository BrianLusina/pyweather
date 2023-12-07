import unittest
from hangman.utils import join_guessed_letters, build_guessed_word


class UtilsTestCase(unittest.TestCase):
    def test_join_guessed_letters(self):
        letters = {"a", "b", "c", "d"}
        expected = 'a b c d'
        actual = join_guessed_letters(letters)
        self.assertEqual(expected, actual)

    def test_build_guessed_word(self):
        guessed_letters = {"a", "b", "c", "d", "p", "o"}
        target_word = "airport"
        expected = 'a _ _ p o _ _'
        actual = build_guessed_word(target_word, guessed_letters)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
