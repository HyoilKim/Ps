# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time-complexity: O(nlogn) / 96ms
# space-complexity: O(n)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        ll = []
        for head in lists:
            while head:
                ll.append(head.val)
                head = head.next
        ll.sort()
        
        head = node = ListNode()
        for i in range(len(ll)):
            node.next = ListNode(ll[i])
            node = node.next
        return head.next

# other solution 1  
# Compare every k nodes (head of every linked list) and get the node with the smallest value.
# time-complexity: O(nk)
# space-complexity: O(n)

# other solution 2 
# priority queue
# time-complexity: O(nlogk) / 156ms
# space-complexity: O(n)
from collections import heapq
class Solution:
    def mergeKLists(self, lists):
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))

        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))

        return head.next

# divede and conquer
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next