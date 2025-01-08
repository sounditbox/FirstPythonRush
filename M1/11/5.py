# filter(func, iter) - func применяется к каждому элементу коллекции,
# func принимает один аргумент и возвращает bool

def greater_than_10(x):
    return x > 10


nums = [5, 42, 67, 10, 6, 9, 120, 64, 2, 8, 4]


# 1 вариант
# nums2 = []
# for i in range(len(nums)):
#     if greater_than_10(nums[i]):
#         nums2.append(nums[i])
# nums = nums2

# 2 вариант
# nums = [el for el in nums if greater_than_10(el)]

# 3 вариант
# nums = list(filter(greater_than_10, nums))
print(nums)