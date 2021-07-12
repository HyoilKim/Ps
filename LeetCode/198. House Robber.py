# my solution
# 예외 케이스 더 생각하고 제출하기
# 초기에 dp[1] 초기화 잘못함
# time - O(n)
# space - O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]

# best solution
# time - O(n)
# space - O(1)
class Solution(object):
    def rob(self, nums):
        prev = cur = 0
        for num in nums:
            pprev = prev # This represents the nums[i-2]th value
            prev = cur # This represents the nums[i-1]th value
            cur = max(num+pprev, prev) # Here we just plug into the formula
        return cur