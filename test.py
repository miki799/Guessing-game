import unittest
import main


class TestMain(unittest.TestCase):
    def test_input(self):  # if correct input
        result = main.guess_game(5, 5)
        self.assertTrue(result)

    def test_incorrect_input(self):  # string
        result = main.guess_game('sds', 5)
        self.assertFalse(result)

    def test_wrong_guess(self):  # bad guess
        result = main.guess_game(1, 5)
        self.assertFalse(result)

    def test_out_of_range(self):  # too far guess
        result = main.guess_game(100, 2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
