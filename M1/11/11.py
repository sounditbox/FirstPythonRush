# логирование
import datetime
import time


def logger(file=None):
    def outer(func):
        def inner(*args):
            res = func(*args)
            if file is None:
                print(f'{func.__name__}{args} = {res} - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            else:
                print(f'{func.__name__}{args} = {res} - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', file=open(file, 'a'))
            return res

        return inner

    return outer

@logger(file='logs.txt')
def f(a, b):
    return a + b


@logger(file='logs.txt')
def g(a, b):
    return a * b


print(f(1, 2))
print(g(356, 790))
print(f(7, 35))
print(f(4, 3))
print(g(10, 34))
print(g(101, 42))
print(f(1, 3))
print(g(26, 4002))
