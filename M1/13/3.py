try:
    x = int(input("Введите число: "))
    y = 10 / x
    y.a
    print(y)
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print('Нужно ввести целое число!')
else:
    print('Введено корректное число')
finally:
    print('Пока!')
print('...')