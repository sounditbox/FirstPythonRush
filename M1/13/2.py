class WrongNumberException(ValueError):
    pass


class NonPositiveNumberException(WrongNumberException):
    pass


n = int(input('Угадай положительное целое число:\n'))
if n == 42:
    print('Угадал!')
elif n < 0:
    raise NonPositiveNumberException
else:
    raise WrongNumberException('атата!')

# stdin stdout stderr
# PyQT6 / tkinter
