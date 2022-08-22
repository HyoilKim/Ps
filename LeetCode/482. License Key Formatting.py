# My bad answer
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 각 그룹은 1개 이상 k개 이하
        # 첫번째 그룹제외하고 k개 씩 그룹화 해야함
        res = []
        cnt = 0
        for c in s[::-1]:
            if cnt < k:
                if c == '-': continue
                else: 
                    res.insert(0, c)
                    cnt += 1
            elif cnt == k:
                res.insert(0, '-')
                if c == '-':
                    cnt = 0
                else:
                    res.insert(0, c)
                    cnt = 1
                    
        for c in res:
            if c == '-':
                del res[0]
            else: break
        return ''.join(res).upper()
        
# Great answer
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        return '-'.join(s[i:i+k] for i in range(0, len(s), k))[::-1]  
            
