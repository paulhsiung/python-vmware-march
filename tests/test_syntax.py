import unittest

EXERCISES = True

if EXERCISES:
    from excercises.syntax import clamp, char_range
else:
    from answers.syntax import clamp, char_range


class SyntaxExcercises(unittest.TestCase):
    def test_clamp(self):
        hi = 10
        lo = 0
        self.assertEqual(clamp(5, hi, lo), 5)
        self.assertEqual(clamp(11, hi, lo), hi)
        self.assertEqual(clamp(-2, hi, lo), lo)
        self.assertEqual(clamp(0, hi, lo), 0)

    def test_char_range(self):
        self.assertEqual(char_range("apple", 1, 3), "ppl")
        self.assertEqual(char_range("apple", 0, 0), "a")
        self.assertEqual(char_range("apple", 3, 3), "l")

