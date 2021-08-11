# my solution(Time Limit Exceeded)
# time - O(2^N)
# space - O(N)
class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        def dfs(nums, total):
            if not nums:
                if total == target:
                    self.result += 1
                return
            dfs(nums[1:], total+nums[0])
            dfs(nums[1:], total-nums[0])
            
        self.result = 0
        dfs(nums, 0)
        return self.result
        
# dfs + memoization
# time - O(2^N) / 384ms
# space - O(2^N) / 42.3MB
class Solution:            
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == target:
                    memo[(i, total)] = 1
                else:
                    memo[(i, total)] = 0  # if memo is defaultdict, can skip this line
            else:
                memo[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return memo[(i, total)]

        # idx, value: 특정 위치에서 값이 동일하면 이후는 생략
        memo = {} 
        dfs(0, 0)
        return memo[(0, 0)]

# bfs
# time - O(N^2) / 180ms
# space - O(N^2) / 14.4MB
# nums로 만들 수 있는 모든 경우의 수를 최단거리로 구함
from collections import defaultdict
class Solution:            
    def findTargetSumWays(self, nums, target): 
        queue = {0:1} # 초기화
        for n in nums:
            tmp = defaultdict(int)
            for total, cnt in queue.items():
                tmp[total+n] += cnt
                tmp[total-n] += cnt
            queue = tmp
        return queue[target]