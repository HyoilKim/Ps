class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                ll, rr = s[l:r], s[l+1:r+1]
                return ll == ll[::-1] or rr == rr[::-1]
            l, r = l+1, r-1
        return True
