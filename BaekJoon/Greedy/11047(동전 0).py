n, money = map(int, input().split(' '))
idx = 0
arr = []

for i in range(n):
    arr.append(int(input()))
    if arr[i] < money:
        idx = i

res = 0
while money > 0:
    res += money // arr[idx]
    money = money % arr[idx]
    idx -= 1
print(res)