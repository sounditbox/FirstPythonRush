def fib(n):
    # Функция вычисления n-го числа Фибоначчи
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(10))

for val in [1, 2, 3]:
    print(val)