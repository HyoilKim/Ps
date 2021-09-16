'''
idea
1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
2. All other containers are less wide and thus would need a higher water level in order to hold more water.
3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

time - O(n)
space - O(1)
'''
# best solution
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

# second try success
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        result = 0
        while l < r:
            h = min(height[l], height[r])
            result = max(result, h*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
            