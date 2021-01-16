from collections import defaultdict

def lengthOfLongestSubstring(s):
    longest_str = ''
    for i in range(len(s)):
        substr = s[i]
        repeat = defaultdict(int)
        repeat[s[i]] = 1

        for j in range(i+1, len(s)):
            if repeat[s[j]]:
                break
            substr += s[j]
            repeat[s[j]] = 1

        if len(longest_str) < len(substr):
            longest_str = substr    
    
    return longest_str

# best solution   
def lengthOfLongestSubstring(s): 
    n = len(s)
    ans = 0 
    mp = {}
    i = 0  # 중복 알파벳 위치
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i) # 중복된 알파벳이 나왔을 때 i의 왼쪽 무시
                                 # 새로운 문자열 에서는 새로운 값
        ans = max(ans, j - i + 1) 
        mp[s[j]] = j + 1 # 중복 되었을 때 그 다음 문자열의 인덱스 저장

    return ans

s = "aabcbad"
res = lengthOfLongestSubstring(s)
print(res)