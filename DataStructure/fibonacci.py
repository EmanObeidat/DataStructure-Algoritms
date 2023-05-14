 linked-list
def fibonacci_iteration(n):
    list=[]
   
    
    for n1 in range(0,n+1):
            if n1<=1:
                list.append(n1) 
            else:
                first,second=list[len(list)-2],list[len(list)-1]
                sum=first+second
                list.append(sum)

    return list[-1]
res=fibonacci_iteration(3)
print(res)



def fibonacci_recursive(n):
    if n<=1:
        return n
    else:
       return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
print(fibonacci_recursive(4))

 main
