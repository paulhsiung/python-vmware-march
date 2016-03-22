import unittest


EXCERCISES = True

if EXCERCISES:
    from excercises.data_structures import evens, counter, csv_line, \
                                similar, filter_and_rank_teams
else:
    from answers.data_structures import evens, counter, csv_line, \
                                similar, filter_and_rank_teams


class DataStructureExcercises(unittest.TestCase):
    def test_evens(self):
        self.assertEqual(evens(10), [2, 4, 6, 8, 10])
        self.assertEqual(evens(11), [2, 4, 6, 8, 10])
        self.assertEqual(evens(-1), [])
        self.assertEqual(evens(0), [])
        self.assertEqual(evens(1), [])
        self.assertEqual(evens(2), [2])

    def test_counter(self):
        elements = ['a', 'b', 'a', 'c', 's', 's', 's']
        self.assertEqual(counter(elements), {
            'a' : 2, 'b' : 1, 's' : 3, 'c' : 1})
        self.assertEqual(counter([]), {})
        self.assertEqual(counter([None]), {None : 1})

    def test_csv_line(self):
        self.assertEqual(csv_line([0, None, 'apple'], ","), "0,None,apple")
        self.assertEqual(csv_line([], ","), "")
        self.assertEqual(csv_line(["Red", "Blue"], "||"), "Red||Blue")

    def test_similar(self):
        self.assertEqual(similar(['a', 'b'], ['b']), ['b'])
        self.assertEqual(similar([], []), [])
        self.assertEqual(similar(['b'], []), [])
        self.assertEqual(similar(['b', 'b', 'b', 'e'], ['b', 'd', 'z']), ['b'])

    def test_filter_and_rank_teams(self):
        items = [
            (8, "Seahawks"), 
            (11, "49ers"), 
            (12, "Green Bay"),
            (9, "Packers"), 
            (13, "Patriots"),
            (12, "Jets"),
        ]
        right_items = [ 
            (13, "Patriots"),
            (12, "Jets"), 
            (11, "49ers"),
        ]
        self.assertEqual(filter_and_rank_teams(items, 11, ["Green Bay"], 3), right_items)




