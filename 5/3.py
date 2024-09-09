# Global
a = 1
b = 2


def f():
    # Local
    global a
    a += 10
    d = 42
    e = 100
    print(a, b, c, d, e)




c = 3
f()