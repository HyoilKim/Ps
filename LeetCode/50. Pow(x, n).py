# recursive solution
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

# readable recursive solution
class Solution:
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

# iterative solution
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1
        while n:
            if n % 2: # n & 1
                res *= x
            x *= x
            n //= 2 # n >>= 1
        return res