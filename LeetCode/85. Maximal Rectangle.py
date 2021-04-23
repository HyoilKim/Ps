# my solution 
# nested 6 for: time over

# best solution
# increasing stack, similar to #84
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        memo = [[0]*w for _ in range(h)]

        # memo[i][j]: 사각형의 최대 높이
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    memo[i][j] = memo[i-1][j] + 1
        return max(self.largestRectangleArea(row) for row in memo)

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, area = [-1], 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]: # 등호 X
                h = heights[stack.pop()]
                w = (i-1) - stack[-1]
                area = max(area), h*w)
            stack.append(i)
        return area