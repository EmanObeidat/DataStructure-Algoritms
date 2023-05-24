class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle of the linked list using the two-pointer technique
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half = reverse_linked_list(slow.next)
    slow.next = None

    # Compare the first half with the reversed second half
    current1 = head
    current2 = second_half
    while current1 and current2:
        if current1.val != current2.val:
            return False
        current1 = current1.next
        current2 = current2.next

    return True
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

# Check if the linked list is a palindrome
result = is_palindrome(head)
print(result)  # Output: True

# create another linked list : 1>2>3>4>5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(1) #output: false 
result = is_palindrome(head)
print(result)