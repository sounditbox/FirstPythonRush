def f():
    def f2():
        def f3():
            # a = 42
            nonlocal a
            print(a)

        a = 12
        f3()

    a = 5
    f2()


a = 0
f()
