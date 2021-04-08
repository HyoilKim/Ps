class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        # 포인터 이동하면서 max 보다 작으면 res+=height*1
        # max보다 크면 max 업데이트
        l = 0; r = len(height)-1
        lmax = -1; rmax = -1    
        result = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < lmax:
                    result += lmax-height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    result += rmax-height[r]
                else:
                    rmax = height[r]
                r -= 1
        return result


# solution 1 (brute force - O(n^2))
# 각 위치에서 본인 보다 큰 왼/오른쪽 막대를 2개 찾고(없으면 +0)
# 작은 막대 높이 - 본인 높이 를 더한다
# left_max = max(left_max, height[cur])
# right_max = max(right_max, height[cur])
# result += min(left_max, right_max) - height[cur]

# solution 2 (Dp)
# 각 위치별 left_max와 right_max를 미리 구함
# left_max[i] = max(height[cur], left_max[i-1])
# right_max[i] = max(height[cur], right_max[i+1])
# result += min(left_max[cur], right_max[cur])