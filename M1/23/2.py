# Ряд Фибоначчи: 0 1 1 2 3 5 8 13 21 34 55 89 ...
# F(1) = 0, F(2) = 1, F(n) = F(n-1) + F(n-2)

def iter_fib(n):  # O(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def rec_fib(n):  # O(2**n)
    global call_number
    call_number += 1

    if n in (1, 2):
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


results = {}


def rec_fib_memo(n):  # O(
    global call_number
    call_number += 1

    if n in results:
        return results[n]

    if n in (1, 2):
        result = 1
    else:
        result = rec_fib(n - 1) + rec_fib(n - 2)
    results[n] = result
    return result


def get_call_number():
    global call_number
    for i in range(1, 40):
        results.clear()
        call_number = 0
        print(rec_fib_memo(i))
        print(f'N: {i} | Вызовов: {call_number}')


call_number = 0
get_call_number()
