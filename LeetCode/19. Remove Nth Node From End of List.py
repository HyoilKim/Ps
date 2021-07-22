# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution(two pass)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        
        cur = head
        for _ in range(length-n-1):
            cur = cur.next
        
        if length == n:
            head = cur.next
        elif cur.next:
            cur.next = cur.next.next
        else:
            return None
            
        return head
        
# best solution(one pass)
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# second try(one pass)
class Solution:
    def removeNthFromEnd(self, head, n):
        cur = head
        while cur:
            tmp = cur
            for _ in range(n):
                tmp = tmp.next
            if not tmp:
                head = cur.next
                break
            if not tmp.next:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head