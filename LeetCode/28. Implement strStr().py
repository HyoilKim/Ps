# time - O(N*M)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
# KMP
# time - O(N+M)