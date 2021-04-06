# 문제 설명 - 주어진 배열에 존재하지 않은 가장 작은 양수
# time - n
# space - n
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = dict()
        for i in nums:
            if i > 0:
                dic[i] = 1
            
        for i in range(1, 2**31):
            if dic.get(i, 0) == 0:
                return i
            

# best solution
# time - n
# space - 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0) # hash 길이 맞추기
        n = len(nums)
        
        # delete negative integer & >= n
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        # hash값 저장
        for i in range(n): 
            nums[nums[i] % n] += n
        
        # 0 -> doesn't exist
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
            
        return n