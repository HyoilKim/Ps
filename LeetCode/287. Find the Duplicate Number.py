# 1. sort
# time - O(NlogN)
# space - O(N)
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

# 2. Set
# time - O(N)
# space - O(N)
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# 3. Negative Marking
# time - O(N)
# space - O(1)
class Solution:
    def findDuplicate(self, nums):
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate

# 4-1. Array as HashMap(Recursion)
# time - O(N)
# space - O(N) / recursion depth
class Solution:    
    def findDuplicate(self, nums):
        def store(nums, cur):
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)
        
        return store(nums, 0)

# 4-2. Array as Hashmap(Iterative)
# time - O(N)
# space - O(1)
class Solution:
    def findDuplicate(self, nums):
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

# 5. Binary Search
# time - O(NlogN)
# space - O(1)
class Solution:
    def findDuplicate(self, nums):
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate