# my solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.back(nums, [], answer)
        return self.answer
    
    def back(self, nums, path, answer):
        if nums == []:
            answer.append(path)
            return
        
        answer.append(path)
        for i, n in enumerate(nums, 1):
            self.back(nums[i:], path+[n], answer)
      
# Cascading
# time - O(N*2^N)
# space - O(N*2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# backtracking
# time - O(N*2^N)
# space - O(N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:  
                output.append(curr[:]) # deepcopy
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

# bitmask
# time - O(N*2^N)
# space - O(N*2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output