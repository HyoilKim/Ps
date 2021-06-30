# my solution
# hash, O(NlogN)
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums):
        dic = defaultdict(int)
        for num in nums:
            dic[num] = 1
        
        max_len = 0
        length = 1
        for num in sorted(dic.keys()):
            length = length+1 if dic[num+1] > 0 else 1
            max_len = max(max_len, length)
            
        return max_len

# another solution
# set, O(N)
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums: # idea
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best