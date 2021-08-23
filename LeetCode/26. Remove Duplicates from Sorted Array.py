# my solution
# time - O(N)
# space - O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in range(-100, 101):
            for j in range(len(nums)):
                if num == nums[j]:
                    nums[idx] = num
                    idx += 1
                    break
        return idx

# best solution
class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0
        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1