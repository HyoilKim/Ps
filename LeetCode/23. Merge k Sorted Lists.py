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
class Solution(object):
    def mergeKLists(self, lists):
        q = PriorityQueue()
        for l in lists:
            while l:
                q.put(l.val)
                l = l.next
        
        head = point = ListNode(0)
        while not q.empty():
            point.next = ListNode(q.get())
            point = point.next
        return head.next

