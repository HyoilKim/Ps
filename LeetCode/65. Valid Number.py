class Solution:
    def isNumber(self, s: str) -> bool:
        met_dot = met_e = met_digit = False
        for i, c in enumerate(s):
            if c in '+-':
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif c in 'eE':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif c.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
