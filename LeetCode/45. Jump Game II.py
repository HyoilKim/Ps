# my solution
# time: O(N*M)
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10001] * len(nums)
        dp[0] = 0
        for i, max_h in enumerate(nums):
            for h in range(1,max_h+1):
                if i+h < len(nums):
                    dp[i+h] = min(dp[i]+1, dp[i+h])
        return dp[-1]

# best solution(greedy)
# time: O(N)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps

def jump(self, nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums)-1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times