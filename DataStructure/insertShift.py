arr1=[1,2,3,4,5,6,7]
def insertShiftArray(arr, val):
    n = len(arr)
    if n % 2==0:
      mid = n // 2
      arr.insert(mid,val)
      print(arr)
    else:
        mid =int(n//2)
        arr.insert(mid+1, val)
        print(arr)


insertShiftArray(arr1, 8)
