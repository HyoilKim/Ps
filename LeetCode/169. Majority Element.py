# my solution
# time-complexity: O(n)
# space-complexity: O(n)
from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
            if dic[n] >= len(nums)/2:
                return n

# time-complexity: O(nlogn)
# space-complexity: O(1)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]