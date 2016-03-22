import unittest

EXCERCISES = True

if EXCERCISES:
    from exercises.functions import power_list_factory, dict_updater_factory
else:
    from answers.functions import power_list_factory, dict_updater_factory

class FunctionExercises(unittest.TestCase):
    def test_power_list_factory(self):
        func = power_list_factory()
        p = 2
        self.assertEqual(func(p, 0, 1, 2, 3, 4), sum([x**2 for x in range(5)]))
        self.assertEqual(func(10, 0), 0)

    def test_dict_updater_factory(self):
        d1, d2 = {'a' : 1, 'b' : 2}, {'b' : 10, 'c' : 3}
        func = dict_updater_factory()
        self.assertEqual(func(d1, d2), {'a' : 1, 'b' : 10, 'c' : 3})
