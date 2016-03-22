import re

def string_formatting(amount, value, item):
    """
    Return a string with the following formatting:

        '<floating to 5 decimal places> grams of <string> cost $<floating money format>'

    Ensure you round to the nearest correct decimal place!

    @param: amount (floating)
    @param: value (floating)
    @param: item (string)
    @returns: string

    Test with:
    $ py.test tests/test_strings.py::StringExercises::test_string_formatting
    """
    return None


def extract_words(sentence):
    """
    Return a list of words from a sentence.

    Words are:
        1) Separated by spaces
        2) Do not include periods
        3) Do not include spaces, tabs, or newlines
        4) Always all lowercase

    Test with:
    $ py.test tests/test_strings.py::StringExercises::test_extract_words
    """
    return None


def only_alphanumeric(string):
    """
    Given a string, return the string, but with ONLY alpha numeric characters
    remaining. Order should otherwise stay the same.

    You may assume only ASCII characters :)

    HINT: Use the function .isalnum() to test whether a string or substring is
        alphanumeric.

    Test with:
    $ py.test tests/test_strings.py::StringExercises::test_only_alphanumeric
    """
    return None


def drumpf(string):
    """
    Replace all instance of "Trump" with "Drumpf", and return the new sentence.

    Test with:
    $ py.test tests/test_strings.py::StringExercises::test_drumpf
    """
    return None


def extract_usa_phone_numbers(text):
    """
    Given a string of text, extract every phone number.

    Example:

                rest
                  |
                  v
        "402-332-2393"
           ^
           |
        area_code (optional)

    The leading one is optional, as are the dashes. The parenthesis are
    optional, but must have both the closing and opening if present.

    Any mistakenly retrieved phone numbers that are invalid will cause the test to fail.

    Returns a list of strings

    Test with:
    $ py.test tests/test_strings.py::StringExercises::test_extract_usa_phone_numbers
    """
    return None



