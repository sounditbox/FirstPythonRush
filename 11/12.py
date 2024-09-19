def f():
    print('bla1')
    yield 1
    print('bla2')
    yield 2
    print('bla3')
    yield 3
    print('bla4')
    yield 4
    print('bla5')
    yield 42
    print('bla6')
    yield 100
    print('bla7')


iter = f()

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))