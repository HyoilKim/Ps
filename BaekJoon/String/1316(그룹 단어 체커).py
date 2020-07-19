n = int(input())
num = 0

for i in range(n):
    group = []
    flag = True
    word = input()

    # 문자열 indexing 가능
    for idx, j in enumerate(word):
        if j in group:
            if word[idx] != word[idx-1]:
                flag = False
        else:
            group.append(j)

    if flag == True:
        num += 1

print(num)