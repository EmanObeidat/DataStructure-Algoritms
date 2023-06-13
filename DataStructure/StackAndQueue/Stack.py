class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
    def push(self,value):
        node=Node(value)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value from the top of the stack.
        """
        def pop(self):
            if self.top is None:
                raise EmptyError("Stack is empty!")
            else:
                temp=self.top
                self.top=temp.next
                temp.next=None
            return temp.value
        """
        Returns the value from the top of the stack without removing it.

        Returns:
            The value from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        def peek(self):
            if self.top is None:
                raise EmptyError("Stack is empty!")
            else:
                return self.top.value
# check if the stack is empty return true otherwise false  
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

            
        """   
        A string representation of the stack, showing its elements from top to bottom.
        """
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