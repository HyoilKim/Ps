# easy solution
# time - O(NlogN)
class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_binary(n):
            # result = ''
            cnt = 0
            while n > 0:
                n,r = divmod(n, 2)
                # result = str(r)+result
                if r == 1:
                    cnt += 1
            return cnt
        
        return [to_binary(i) for i in range(n+1)]

# 규칙 - 이전 값들에서 모두 1씩 더한 값을 추가한다
# time - O(N)
class Solution(object):
    def countBits(self, num):
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]

    # 속도 향상
    def countBits(self, num: int):
        nextOrder = 2
        tracker = 0
        counter = [0]*(num+1)

        for i in range(1, num+1):
            if i == nextOrder:
                nextOrder *= 2
                tracker = 0
            counter[i] = counter[tracker] + 1
            tracker += 1
        return counter