# my solution
# set, O(n)
class Solution:
    def singleNumber(self, nums):
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        return result.pop()

# another solution
# set, O(n)
def singleNumber(self, nums):
    return sum(set(nums)) * 2 - sum(nums)

# anther solution
# bit operation(xor)
from functools import reduce
def singleNumber(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
