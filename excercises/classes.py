"""
A calculator that keeps a memory of its past executions.

Your job is to finish MyCalculator class. It must inheirit from
BaseCalculator, and should work like the following:

    c = MyCalculator()     # to start with total=0
    c = MyCalculator(290)  # to start with total=290

You should be able to use the following operations with two
arguments x and y to perform stateless operations:

    print c.add(5, 4)         # 9
    print c.multiply(2, 5.5)  # 11
    print c.subtract(12, 100) # -88
    print c.divide(10, 2)     # 2.5

And stateful operations using the same functions, but with single args:

    c = MyCalculator()           # to start with total=0
    c.add(2)
    print c.get_current_total()  # prints 12
    c.multiply(10)
    print c.get_current_total()  # prints 120

    # And you should be able to get a list of all past states of total
    print c.get_past_totals()    # print [0, 12, 120]

Run tests with:

    $ py.test tests/test_classes.py::ClassesExcercises
"""

class BaseCalculator(object):
    def __init__(self):
        self.total = 0

    def get_current_total(self):
        return self.total

class MyCalculator(BaseCalculator):

    def __init__(self, starting_total=0):
        BaseCalculator.__init__(self)
        self.total = starting_total
        self.stack = [starting_total]

    def get_current_total(self):
        return self.total

    def get_past_totals(self):
        return self.stack

    def dothis(self, func, x, y):
        print x, y
        if y is None:
            self.total = func(self.total, x)
            self.stack.append(self.total)
        else:
            return func(x, y)

    def add(self, x, y = None):
        return self.dothis(lambda a, b: a + b, x, y)

    def multiply(self, x, y = None):
        return self.dothis(lambda a, b: a * b, x, y)

    def subtract(self, x, y = None):
        return self.dothis(lambda a, b: a - b, x, y)

    def divide(self, x, y = None):
        return self.dothis(lambda a, b: a / float(b), x, y)


