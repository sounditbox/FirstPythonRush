# print(type(range(5, 10)))
for i in range(10):
    print(f'Запущена {i}-я итерация внешнего цикла')
    for j in range(10):
        print(f'Запущена {j}-я итерация внутреннего цикла')
