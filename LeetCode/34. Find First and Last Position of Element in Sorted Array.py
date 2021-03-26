# my solution
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]
        
#         left= bisect_left(nums, target)
#         right = bisect_right(nums, target)
#         if left >= len(nums) or right <= 0: # right<=0 은 없어도 아래 if에서 걸러지기 때문에 없어도 됨
#             return [-1,-1]
#         else:
#             if nums[left] == target and nums[right-1] == target:
#                 return [left, right-1]
#             else:
#                 return [-1, -1]

# no library
def searchRange(nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]

print(searchRange([1,2,2,2,3,4], 2))