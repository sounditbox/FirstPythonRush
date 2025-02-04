# Функция - именованный участок кода

def func(a, b, c, *args, d=42, **kwargs):
    print(a, b, c, args, d, kwargs)


# func(1, 2, 3)
# func(1, 2, 3, 4, 5)
# func(1, 2, 3, 4, 5, 6, 7)
func(1, 2, 3)
func(1, 2, 3, 4, 5, d=111)
func(1, 2, 3, 4, 5, d=111, e=123, f=90)