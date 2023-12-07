import unittest
from hangman.word_repository import select_word


class WordRepositoryTestCase(unittest.TestCase):
    def test_load_words(self):
        """should load the words from the default words.txt file"""

        actual_random_word = select_word()
        self.assertIsNotNone(actual_random_word)


if __name__ == "__main__":
    unittest.main()
