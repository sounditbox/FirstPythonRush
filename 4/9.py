def f():
    print(42)


def f2():
    print(42)

def b():
    print(21)


def call_this(func):
    print(f'Вызов функции {func.__name__}')
    func()


res1 = call_this(f)
res2 = call_this(b)
print(res1, res2)