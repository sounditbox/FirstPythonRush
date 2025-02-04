def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # A list of zero or one elements is already sorted

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    # Compare elements from left and right lists and collect them in order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list


# Example usage:
if __name__ == "__main__":
    unsorted_array = [34, 7, 23, 32, 5, 62]
    sorted_array = merge_sort(unsorted_array)
    print("Sorted array:", sorted_array)
