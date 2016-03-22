"""
INSTRUCTIONS:

Complete these excercises one by one.
Check each as you go with the provided "Test with" statement.

Happy coding!
"""


def clamp(value, hi, lo):
    if value < lo:
        return lo
    elif value > hi:
        return hi
    """
    We want to make sure our value is in the range [lo, hi]

    If value is less than, lo, return lo.
    If value is greater than hi, return hi,
    otherwise return value:

    @param: value (numeric)
    @param: hi (numeric)
    @param: lo (numeric)
    @returns: numeric

    Test with:
    $ py.test tests/test_syntax.py::SyntaxExcercises::test_clamp
    """
    return value


def char_range(string, a, b):
    """
    Return a substring of the original going from character
    at index a to character at index b (inclusive!).

    @param: string (str)
    @param: a (positive int)
    @param: b (positive int, greater than or equal to a)
    """
    return string[a:b+1]
