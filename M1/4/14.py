

def func(a, b, *args):
    return a, b, args


print(func(1, 2))
print(func(1, 2, 3))
print(func(1, 2, 3, 4))
print(func(1, 2, 3, 4, 5))