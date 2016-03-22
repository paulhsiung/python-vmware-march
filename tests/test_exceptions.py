import unittest

EXCERCISES = True

if EXCERCISES:
    from exercises.exceptions import add_and_divide, throw_my_exception, ArgIsNoneException
else:
    from answers.exceptions import add_and_divide, throw_my_exception, ArgIsNoneException

class ExceptionExercises(unittest.TestCase):
    def test_add_and_divide(self):
        self.assertEqual(add_and_divide(10, 3), (10 + 3) / 3)
        self.assertEqual(add_and_divide(10, 0), 10)
        self.assertEqual(add_and_divide(None, 3), None)
        self.assertEqual(add_and_divide(None, []), None)

    def test_throw_my_exception(self):
        self.assertRaises(ArgIsNoneException, throw_my_exception, 1, 1, 1, 2, None, 3)
