# декораторы(подменщики) - изменяют поведение функции, не меняя её код

def outer(func):
    def placeholder(*args):
        print('Запущена функция-подмена')
        return func(*args)

    return placeholder

@outer
def f(a, b):
    return a + b


# f = outer(f)

print(f(5, 5))