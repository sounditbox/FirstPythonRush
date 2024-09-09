# n! = 1 * 2 * 3 * ... * (n-1) * n = n * (n-1)!

# 5! = 1 * 2 * 3 * 4 * 5 = 120 = 5 * 4!

def fib2(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fib(n):
    if n == 1:
        return 1
    else:
        return fib(n - 1) * n


print(fib(5))
