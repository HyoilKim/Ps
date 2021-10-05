# my solution
class Solution:
    def countAndSay(self, n: int) -> str:
        def convert(num):
            res = ''
            ch, cnt = num[0], 1
            for i in range(1, len(num)):
                if ch == num[i]:
                    cnt += 1
                else:
                    res += str(cnt)+ch
                    ch = num[i]
                    cnt = 1
            res += str(cnt)+ch
            return res
    
        res = '1'
        for _ in range(1, n):
            res = convert(res)
        return res
    
# clean code
class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        prev = "1"
        res = ""
        for i in range(1, n):
            count = 1
            for j in range(len(prev)-1):
                if prev[j] == prev[j+1]:
                    count += 1
                else:
                    res += str(count)+prev[j]
                    count = 1
            res += str(count)+prev[-1]
            prev = res
            res = ""
        return prev