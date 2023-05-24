import pytest
from Linked_List.zip import LinkedList,Node



def test_linked_list_merge():
    # Creating two Linked lists
    llist1 = LinkedList()
    llist2 = LinkedList()

    # 1. First Linked List: 0 -> 1 -> 2 -> 3
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
    llist1.push(0)

    # 2. Second Linked List: 8 -> 7 -> 6 -> 5 -> 4
    for i in range(8, 3, -1):
        llist2.push(i)

    # Ensure the initial lists are correct
    assert llist1.head.value == 0
    assert llist1.head.next.value == 1
    assert llist1.head.next.next.value == 2
    assert llist1.head.next.next.next.value == 3
    assert llist2.head.value == 8
    assert llist2.head.next.value == 7
    assert llist2.head.next.next.value == 6
    assert llist2.head.next.next.next.value == 5
    assert llist2.head.next.next.next.next.value == 4

    # Merge the linked lists
    llist1.merge(p=llist1, q=llist2)

    # Ensure the merge operation modifies the first linked list correctly
    assert llist1.head.value == 0
    assert llist1.head.next.value == 8
    assert llist1.head.next.next.value == 1
    assert llist1.head.next.next.next.value == 7
    assert llist1.head.next.next.next.next.value == 2
    assert llist1.head.next.next.next.next.next.value == 6
    assert llist1.head.next.next.next.next.next.next.value == 3
    assert llist1.head.next.next.next.next.next.next.next.value == 5
    assert llist1.head.next.next.next.next.next.next.next.next.value == 4

    # Ensure the merge operation modifies the second linked list correctly
    assert llist2.head is None

    print("All test cases passed.")

# Run the test
test_linked_list_merge()
