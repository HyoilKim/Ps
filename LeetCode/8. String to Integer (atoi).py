# my solution
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "":
            return 0

        flag = False
        if s[0] == '-':
            s = s[1:]
            flag = True
        elif s[0] == '+':
            s = s[1:]

        res = ""
        for c in s:
            if c.isdigit():
                res += c
            else:
                break
              
        if res == "":
            return 0
        else:
            if flag:
                res = -1 * int(res)
                if res < -2**31:
                    return -2**31
                else:
                    return res
            else:
                res = int(res)
                if res > 2**31-1:
                    return 2**31-1
                else:
                    return res

            res = int(res)
            if res > 2**31-1:
                return 2**31-1
            else:
                return res


# best solution(java)
# time: O(N), space: O(1)
class Solution {
    public int myAtoi(String str) {
        int i = 0;
        int sign = 1;
        int result = 0;
        if (str.length() == 0) return 0;

        # Discard whitespaces in the beginning
        while (i < str.length() && str.charAt(i) == ' ')
            i++;

        # Check if optional sign if it exists
        if (i < str.length() && (str.charAt(i) == '+' || str.charAt(i) == '-'))
            sign = (str.charAt(i++) == '-') ? -1 : 1;

        # Build the result and check for overflow/underflow condition
        while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            if (result > Integer.MAX_VALUE / 10 ||
                    (result == Integer.MAX_VALUE / 10 && str.charAt(i) - '0' > Integer.MAX_VALUE % 10)) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            result = result * 10 + (str.charAt(i++) - '0');
        }
        return result * sign;

    }
}