from collections import defaultdict
import sys
input = sys.stdin.readline

dic = defaultdict(int)
cnt = 0
while True:
    name = input().rstrip()
    if not name: break
    dic[name] += 1
    cnt += 1

for name in sorted(dic.keys()):
    print(name, '%.4f' % (dic[name]*100 / cnt))
