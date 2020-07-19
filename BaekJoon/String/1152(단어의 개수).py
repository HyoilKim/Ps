# my solution
'''
line = input()
words = line.split(' ')
idx = []

for i, word in enumerate(words):
    if word == '':
        idx.append(i)

# delete시 len이 변경 되기 때문에 뒤에서 삭제
for i in list(reversed(idx)):
    del words[i]

print(len(words))
'''

# split 파라미터 null
print(len(input().split()))