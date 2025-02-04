from functools import lru_cache


def memoize(func):
    results = {}

    def inner(n):
        if n in results:
            return results[n]
        res = func(n)
        results[n] = res
        return res

    return inner


@lru_cache
def rec_fib(n):  # O(n) time, O(n) space
    if n in (1, 2):
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


print(rec_fib(123))