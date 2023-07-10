def insert(sorted_arr, value):
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
