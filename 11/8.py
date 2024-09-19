# lambda-функции, анонимные функции, inline-функции

# def f():
#     pass
#
# g = f
#
# print(g.__name__)
#
# my_sum = lambda x, y: x + y
#
# print(my_sum.__name__)


nums = [5, 2, 7, 1, 6, 9, 0, 4, 2, 8, 4]
print(list(map(lambda x: x ** 2, nums)))
print(list(filter(lambda x: x > 5, nums)))

nums = [5, 42, 67, 10000000, 6, 9, 120, 64, 82, 245624578, 4]
print(max(nums, key=lambda x: str(x)))
print(min(nums, key=lambda x: x // 10 % 10))
print(sorted(nums, key=lambda x: int(str(x)[::-1])))