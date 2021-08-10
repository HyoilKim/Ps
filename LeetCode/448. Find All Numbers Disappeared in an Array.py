# time - O(N)
# space - O(1)
# 배열의 값을 인덱스로 사용하여서 -표기를 함
# 다시 배열을 보았을 때 -가 아닌 인덱스가 사라진 값임
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num)-1
            nums[idx] = -abs(nums[idx])
            print(nums)
        return [i+1 for i, num in enumerate(nums) if num > 0]
        
# my solution(wrong)
# time - O(N)
# space - O(N)
class Solution:
    def findDisappearedNumbers(self, nums):
        sets = set(nums)
        return [n for n in range(1, len(nums)+1) if n not in sets]