import unittest
from unittest.mock import *

from src.zad03.checker import Checker


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_remainder_before_17(self):
        self.checker.env.getTime = Mock(name='getTime')
        self.checker.env.getTime.return_value = 16
        self.checker.env.resetWav = Mock(name='resetWav')
        self.checker.env.resetWav.return_value = False

        self.assertFalse(self.checker.remainder("song.wav"))

    def test_remainder_after_17(self):
        self.checker.env.getTime = Mock(name='getTime')
        self.checker.env.getTime.return_value = 18
        self.checker.env.wavWasPlayed = Mock(name='wavWasPlayed')
        self.checker.env.wavWasPlayed.return_value = True

        self.assertTrue(self.checker.remainder("song.wav"))

    def tearDown(self):
        self.checker = None


if __name__ == '__main__':
    unittest.main()
