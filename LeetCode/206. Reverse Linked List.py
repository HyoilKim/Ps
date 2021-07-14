# my solution
# iteratively
# time - O(n)
# space - O(1)
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
            
# recursively
# time - O(n)
# space - O(n)
class Solution:
    def reverseList(self, head):
        def _reverse(cur, prev=None):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            return _reverse(nxt, cur)
        
        return _reverse(head)
