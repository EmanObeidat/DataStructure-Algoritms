import pytest
from Linked_List.LinkedListInserstion import LinkedList,Node

def test_insertion():
        # Test: Can successfully add a node to the end of the linked list
        my_list = LinkedList()
        my_list.append(1)
        assert my_list.head.value == 1

        # Test: Can successfully add multiple nodes to the end of a linked list
        my_list.append(2)
        my_list.append(3)
        assert my_list.head.value == 1
        assert my_list.head.next.value == 2
        assert my_list.head.next.next.value == 3

        # Test: Can successfully insert a node before a node located in the middle of a linked list
        my_list.insert_before(2, 5)
        assert my_list.head.value == 1
        assert my_list.head.next.value == 5
        assert my_list.head.next.next.value == 2
        assert my_list.head.next.next.next.value == 3

        # Test: Can successfully insert a node before the first node of a linked list
        my_list.insert_before(1, 0)
        assert my_list.head.value == 0
        assert my_list.head.next.value == 1
        assert my_list.head.next.next.value == 5
        assert my_list.head.next.next.next.value == 2
        assert my_list.head.next.next.next.next.value == 3

        # Test: Can successfully insert after a node in the middle of the linked list
        my_list.insert_after(1, 4)
        assert my_list.head.value == 0
        assert my_list.head.next.value == 1
        assert my_list.head.next.next.value == 4
        assert my_list.head.next.next.next.value == 5
        assert my_list.head.next.next.next.next.value == 2
        assert my_list.head.next.next.next.next.next.value == 3

        # Test: Can successfully insert a node after the last node of the linked list
        my_list.insert_after(3, 6)
        assert my_list.head.value == 0
        assert my_list.head.next.value == 1
        assert my_list.head.next.next.value == 4
        assert my_list.head.next.next.next.value == 5
        assert my_list.head.next.next.next.next.value == 2
        assert my_list.head.next.next.next.next.next.value == 3
        assert my_list.head.next.next.next.next.next.next.value == 6
        assert my_list.head.next.next.next.next.next.next.next is None

        print("All tests passed!")
test_insertion()