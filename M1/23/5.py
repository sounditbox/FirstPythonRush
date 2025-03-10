def selection_sort(arr):  # O(n**2)
    n = len(arr)  # Определяем длину массива
    for i in range(n):
        # Находим минимальный элемент в оставшейся неотсортированной части массива
        min_idx = i  # Инициализируем индекс минимального элемента
        for j in range(i + 1, n):
            # Если текущий элемент меньше минимального, обновляем min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Обмен значениями
    return arr  # Возвращаем отсортированный массив


# Пример использования:
arr = [64, 25, 12, 22, 11]  # Исходный массив данных
selection_sort(arr)  # Сортируем массив с помощью функции выбора
print("Отсортированный массив:", arr)
# Вывод: Отсортированный массив: [11, 12, 22, 25, 64]
