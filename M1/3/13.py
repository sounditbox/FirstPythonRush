reds = 0
blues = 0
for i in range(43673676, 246368373, 16546):
    if i % 13 == 0:
        print(f'{i} - Красное число!')
        reds += 1
        if reds == 2:
            break
    if i % 17 == 0:
        print(f'{i} - Синее число!')
        blues += 1
        if blues == 2:
            break
else:  # Сработает, если не было break
    print('Все числа чёрные!')
