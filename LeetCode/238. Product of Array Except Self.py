# my solution
# time - O(N)
# space - O(1)
class Solution:
    def productExceptSelf(self, nums):
        total = except_zero = 1
        zero_cnt = 0
        for num in nums:
            total *= num
            if num == 0: 
                zero_cnt += 1
            else:
                except_zero *= num
        
        result = []
        for num in nums:
            if num != 0:
                result.append(total // num)
            elif num == 0 and zero_cnt >= 2:
                result.append(0)
            elif num == 0 and zero_cnt == 1:
                result.append(except_zero)
        
        return result

# another solution(left to right, right to left)
# time - O(N)
# space - O(1)
class Solution:
    def productExceptSelf(self, nums):
        k = 1
        output = []
        for num in nums:
            output.append(k)
            k *= num
        
        k = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= k
            k *= nums[i]
            
        return output
    
    # simplify
    def productExceptSelf(self, nums):
        ans = [1]*len(nums)
        left = right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return ans