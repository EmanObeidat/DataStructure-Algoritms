This challenge include how we can write python code that takes an array and return reverse array

## Whiteboard Process
![Whiteboard](../assests/Untitled%20(7).jpg)

## Approach & Efficiency
```
 This approach involves using a For loop to iterate over the indices in reverse order, and an additional array to store the reversed elements.
```
## Solution
```
array = [1, 2, 3, 4, 5]
def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr
print(reverseArray(array))
```