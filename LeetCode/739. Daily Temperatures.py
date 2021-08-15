# my solution
# time - O(N^2)
# space - O(N)
import heapq
class Solution:
    def dailyTemperatures(self, temperatures):
        heap = []
        result = [0]*len(temperatures)
        for i, temper in enumerate(temperatures):
            while heap and heap[0][0] < temper:
                _, j = heapq.heappop(heap)
                result[j] = i-j
            heapq.heappush(heap, (temper, i))
        return result

# using stack
# time - O(N) / O(2N)
# space - O(N)
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

    