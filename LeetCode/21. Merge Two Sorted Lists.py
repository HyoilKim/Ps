# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else: 
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next

# best solution1(if both lists are non-empty)
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

# best solution2
def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a