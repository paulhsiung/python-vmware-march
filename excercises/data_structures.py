
def evens(n):
    """
    Return a list of all integers greater than 0 and up
    to (and including) `n` that are even.

    @param: n (positive, numeric)

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_evens
    """
    return [i+1 for i in range(1,n,2)]


def counter(elements):
    """
    Given a list of elements, return a dictionary where
    each key is an element, and the value is the integer number of times
    it appeared in the original list.

    @param: elements (list)

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_counter
    """
    ret = {}
    print elements
    for key in set(elements):
        ret[key] = elements.count(key)
    return ret


def csv_line(elements, sep):
    """
    Given a list of elements make a string that is each object's
    string representation, separated by the `sep` string.

        >>> print csv_line([0, None, 'apple'], ",")
        0,None,apple

    HINT: You may need to convert elements to strings.

    BONUS POINTS: Do this in a single line! Look up the `join()` function.

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_csv_line
    """
    print sep
    print elements
    return sep.join([str(e) for e in elements])


def similar(first, second):
    """
    Return a list of elements that are in BOTH first and second lists

    @param: first (list)
    @param: second (list)

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_similar
    """
    return list(set(first).intersection(set(second)))


def filter_and_rank_teams(teams, min_score, restricted_teams, top_n):
    """
    Given a list of (int score, team name) tuples, and an integer min_score,
    return a list consisting of only tuples where first score value is
    greater than or equal to min_score AND if that team name is NOT in
    the restricted_teams list.

    The final list must be sorted by score of the tuple, descending.

    Only return the top_n teams by score.

    @param: teams (list of tuples)
    @param: min_score (int)
    @param: restricted_teams (list of strings)

    HINT: List comprehensions, sorting, and slicing will be useful here!

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_filter_and_rank_teams
    """
    teams = [(s,n) for (s,n) in teams
                        if s >= min_score and n not in restricted_teams ]

    teams.sort(key=lambda tup: tup[0], reverse=True)
    return teams[:top_n]



