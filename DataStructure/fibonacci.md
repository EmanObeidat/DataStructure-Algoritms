## Whiteboard Process
![fibonacci](./Untitled%20(9).jpg)
## Approach & Efficiency
I used two ways to write fibonacci function, the first one by using recursion, and the second one by using iteration"for loop"
## Solution
```
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

results1=fibonacci_recursive(4) 
print(results1,)   

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for n1 in range(2, n+1):
            a, b = b, a + b
        return b
res=fibonacci_iterative(3)

print(res)
```
## Algorithm
```
1. Start with n as the input value for which you want to find the Fibonacci number.
2. If n is 0 or 1, return n as the Fibonacci number.
3. Initialize variables a and b to 0 and 1, respectively.
4. Loop from i = 2 to n:
      a. Calculate the next Fibonacci number as the sum of a and b.
      b. Update a to the value of b.
      c. Update b to the calculated Fibonacci number.
5. After the loop, the value of b will be the nth Fibonacci number.
6. Return b as the result.
```