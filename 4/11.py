def f():
    def g():
        return 42

    return g


inner_func = f()
print(inner_func())
