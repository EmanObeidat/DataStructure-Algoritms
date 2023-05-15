# White Board
![White Board](./Untitled%20(12).jpg)
# Approach & Efficiency
```
I created a two class one for linked list and other for Node and used three methods like append , insert after and insert before
```
# Solution
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        elif self.head.value == value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            if current.next:
                new_node.next = current.next
                current.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current and current.value != value:
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node
   

    


# Example usage
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert_before(2, 5)
my_list.insert_after(2, 7)
```
 ## The LinkedList class has three main methods:
 ```
 1.Append: The append method adds a new node to the end of the linked list
 2.Insert Before: The insert_before method inserts a new node before the first occurrence of a specified value.
 3.Insert After: The insert_after method inserts a new node after the first occurrence of a specified value. Similar to the insert before operation
 ```