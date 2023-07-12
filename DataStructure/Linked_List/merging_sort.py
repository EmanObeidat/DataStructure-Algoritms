def merge_sort(arr):
    """
    Sorts the given array in ascending order using the Merge Sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        None: The original array is sorted in place.

    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)


def merge(left, right, arr):
    """
    Merges two sorted arrays (left and right) into a single sorted array.

    Args:
        left (list): The left half of the array to be merged.
        right (list): The right half of the array to be merged.
        arr (list): The array to store the merged result.

    Returns:
        None: The merged array is stored in the `arr` parameter.

    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [8, 4, 23, 42, 16, 15]
merge_sort(arr)
print("Sorted array:", arr)
