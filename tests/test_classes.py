import unittest

EXCERCISES = True

if EXCERCISES:
    from exercises.classes import MyCalculator
else:
    from answers.classes import MyCalculator

class ClassesExercises(unittest.TestCase):

    def test_stateless_ops(self):

        c = MyCalculator()
        self.assertEqual(c.total, 0)
        self.assertEqual(c.add(4, 5), 9)
        self.assertEqual(c.multiply(3.3722, 33), 111.2826)
        self.assertEqual(c.divide(10, 4), 2.5)
        self.assertEqual(c.subtract(11, 6), 5)
        self.assertEqual(c.subtract(11, 12), -1)

        c = MyCalculator(10)
        self.assertEqual(c.total, 10)
        self.assertEqual(c.add(4, 5), 9)
        self.assertEqual(c.multiply(3.3722, 33), 111.2826)
        self.assertEqual(c.divide(10, 4), 2.5)
        self.assertEqual(c.subtract(11, 6), 5)
        self.assertEqual(c.subtract(11, 12), -1)

    def test_stateful_ops(self):

        c = MyCalculator()

        c.add(3)
        self.assertEqual(c.get_current_total(), 3)

        c.subtract(2)
        self.assertEqual(c.get_current_total(), 1)

        c.multiply(10)
        self.assertEqual(c.get_current_total(), 10)

        c.divide(5)
        self.assertEqual(c.get_current_total(), 2)

        c.divide(2)
        self.assertEqual(c.get_current_total(), 1)

        self.assertEqual(c.get_past_totals(), [0, 3, 1, 10, 2, 1])


        c = MyCalculator(10)

        c.add(3)
        self.assertEqual(c.get_current_total(), 13)

        c.subtract(2)
        self.assertEqual(c.get_current_total(), 11)

        c.multiply(10)
        self.assertEqual(c.get_current_total(), 110)

        c.divide(5)
        self.assertEqual(c.get_current_total(), 22)

        c.divide(2)
        self.assertEqual(c.get_current_total(), 11)

        self.assertEqual(c.get_past_totals(), [10, 13, 11, 110, 22, 11])



