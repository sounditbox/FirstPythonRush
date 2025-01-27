try:
    10 / 0
except ZeroDivisionError:
    print('Деление на ноль')
except BaseException:
    print('Деление на ноль')
else:
    print('Деление прошло успешно')
finally:
    print('Конец программы')

