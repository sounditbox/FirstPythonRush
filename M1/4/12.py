def power(exp):
    def inner(base):
        return base ** exp

    return inner


square = power(2)
cube = power(3)
tesseract = power(4)

print(square(10))
print(cube(10))
print(tesseract(10))