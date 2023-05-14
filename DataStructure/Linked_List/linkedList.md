 # WHITE BOARD
![white board](./Untitled%20(11).jpg)
# Approach & Efficiency
```
I created a two class one for linked list and other for Node and used three methods like insert , include and to string
```
# Solution
```
import pytest
from Linked_List.linkedList import LinkedList,Node

def test_linked_list():
    # Create an empty linked list
    my_list = LinkedList()

    # Test inserting values
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')

    # Test includes() method
    assert my_list.includes('b') is True
    assert my_list.includes('d') is False

    # Test to_string() method
    expected_output = "{ a } -> { b } -> { c } -> NULL"
    assert my_list.to_string() == expected_output

    # Test inserting additional value
    my_list.insert('d')
    expected_output = "{ d } -> { a } -> { b } -> { c } -> NULL"
    assert my_list.to_string() == expected_output

    # Test Node objects
    node_d = my_list.head
    node_a = node_d.next
    node_b = node_a.next
    node_c = node_b.next

    assert node_d.value == 'd'
    assert node_a.value == 'a'
    assert node_b.value == 'b'
    assert node_c.value == 'c'
    assert node_d.next == node_a
    assert node_a.next == node_b
    assert node_b.next == node_c
    assert node_c.next is None

    print("All tests passed!")

# Run the test
test_linked_list()


```

 ## The LinkedList class has three main methods:
```
(1)insert(value): Inserts a new node at the beginning of the linked list.
(2)includes(value): Checks if a given value exists in the linked list.
(3)to_string(): Converts the linked list into a string representation.
```