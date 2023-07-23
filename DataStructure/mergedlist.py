class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def mergeTwoLists(l1, l2):
        dummy = ListNode(-1)
        mergedList = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                mergedList.next = l1
                l1 = l1.next
            else:
                mergedList.next = l2
                l2 = l2.next

            mergedList = mergedList.next

        if l1:
            mergedList.next = l1
        if l2:
            mergedList.next = l2

        return dummy.next
