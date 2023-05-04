This challenge include how we can write python code that insert a number to the middle of array without built in function.
## Whiteboard Process
![whiteboard](./Untitled%20(8).jpg)
## Approach & Efficiency
```
In this code, i create a function and used len to calculate the length of array, then i declare mid variable which equal the length devided by 2.
Also i used if condition, it check if the length equal even number or not. Finally i used insert() which take index and value.
```
## Solution
```
arr1=[1,2,3,4,5,6,7]
def insertShiftArray(arr, val):
    n = len(arr)
    if n%2==0:
      mid = n // 2
      arr=arr.insert(mid,val)
      print(arr)
    else:
        mid = n // 2
        int(mid)
        arr.insert(mid+1, val)
        print(arr)


insertShiftArray(arr1, 8)
```