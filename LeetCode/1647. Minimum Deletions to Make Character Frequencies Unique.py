import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        nums = list(dict(sorted(freq.items(), key=lambda x: x[1])).values())
        res = 0
        visit = set()
        for n in nums:
            while n > 0 and n in visit:
                res += 1
                n -= 1
            visit.add(n)
        return res
