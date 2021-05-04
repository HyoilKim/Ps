# solution
# 1. Find the largest index i such that nums[i] < nums[i + 1]
# 2. Find the largest index j > i such that nums[i] < nums[j].
# 3. Swap nums[j] and nums[i].
# 4. Reverse the sub-array nums[i + 1:].

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:                         # 1.
                k = -1
                for j in range(i, len(nums)):               # 2.
                    if nums[j] > nums[i-1]:
                        k = j
                nums[i-1], nums[k] = nums[k], nums[i-1]     # 3.
                
                l = i; r = len(nums)-1                      # 4.
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                return
            
        nums.reverse()
        return
