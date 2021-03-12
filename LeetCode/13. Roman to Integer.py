class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        cur_val = 0
        total = 0
        
        for cur in s:
            prev_val = cur_val
            cur_val = roman[cur]
            
            if prev_val < cur_val:
                total -= prev_val
                total += cur_val - prev_val
            else:
                total += cur_val
                
            prev_val = cur_val
        
        return total