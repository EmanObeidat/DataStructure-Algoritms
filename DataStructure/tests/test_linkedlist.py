# import pytest
# from Linked_List.linkedList import LinkedList,Node



# def test_emptyLinkedList():
#     linked_list = LinkedList()
#     assert linked_list.head == None

# def test_insert_linked_list():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     assert linked_list.head.value == 5

# def test_insert_multiple_linked_list():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     assert linked_list.head.value == 15
#     assert linked_list.head.next.value == 10
#     assert linked_list.head.next.next.value == 5


# def test_find_existing_value():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     assert linked_list.includes(10) == True


# def test_find_non_existing_value():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     assert linked_list.includes(20) == False


# def test_to_string():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     assert linked_list.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"

# def test_append_linked_list():
#     linked_list = LinkedList()
#     linked_list.append(5)
#     assert linked_list.head.value == 5


# def test_append_multiple_linked_list():
#     linked_list = LinkedList()
#     linked_list.append(5)
#     linked_list.append(10)
#     linked_list.append(15)
#     assert linked_list.head.value == 5
#     assert linked_list.head.next.value == 10
#     assert linked_list.head.next.next.value == 15


# def test_insert_before_linked_list_middle():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_before(10, 20)
#     assert linked_list.to_string(
#     ) == "{ 15 } -> { 20 } -> { 10 } -> { 5 } -> NULL"

# def test_insert_before_linked_list_first():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_before(15, 20)
#     assert linked_list.to_string(
#     ) == "{ 20 } -> { 15 } -> { 10 } -> { 5 } -> NULL"


# def test_insert_after_linked_list_middle():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_after(10, 20)
#     assert linked_list.to_string(
#     ) == "{ 15 } -> { 10 } -> { 20 } -> { 5 } -> NULL"


# def test_insert_after_linked_list_last():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_after(5, 20)
#     assert linked_list.to_string(
#     ) == "{ 15 } -> { 10 } -> { 5 } -> { 20 } -> NULL"
# def test_insert_after_linked_list_middle():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_after(10, 20)
#     assert linked_list.to_string(
#     ) == "{ 15 } -> { 10 } -> { 20 } -> { 5 } -> NULL"


# def test_insert_after_linked_list_last():
#     linked_list = LinkedList()
#     linked_list.insert(5)
#     linked_list.insert(10)
#     linked_list.insert(15)
#     linked_list.insert_after(5, 20)
#     assert linked_list.to_string(
#     ) == "{ 15 } -> { 10 } -> { 5 } -> { 20 } -> NULL"




# # def test_kth_from_end_greater_than_length():
# #     ll = LinkedList()
# #     ll.head = Node(1)
# #     assert ll.kth_from_end(2) == None


# # def test_kth_from_end_same_length():
# #     ll = LinkedList()
# #     ll.head = Node(1)
# #     ll.head.next = Node(2)
# #     assert ll.kth_from_end(2) == 1


# # def test_kth_from_end_not_positive_integer():
# #     ll = LinkedList()
# #     ll.head = Node(1)
# #     assert ll.kth_from_end(-1) == None


# # def test_kth_from_end_size_1():
# #     ll = LinkedList()
# #     ll.head = Node(1)
# #     assert ll.kth_from_end(1) == 1


# # def test_kth_from_end_happy_path():
# #     ll = LinkedList()
# #     ll.head = Node(1)
# #     ll.head.next = Node(2)
# #     ll.head.next.next = Node(3)
# #     ll.head.next.next.next = Node(4)
# #     assert ll.kth_from_end(2) == 3