"""
PROFILING EXCERCISES:
====

1) Exercise: `cProfile`

Try using `cProfile` via `cprofilev`. Make sure you can get up the browser page.

How useful is this for a small file / project like `exercises/profiling.py`? Why?

2) Exercise: `line_profiler`

Try using `line_profiler` as described in the slides.

- Which lines are taking the most time? Can you optimize them?
- Which changes helped the most? Can you verify this in the general case with `timeit` to show your points?

"""

def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []

    s = range(3, n + 1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1

    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m ** 2 - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2*i + 3

    return [2] + [x for x in s if x]

print primes(10000000)

