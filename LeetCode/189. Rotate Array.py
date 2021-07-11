# my solution
# time - O(n^2)
# space - O(1)
class Solution:
    def rotate(self, nums: List[int], k: int):
        for _ in range(k):
            nums.insert(0, nums.pop())

# time - O(n)
# space - O(n)
class Solution:
    def rotate(self, nums, k):
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k] 

# using reverse
# time - O(n)
# space - O(1)
'''
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
'''
class Solution:
    def reverse(self, nums: list, start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

# cyclic replacements
# time - O(n)
# space - O(1)
class Solution:
    def rotate(self, nums: List[int], k: int):
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

# brute force
# time-complexity: O(n*k)
class Solution:
    def rotate(self, nums: List[int], k: int):
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

# extra array
# time - O(n)
# space - O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a

