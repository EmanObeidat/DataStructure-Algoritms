class Node:
    def __init__(self,value,next=None) :
        self.value=value
        self.next=next


class Queue:
    def __init__(self,front=None,back=None):
        self.front=front
        self.back=back
        """
        Adds a new element to the back of the queue.

        Args:
            value: The value to be added.

        Returns:
            None
        """
        def enqueue(self,value):
            node=Node(value)
            if self.front is None:
                self.back=node
                self.front=node
            else:
                self.back.next=node
                self.back=node
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The value of the element removed.

        Raises:
            Exception: If the queue is empty.
        """
        def dequeue(self):
            if self.front is None:
                raise EmptyError("Stack is empty!")
            else:
                temp=self.front
                self.front=temp.next
                temp.next=None
            return temp.value
        """
        Returns the value of the element at the front of the queue without removing it.

        Returns:
            The value of the element at the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        def peek(self):
            if self.front is None:
                raise EmptyError("Stack is empty!")
            else:
                return self.front.value
# check if queue is empty and return true otherwise false       
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
# return the values of queue in a string.    
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