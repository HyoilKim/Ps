# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
# best solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = second = head
        for _ in range(n):
            first = first.next
        if not first: # first를 이동 했으니 None 체크(자연스럽게 사고하기)
            return head.next
        while first.next: # first = first.next를 실행하기 때문에 조건이 first가 아닌, first.next
            first = first.next
            second = second.next
        second.next = second.next.next # 항상 first와 second가 n만큼 차이나는 것이 아니기 때문에, second사용
        return head
        
        