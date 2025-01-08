# Аргументы: позиционные и именованные

def f(req, *args, a=1, b=2):
    return req, args


print(f(1, 2, 3))
print(f(1, 2, 3, 4))
print(f(1, 2))
print(f(1))


