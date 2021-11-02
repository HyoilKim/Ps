# my solution
# time - O((N+M)log(N+M))
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[m-i]
        nums1.sort()

# best solution
# time - O(n+m)
def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]