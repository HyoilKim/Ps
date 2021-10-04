# my solution(mod)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend*divisor < 0:
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = sign*(dividend//divisor)  
        
        if res > 2**31-1:
            return 2**31-1
        elif res < -2**31:
            return -2**31
        else:
            return res

    # best solution(without mod)
    def divide(self, a, b):
        sig = (a < 0) == (b < 0) # XOR
        a, b, res = abs(a), abs(b), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1): x += 1
            res += 1 << x
            a -= b << x
        return min(res if sig else -res, 2147483647)