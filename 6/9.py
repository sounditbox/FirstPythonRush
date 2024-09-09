a = [1, 2, 3, 4, 5]
for i in range(len(a) - 1, -1, -1):
    if a[i] % 2 == 0:  # условие для удаления
        del a[i]
