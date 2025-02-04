# Динамическая типизация
#
# a = 42
# a = 'abc'


def f(a: str, b: int, c: float) -> str:
    return a.upper()


# a = 'abc'
ans = f('abc')
ans.upper()
