# Рекурсивная функция
# База рекурсии - точка входа, где рекурсия заканчивается
import datetime


def f():
    f()


def iter_fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def rec_fact(n):
    if n == 1:
        return 1
    return n * rec_fact(n - 1)


# n! = 1 * 2 * 3 * ... * n
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# n! = n * (n-1)!
# 5! = 5 * 4! = 5 * 4 * 3!
# 1! = 1

# O(1) space
# O(n) time
def iter_fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


# O(1) space
# O(2 ** n) time

# O(n) space
# O(n) time

def cached(func):
    results = {}

    def inner(n):
        if n in results:
            return results[n]
        res = func(n)
        results[n] = res
        return res

    return inner


@cached
def rec_fib(n):
    if n in (0, 1):
        return n
    return rec_fib(n - 1) + rec_fib(n - 2)


start = datetime.datetime.now()
res = rec_fib(25)
end = datetime.datetime.now()

print(f'res:{res}, time: {end - start}')
