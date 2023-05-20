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