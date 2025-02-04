def f(**kwargs):
    print(kwargs)


print(*[1, 2, 3])
f(one=1, two=2, three=3)
