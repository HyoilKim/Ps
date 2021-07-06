# my solution
# space complexity: O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        
        while head and head.next:
            if head in nodes:
                return head
            else:
                nodes.add(head)
                head = head.next
        return None

# another solution
# space complexity: O(1)
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # 설명:https://leetcode.com/problems/linked-list-cycle-ii/discuss/44774/Java-O(1)-space-solution-with-detailed-explanation.
        while head != slow:
            slow = slow.next
            head = head.next
        return head