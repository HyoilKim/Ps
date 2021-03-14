from collections import defaultdict

# def lengthOfLongestSubstring(s):
#     longest_str = ''
#     for i in range(len(s)):
#         substr = s[i]
#         repeat = defaultdict(int)
#         repeat[s[i]] = 1

#         for j in range(i+1, len(s)):
#             if repeat[s[j]]:
#                 break
#             substr += s[j]
#             repeat[s[j]] = 1

#         if len(longest_str) < len(substr):
#             longest_str = substr    
    
#     # return longest_str

# best solution 
def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    mp = {} # 알파벳:인덱스
    i = -1  # 중복 알파벳 위치
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i) 
        ans = max(ans, j-i) 
        mp[s[j]] = j
        print(j, i, mp)
    return ans

s = "pwwkew"
res = lengthOfLongestSubstring(s)
print(res)