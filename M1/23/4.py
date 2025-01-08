def bubble_sort(nums):  # O(n**2)
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not swapped:
            break


numbers = [5, 7, 2, 85, 3, 52, 87, 33, 66, 8]
bubble_sort(numbers)
print(numbers)
