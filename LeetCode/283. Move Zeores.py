# my solution
# time - O(N)
# space - O(1), in place
class Solution:
    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else: # no zero in nums, replace itself -> elif zero > 0
                nums[i-zero], nums[i] = nums[i], nums[i-zero]
            