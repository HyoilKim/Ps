# my solution
# isIn = [-1 for i in range(26)]
# word = input()

# for i, c in enumerate(word):
#     idx = int(ord(c)-97)
#     if isIn[idx] == -1:
#         isIn[idx] = i

# print(' '.join(map(str, isIn)))

# good solution
a = list(map(input().find, map(chr,range(97,123))))
for x in a :
    print(x, end = ' ')

# print(list(map('bc'.find, ['a','b','c'])))