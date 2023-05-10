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