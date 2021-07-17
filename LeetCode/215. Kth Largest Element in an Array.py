# my solution
# time - O(nlogn)
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

# bubble sort
# time - O(nk)
class Solution:
    def findKthLargest(self, nums, k):
        for i in range(k): # k번째 큰 수 까지만 정렬
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[-k]

# selection sort
# time - O(nk)
class Solution:
    def findKthLargest(self, nums, k):
        for i in range(len(nums), len(nums)-k, -1): # k번째 큰 수 까지만 정렬
            max_idx = 0
            for j in range(i):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[max_idx], nums[i-1] = nums[i-1], nums[max_idx]
        return nums[-k]

# heap sort
from collections import heapq 
class Solution:
    # time - O(n+(n-k)logn)
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums: # O(n)
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k): # O((n-k)*logn)
            heapq.heappop(heap)
        return heapq.heappop(heap)
    
    # time - O(nlogk)
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heap[0]

# quick sort
# best: O(N) / worst: O(N^2) 
class Solution:
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, n, k): # quick select
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        else:
            return self.quickSelect(nums, pos + 1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right] # pick the last one as pivot
        i = left
        for j in range(left, right): # left to right -1
            if nums[j] > pivot: # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i