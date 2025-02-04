# Возврат значений
def func():  # Функция ВСЕГДА возвращает какое-то значение
    # return: завершает выполнение функции и
    # подставляет свой аргумент на место вызова функции
    return 42

# NoneType - спец.тип только с одним значением - None
# None это ничего


def func2():
    pass


def func3():
    return


def func4():
    return None


print(func2())
print(func3())
print(func4())

