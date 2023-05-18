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
# Code Challenge 6
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


# Code Challenge 7

    def kth_from_end(self, k):
        fast = self.head
        slow = self.head

        # Move the fast pointer ahead by k positions
        for _ in range(k):
            if fast is None:
                return None  # List is shorter than k elements
            fast = fast.next

        # Move both the fast and slow pointers until the fast pointer reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # Return the value of the node pointed to by the slow pointer
        return slow.value
# Create an empty linked list
my_list = LinkedList()

# Insert values
my_list.insert('c')
my_list.insert('b')
my_list.insert('a')
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert_before(2, 5)
my_list.insert_after(2, 7)

# Check if a value exists
print(my_list.includes('b'))  # Output: True
print(my_list.includes('d'))  # Output: False

# Convert the linked list to a string representation
print(my_list.to_string())  # Output: "{ a } -> { b } -> { c } -> NULL"
list1=LinkedList().kth_from_end(7)
print(list1)