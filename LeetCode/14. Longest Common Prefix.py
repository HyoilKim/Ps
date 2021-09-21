class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        strs.sort(key=lambda x: len(x))
        result = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return result
            result += ch
        return result
    
# second try success
# time - O(N^3) / N: shortest string's length
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        
        for i in range(len(strs[0]), 0, -1):
            prefix = strs[0][:i]
            flag = True
            for j in range(1, len(strs)):
                if not strs[j].startswith(prefix):
                    flag = False
                    break
            if flag:
                return prefix
        
        return ''

    # more fast solution
    # time - O(N^2)
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 