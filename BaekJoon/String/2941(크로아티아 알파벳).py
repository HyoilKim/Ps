alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
for i in alpha: 
    word = word.replace(i, '*')    # string.replace
print(len(word))

# count 사용
a = input()
num = 0
for i in alpha:
    num += a.count(i)
print(len(a) - num)