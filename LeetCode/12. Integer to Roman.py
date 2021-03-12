class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',
                 40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        res = ""
        for v, s in roman.items():
            q = num // v
            r = num % v
            if q == 0:
                continue
            else:
                res += (s*q)
            num = r
        
        return res
    
    # num으로 종료 조건
    def intToRoman(num):
        result = ''
        mapping = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    
        while num != 0:
            for k, v in mapping.items():
                if num >= k:
                    dividend = int(num/k)
                    num %= k
                    result += dividend*v
        return result