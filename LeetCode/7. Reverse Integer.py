class Solution:
    def reverse(self, x: int) -> int:   
        x = str(x)
        if x[0] != '-':
            x = x[::-1]
        else:
            rev = x[::-1]
            x = '-'+rev[:-1]
            
        x = int(x)
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            return x
            
# java logic
# java에서 -123/10 결과는 12이고, -123%10은 -3이다. (python(-13,7)과 다름)

# public int reverse(int x) {
#     long res = 0;
#     while (x != 0) {
#         res = res * 10 + x % 10;
#         x = x / 10;
#     }
    
#     if (res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) {
#         return 0;
#     } else {
#         return (int)res;
#     }
# }