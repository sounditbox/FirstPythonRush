def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))  # Вывод: 1
print(next(counter))  # Вывод: 2
print(next(counter))  # Вывод: 3
print(next(counter))  # Вывод: 4
print(next(counter))  # Вывод: 5
print(next(counter))  # вызовет StopIteration
