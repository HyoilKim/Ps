# my solution
'''
word = str(input()).upper()
arr = [0 for i in range(26)]
for c in word:
    arr[ord(c)-65] += 1 

preMax = max(arr)
preIdx = arr.index(max(arr))
del(arr[preIdx])
curMax = max(arr)

if preMax == curMax:
    print('?')
else preMax > curMax:
    print(chr(65+preIdx))
'''

# count: 부분 문자열의 개수
# set: 중복제거 순서 임의의 dictionary 반환
n = input().upper()
t = []
for i in set(n) : t.append(n.count(i))
idx = [i for i,x in enumerate(t) if x == max(t)]
if len(idx) > 1 : print('?')
else : print(list(set(n))[t.index(max(t))])
