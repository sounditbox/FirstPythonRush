from math import factorial


# Количество путей

# Напишите функцию для вычисления количества различных путей из верхнего левого угла сетки размером m x n
# в нижний правый угол, используя мемоизацию для оптимизации.

def count_paths(m, n, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]

    if (i, j) == (0, 0):
        return 1
    answer = 0
    if i > 0:
        answer += count_paths(m, n, i-1, j, memo)
    if j > 0:
        answer += count_paths(m, n, i, j - 1, memo)
    memo[(i, j)] = answer
    return answer


def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0

    # Запуск рекурсивной функции с начальной точки (0, 0)
    return count_paths(m, n, m-1, n-1, {})


# Примеры использования
print(unique_paths(33, 57))  # Ожидаемый результат: 28
print(unique_paths(3, 7))  # Ожидаемый результат: 28
print(unique_paths(3, 3))  # Ожидаемый результат: 6
print(unique_paths(1, 1))  # Ожидаемый результат: 1
print(unique_paths(0, 0))  # Ожидаемый результат: 0
