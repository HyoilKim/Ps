# my solution
# O(NlogN)
from bisect import bisect_right
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        i = bisect_right(sorted_nums, target)
        if sorted_nums[i-1] == target:
            return nums.index(target)
        else:
            return -1


# best solution
# O(logN)
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            
            # 정렬된 곳 찾기
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
