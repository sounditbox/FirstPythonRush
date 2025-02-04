def func(a, b, c, *args, d=42, **kwargs):
    print(a, b, c, args, d, kwargs)


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, e=12, f=13)
