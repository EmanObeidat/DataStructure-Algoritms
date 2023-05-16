 # WHITE BOARD
![white board](./Untitled%20(13).jpg)
# Approach & Efficiency
```
I created a two class one for linked list and other for Node and used three methods like insert , include and to string
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

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        if self.head is None:
            return "NULL"
        current = self.head
        result = ""
        while current:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        result += "NULL"
        return result

# Create an empty linked list
my_list = LinkedList()

# Insert values
my_list.insert('c')
my_list.insert('b')
my_list.insert('a')

# Check if a value exists
print(my_list.includes('b'))  # Output: True
print(my_list.includes('d'))  # Output: False

# Convert the linked list to a string representation
print(my_list.to_string())  # Output: "{ a } -> { b } -> { c } -> NULL"


```

 ## The LinkedList class has three main methods:
```
(1)insert(value): Inserts a new node at the beginning of the linked list.
(2)includes(value): Checks if a given value exists in the linked list.
(3)to_string(): Converts the linked list into a string representation.
```