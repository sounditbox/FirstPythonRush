# Функции высшего порядка -
# те функции, которые принимают / возвращают / определяют другие функции

def func(inner):
    print(f'running a func {inner.__name__}')

    return inner


def f(a, b):
    return a + b

def f2(a, b):
    return a * b


