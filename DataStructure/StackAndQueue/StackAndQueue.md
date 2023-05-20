# Stack And Queue
## Approach and Effiency
### 1.Stack
```
push(): The  time complexity O(1) ,it is only updating the top reference. and the space complexity is also o(1), it is creating a new node.

pop(): The  time complexity O(1) ,it is removing from the top reference. and the space complexity is also o(1), it is creating a new node.

peek(): The time complexity O(1) and the  space complexity O(1) , it returns the value of the top element.

is_empty(): The  time complexityO(1) and space complexity O(1), it checks if the top reference is None.
```
### 2.Queue
```
enqueue(): The time complexity and space complexity O(1),it is creating a new node and updating the back reference.

dequeue(): The time complexity and space complexity O(1), it is updating the front reference.

peek(): The time complexity and space complexity O(1),it returns the value of the front element.

is_empty(): The  time complexity and space complexity O(1), it returns true if the front reference is None otherwise return false.
```
## Solution for Stack:
```
class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        node=Node(value)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        return temp.value

    def peek(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.top.value
        
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
        

    def __str__(self):
        current=self.top
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

class EmptyError(Exception):
    pass   


if __name__ ==  "__main__":
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01.push(5)
    # stack_01.push("eman")
    # stack_01.push("mohammad")
    # stack_01.push("obeidat")
    # stack_01.pop()
    

    print(stack_01)
    print(stack_01.top.value)

```
## Solution for Queue:
```
class Node:
    def __init__(self,value,next=None) :
        self.value=value
        self.next=next


class Queue:
    def __init__(self,front=None,back=None):
        self.front=front
        self.back=back
        
    def enqueue(self,value):
        node=Node(value)
        if self.front is None:
            self.back=node
            self.front=node
        else:
            self.back.next=node
            self.back=node
    
    def dequeue(self):
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
        return temp.value
    
    def peek(self):
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.front.value
        
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
        
    def __str__(self):
        current=self.front
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

class EmptyError(Exception):
    pass

if __name__ == "__main__":
    queue_1=Queue()
    queue_1.enqueue("H")
    queue_1.enqueue("e")
    queue_1.enqueue("l")
    queue_1.enqueue("l")
    queue_1.enqueue("o")
    # queue_1.dequeue()
    # queue_1.dequeue()
    print(queue_1.peek())
    print(queue_1.is_empty())
    print(queue_1)

```