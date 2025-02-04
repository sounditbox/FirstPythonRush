def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'result of {func.__name__}{args} is {result}')
        return result

    return wrapper


def my_func(a):
    return 42 * a


my_func = decorator(my_func)

print(my_func(5))
