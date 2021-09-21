# time - O(n^2)
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 중복 방지
                continue 
            if nums[i] > 0: # 정렬했기 때문에 num[l], num[r] 모두 양수
                break
            l = i+1
            r = len(nums)-1 
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # 중복 방지
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result

# second try success
class Solution:
    def threeSum(self, nums):
        if len(nums) <= 2: return []
        nums.sort()
        
        result = set()
        for i, n in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l]+nums[r] == -n:
                    result.add((n,nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] < -n:
                    l += 1
                else:
                    r -= 1
        return list(result)
                    
        