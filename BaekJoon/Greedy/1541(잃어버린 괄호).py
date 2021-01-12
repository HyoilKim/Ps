# 문제를 잘 읽자!!
expre = input().split('-')
total = 0
flag = True

for e in expre:
    tmp = list(map(int, e.split('+')))
    if flag:
        total += sum(tmp)
        flag = False
    else:
        total -= sum(tmp)

print(total)

