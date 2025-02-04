# Дан отсортированный список.
# Узнать, есть ли в списке определённое значение
import time

numbers = list(range(100000000))
# numbers = [1, 5, 7, 18, 23, 32, 42, 45, 87, 99]
value = 1001


def algo1(nums, val):  # O(n) - линейная зависимость
    return val in nums


def linear(nums, val):  # O(n) - линейная зависимость
    for num in nums:
        if num == val:
            return True
    return False


def binary_search(nums, val):  # O(log(n)) - логарифмическая зависимость
    if not nums:
        return False
    mid_ind = len(nums) // 2
    mid_elem = nums[mid_ind]
    if mid_elem == val:
        return True
    elif mid_elem < val:
        return binary_search(nums[mid_ind + 1:], val)
    else:
        return binary_search(nums[:mid_ind], val)


def binary_search2(nums, val):  # O(log(n)) - логарифмическая зависимость
    left, right = 0, len(nums)
    while left <= right:
        mid_ind = (right - left) // 2 + left
        mid_elem = nums[mid_ind]
        if mid_elem == val:
            return True
        elif mid_elem < val:
            left = mid_ind + 1
        elif mid_elem > val:
            right = mid_ind - 1


def time_it(func, **kwargs):
    start = time.time()
    res = func(**kwargs)
    end = time.time()
    print(res)
    print(f'time: {end - start}')
    return res


time_it(linear, nums=numbers, val=-1)
time_it(binary_search, nums=numbers, val=-1)
time_it(binary_search2, nums=numbers, val=-1)
