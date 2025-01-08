# scopes

# global
a = 42

def f():
    # nonlocal
    a = 1

    def g():
        # nonlocal
        b = 2

        def h():
            # local
            # a = 3
            nonlocal a
            a += 1
            print(a)

        h()

    g()

f()
