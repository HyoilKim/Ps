# 1. Brute Force
# time - O(n^3)
# space - O(1)

# 2. Using Cumulative Sum
# time - O(N^2)
# space - O(N)

# 3. 2 without Space(my solution, TLE)
# time - O(N^2)
# space - O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k: 
                    result += 1
        return result
                    
# 4. Using Hashmap(best solution)
# continuous + negative nums(no sliding window) => hash
# time - O(N)
# space - O(N) / defaultdict를 쓰면 0이 할당되어서 메모리 낭비
class Solution(object):
    def subarraySum(self, nums, k):
        count, total, res = {0: 1}, 0, 0
        for n in nums:
            total += n
            res += count.get(total - k, 0)
            count[total] = count.get(total, 0) + 1
        return res