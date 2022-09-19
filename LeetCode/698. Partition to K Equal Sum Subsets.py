# solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True) # hit
        buckets = [0]*k
        target = sum(nums) // k
        
        def dfs(i):
            if i == len(nums):
                return set(buckets) == set([target])
            for j in range(k): 
                buckets[j] += nums[i]
                if buckets[j] <= target and dfs(i+1):
                    return True
                buckets[j] -= nums[i]
                if buckets[j] == 0: # hit
                    break
            return False
    
        return dfs(0)
