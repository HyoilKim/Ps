class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        unique = ['']
        
        for word in arr:
            for j in unique:
                tmp = word + j
                if len(tmp) == len(set(tmp)):
                    unique.append(tmp)
                    max_len = max(max_len, len(tmp))
                    
        return max_len
