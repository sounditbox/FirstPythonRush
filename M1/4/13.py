def func(a, b, c, d):
    print(a, b, c, d)


func(1, 2, 3, 4)
func(b=2, a=1, d=4, c=3)


def power(base, exp=2):
    return base ** exp


print(power(5))
print(power(10))
print(power(100))
print(power(100, exp=5))
print(power(2, 3))

print()