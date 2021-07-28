# time - O(N)
# space - O(K)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        deq, n, ans = deque(), len(nums), []

        for i in range(n):
            # deq에 idx 값을 넣어서 window 범위를 벗어나면 pop
            while deq and deq[0] <= i-k:
                deq.popleft()
                
            # deq는 내림차순 정렬로 조작
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            ans.append(nums[deq[0]])
        
        return ans[k-1:]