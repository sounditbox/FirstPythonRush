def insertion_sort(arr):
    # Проходим по каждому элементу массива, начиная со второго
    for i in range(1, len(arr)): # O(n)
        key = arr[i]  # Элемент, который нужно вставить в отсортированную часть
        j = i - 1
        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем key на правильное место
        arr[j + 1] = key
    return arr


# Пример использования
arr = [5, 4, 3, 2, 1]
sorted_arr = insertion_sort(arr)
print("Отсортированный массив:", sorted_arr)
