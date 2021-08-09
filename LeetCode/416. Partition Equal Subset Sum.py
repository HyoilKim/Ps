# my solution(time-limit)
# backtracking
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(subsum, idx):            
            for i in range(idx, len(nums)):
                if subsum+nums[i] == half:
                    return True
                if subsum+nums[i] < half and not visited[i]:
                    visited[i] = True
                    if dfs(subsum+nums[i], i+1):
                        return True
                    visited[i] = False          # 삭제시 통과, 40ms
                                                # nums[i] 와 가능한 subset을 모두 체크했음
            return False
        
        nums.sort(reverse=True)
        total = sum(nums)
        visited = [False]*len(nums)
        half = total//2
        return total%2 == 0 and dfs(0, 0)

    # visited를 set으로 구현
    # 60ms
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(subsum, idx):            
            for i in range(idx, len(nums)):
                if subsum+nums[i] == half:
                    return True
                elif subsum+nums[i] < half and subsum+nums[i] not in visited:
                    visited.add(subsum+nums[i])
                    if dfs(subsum+nums[i], i+1):
                        return True
        
        total = sum(nums)
        visited = set()
        half = total//2
        return total%2 == 0 and dfs(0, 0)
    
    # clean code
    def canPartition(self, nums: List[int]) -> bool:        
        def dfs(nums, target):
            if target < 0: return False
            if target == 0: return True
            if target in cache: return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i+1:], target-n): return True
            return False

        total = sum(nums)
        cache = set()
        return total%2 == 0 and dfs(nums, total//2)

# dp+memo solution
class Solution:
    def canPartition(self, nums):
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        return dfs(0, s >> 1)