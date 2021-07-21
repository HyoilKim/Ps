# my solution
# time - O((N+M)log(N+M))
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 == 0:
            left = nums[len(nums)//2-1]
            right = nums[len(nums)//2]
            return (left+right)/2
        else:
            return nums[len(nums)//2]

# best solution
# time - O(log(N+M))
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        if len(A)>len(B): 
            A, B = B, A
        
        total = len(A) + len(B)
        lo = 0
        hi = len(A)
        while lo <= hi:
            # Find Partition in A using a regular binary search method. 
            midA    = (hi+lo)//2
            A_left  = A[midA-1] if midA   != 0    else float('-inf')
            A_right = A[midA]   if len(A) != midA else float('inf')
            
            # Partition index in B derived from A, and moves in opposite direction of Partition A
            # - Median Index is usually midway somewhere, so here should be ~ Total // 2. And we know that:
            # - midA + midB = Total // 2
            # - midB = Total // 2 - midA
            midB    = total//2 - midA       
            B_left  = B[midB-1] if midB   !=0      else float('-inf')            
            B_right = B[midB]   if len(B) != midB  else float('inf')

            if A_left <= B_right and B_left <= A_right:     # If both lefts are less than both rights, ideal partition detected.
                if total %2 == 0:
                    return max(A_left, B_left)/2.0 + min(A_right, B_right)/2.0
                else:
                    return min(A_right, B_right)                
            elif A_left > B_right:                          # A is too big   --> Reduce A partition size
                hi = midA-1
            elif A_left < B_right:                          # A is too small --> Increase A partition size (thereby reducing B)        
                lo = midA+1
        return None