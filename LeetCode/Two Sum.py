# my solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

nums = [2,7,11,15]
target = 9
res = twoSum(nums, target)
print(res)

# best solution
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            another = target - v
            
            if another in seen:
                return [seen[another], i]
            
            seen[v] = i
        return []
