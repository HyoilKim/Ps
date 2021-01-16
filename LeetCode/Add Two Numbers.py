# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = []
        while True:
            n1.append(str(l1.val))
            l1 = l1.next
            if not l1:
                break
        
        n2 = []
        while True:
            n2.append(str(l2.val))
            l2 = l2.next
            if not l2:
                break
            
        n1 = int(''.join(reversed(n1)))
        n2 = int(''.join(reversed(n2)))
        res = list(map(int, ''.join(str(n1+n2))))
        
        pre = ListNode(res[0])
        for i in range(1, len(res)):
            cur = ListNode(res[i])
            cur.next = pre
            pre = cur
        
        return pre

# best solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next