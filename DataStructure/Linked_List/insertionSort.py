def insert(sorted_arr, value):
    '''
    
    Inserts a value into a sorted array in its appropriate position.

    Args:
        sorted_arr (list): A sorted list of values in ascending order.
        value: The value to be inserted into the sorted array.

    Returns:
        None: The function modifies the sorted_arr in-place.

    Description:
        This function inserts the given value into the sorted_arr such that the resulting array remains sorted in
        ascending order. It finds the appropriate position for the value by comparing it to each element in the array,
        starting from the beginning, until it finds an element that is greater than the value. It then shifts the
        remaining elements one position to the right and inserts the value into the correct position.
    '''
    i = 0
    while value > sorted_arr[i]:
        i += 1
        if i == len(sorted_arr):
            break
    while i < len(sorted_arr):
        temp = sorted_arr[i]
        sorted_arr[i] = value
        value = temp
        i += 1
    sorted_arr.append(value)

def insertion_sort(input_arr):
    '''
    Sorts a list of values using the insertion sort algorithm.

    Args:
        input_arr (list): A list of values to be sorted.

    Returns:
        list: The sorted list of values in ascending order.

    Description:
        This function sorts the input_arr using the insertion sort algorithm. It iterates over each element in the input
        array, starting from the second element. For each element, it calls the insert function to insert the element into
        the appropriate position in the sorted_arr. Finally, it returns the sorted_arr.
    '''
    if not input_arr:
        return []
    sorted_arr = [input_arr[0]]
    for i in range(1, len(input_arr)):
        insert(sorted_arr, input_arr[i])
    return sorted_arr

# Test Case 1: [8, 4, 23, 42, 16, 15]
input_arr = [8, 4, 23, 42, 16, 15]
sorted_arr = insertion_sort(input_arr)
print("Test Case 1 Output:", sorted_arr)

# Test Case 2: [20, 18, 12, 8, 5, -2]
input_arr = [20, 18, 12, 8, 5, -2]
sorted_arr = insertion_sort(input_arr)
print("Test Case 2 Output:", sorted_arr)

# Test Case 3: [5, 12, 7, 5, 5, 7]
input_arr = [5, 12, 7, 5, 5, 7]
sorted_arr = insertion_sort(input_arr)
print("Test Case 3 Output:", sorted_arr)

# Test Case 4: [2, 3, 5, 7, 13, 11]
input_arr = [2, 3, 5, 7, 13, 11]
sorted_arr = insertion_sort(input_arr)
print("Test Case 4 Output:", sorted_arr)
