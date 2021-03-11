class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = -1
        
        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            area = (r-l) * h
            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area