import sys
input = sys.stdin.readline

# index: 맛의 번호
# value: 갯수
MAX = 1000001
tree = [0]*(MAX*4)

# target: 수정 노드
# diff: 수정 값
# idx: target 까지 도달하는 경로에 있는 노드
def update(start, end, idx, target, diff):
    if target < start or target > end: return
    tree[idx] += diff
    if start == end: return
    mid = (start+end)//2
    update(start, mid, idx*2, target, diff)
    update(mid+1, end, idx*2+1, target, diff)

# n번째 순서에 있는 맛의 번호 찾기
def query(start, end, idx, target):
    if start == end:
        return start
    mid = (start+end)//2
    if target <= tree[idx*2]: # 왼 자식 보다 작거나 같으면 왼쪽으로
        return query(start, mid, idx*2, target)
    else:
        return query(mid+1, end, idx*2+1, target-tree[idx*2])

tc = int(input())
for _ in range(tc):
    cmd = list(map(int, input().rstrip().split()))
    if cmd[0] == 1:
        favor = query(1, MAX, 1, cmd[1])
        print(favor)
        update(1, MAX, 1, favor, -1) # (start,end,idx,target,diff)
    else:
        update(1, MAX, 1, cmd[1], cmd[2])