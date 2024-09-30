def f():
    a = 42

    def g():
        print(a)

    return g


func = f()
func()
