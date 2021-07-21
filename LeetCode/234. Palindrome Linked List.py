# best solution
# time - O(N)
# space - O(1)
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast: # 홀수이면 slow를 중앙에서 오른쪽으로 한 칸 이동
            slow = slow.next
            
        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        
        return not slow        

# time - O(N)
# space - O(1)
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True