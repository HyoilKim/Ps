# my solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        while head.next and head.val < 10**6:
            head.val = 10**6
            head = head.next

        return head.val == 10**6

# another solution
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: return True
            
        return False