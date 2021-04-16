import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
        return tree[node]

# start: 시작 인덱스, end: 끝 인덱스
# left, right: 구간 합을 구하고자 하는 범위
def sum(start, end, node, left, right):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start+end)//2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

# index: 구간 합을 수정하고자 하는 노드
# diff: 수정할 값
def update(start, end, node, index, diff):
    if index < start or index > end: return
    tree[node] += diff
    if start == end: return
    mid = (start+end)//2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

n = int(input())
tree = [0]*(n*4)

# ability 기준으로 정렬
# dic - {cur_rank : ability}
dic = {} 
for i in range(n):
    dic[i+1] = int(input())

# 현재 순위 - 본인 보다 낮은 ability 개수 : 최종 순위
# 본인 보다 낮은 ability는 sum의 결과로 알 수 있음
result = {}
for k, v in sorted(dic.items(), key=lambda x:x[1]):
    result[v] = k-sum(0, n-1, 1, 0, k)
    update(0, n-1, 1, k, 1)

for k, v in dic.items():
    print(result[v])
