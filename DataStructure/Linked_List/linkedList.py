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
