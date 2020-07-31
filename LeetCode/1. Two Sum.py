class Solution(object):
    def twoSum(self, nums, target):
        res = []
        tmp = nums[:]
        for i, num in enumerate(tmp):
            target -= num
            res.append(i)
            del nums[i]
            
            if target in nums:
                res.append(nums.index(target)+1)
                return res
            else:
                res.remove(i)
                nums.insert(i, num)
                target += num
                
        return []

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