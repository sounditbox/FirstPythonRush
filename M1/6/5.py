# Вывести сумму квадратов всех трёхзначных чисел, кратных 13

# nums = []
# for i in range(100, 1000):
#     if i % 13 == 0:
#         nums.append(i ** 2)
# print(sum(nums))

print(sum([i ** 2 for i in range(100, 1000) if i % 13 == 0]))

