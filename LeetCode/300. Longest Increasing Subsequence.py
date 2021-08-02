# dp solution
# time - O(N^2)
# space - O(N)
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        result = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
            result = max(result, dp[i])
        return result

# binary seach solution(best)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for n in nums:
            idx = bisect_left(dp, n)
            if idx == len(dp):
                dp.append(n)
            else:
                dp[idx] = n
        return len(dp)    
        