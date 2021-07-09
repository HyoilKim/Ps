# solution
# len(a) != len(b) -> reset another list's head
# amazing institution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# normal solutioj
class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        lenA, lenB = 0, 0      
        while a:
            lenA += 1
            a = a.next       
        while b:
            lenB += 1
            b = b.next
            
        a, b = headA, headB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                a = a.next      
        elif lenB > lenA:
            for _ in range(lenB-lenA):
                b = b.next              
                
        while a != b:
            b = b.next    
            a = a.next  
        return a