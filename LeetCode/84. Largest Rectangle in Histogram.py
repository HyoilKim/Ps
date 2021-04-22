# my solution - time over
# time complexity: O(NM)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        for incre_h in range(1, max(heights)+1):
            width = 0
            stack = []
            for i, height in enumerate(heights):
                if height >= incre_h:
                    # stack과 height를 수정하면 empty 스택 처리 하지 않아도 됨
                    # stack = [-1], height.append(0)
                    if not stack: 
                        width = 1
                        stack.append(i)
                    elif stack.pop() == i-1:
                        width += 1
                        stack.append(i)
                else:
                    answer = max(answer, width*incre_h)
                    width = 0
                    stack = []
                    
            answer = max(answer, width*incre_h)
            
        return answer

# best solution
# time - O(N^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # case: 1 2
        stack = [-1] # case: 2 1
        ans = 0
        
        for i in range(len(heights)):
            # incresing stack
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = (i-1) - stack[-1]
                ans = max(ans, height * width)
            stack.append(i) 
            
        return ans
    