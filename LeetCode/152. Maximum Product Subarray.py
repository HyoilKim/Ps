# Kadane's Algorithms
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total_max = total_min = result = nums[0]
        for i in range(1, len(nums)):
            max_total = max(nums[i], nums[i]*total_max, nums[i]*total_min)
            min_total = min(nums[i], nums[i]*total_max, nums[i]*total_min)
            total_max, total_min = max_total, min_total
            result = max(result, total_max)
        return result

# swap max, min
def maxProduct(nums):
    r = nums[0]
    imax = imin = r
    for i in range(1, len(nums)):
        if nums[i] < 0:
            imax, imin = imin, imax
        imax = max(nums[i], imax*nums[i])
        imin = min(nums[i], imin*nums[i])
        r = max(r, imax)
    return r