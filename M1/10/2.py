# n! = 1 * 2 * 3 * ... * n
# 3! = 1 * 2 * 3 = 6
# 5! = 120

# Функция вычисления факториала n по числу n
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


for i in range(1, 50):
    print(factorial(i))

