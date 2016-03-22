def add_and_divide(a, b):
    """
    Modify this function to handle:
    1) Divide by zero
    2) Type errors (if a or b is not numeric)

    Do not just except all Exceptions!

    If type 1) exception return None.
    If type 2) error, return `a`.

    Otherwise return (a + b) / b

    Test with:
    $ py.test tests/test_exceptions.py::ExceptionExercises::test_add_and_divide
    """
    return None


# class ArgIsNoneException:
#     pass

class ArgIsNoneException():
    pass

def throw_my_exception(*args):
    """
    If any single argument == None, throw the `ArgIsNoneException` with
    the message "Arg is None!".

    You may need to modify the class definition above as well.

    This function should always return None.

    Test with:
    $ py.test tests/test_exceptions.py::ExceptionExercises::test_throw_my_exception
    """
    return None



