testcase = int(input())
for i in range(testcase):
    r, s = input().split(' ')
    for c in s:
        print(c*int(r), end='')
    print("")