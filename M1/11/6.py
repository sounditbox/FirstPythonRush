# max(), min(), sorted() list.sort()
# key - функция-критерий

def by_tens_digit(x):
    return x // 10 % 10


def by_str(x):
    return str(x)


nums = [5, 42, 67, 10000000, 6, 9, 120, 64, 82, 245624578, 4]

print(max(nums, key=by_str))
print(min(nums, key=by_str))
print(sorted(nums, key=by_str))

