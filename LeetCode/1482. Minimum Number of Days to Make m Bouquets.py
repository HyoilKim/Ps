class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l+r) // 2
            adj_cnt = 0
            bouquet = 0
            for day in bloomDay:
                adj_cnt = adj_cnt+1 if day <= mid else 0
                if adj_cnt == k:
                    adj_cnt = 0
                    bouquet_cnt += 1
            if bouquet >= m:
                r = mid
            elif bouquet < m:
                l = mid+1
        return l
