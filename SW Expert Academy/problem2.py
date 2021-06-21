import sys
input = sys.stdin.readline

def filtering(num, filt, start_idx):
    j = start_idx                      # replace index
    for i in range(len(filt)):
        if filt[i] == '+':
            if num[j] == '9':
                return 0
            num = num[:j] + str(int(num[j])+1) + num[j+1:]
        elif filt[i] == '-':
            if num[j] == '0':
                return 0
            num = num[:j] + str(int(num[j])-1) + num[j+1:]
        j += 1
    return num  

def solution(num, filt, cnt, idx):
    if int(num) == int(target):
        global min_cnt
        min_cnt = min(min_cnt, cnt)
        return 
    
    for i in range(idx, len(num)-len(filt)+1):
        filter_num = filtering(num, filt, i)
        if filter_num and filter_num not in nums:
            nums.add(filter_num)
            # print(filter_num, filt, cnt, idx)
            solution(filter_num, filt, cnt+1, idx)
            solution(filter_num, filt, cnt+1, idx+1)
            solution(filter_num, filt[::-1], cnt+1, idx+1)

tc = int(input())
for i in range(tc):
    num, target, _ = input().split()
    filt = input().rstrip()
    min_cnt = float('inf')
    nums = set()
    solution(num, filt, 0, 0)
    solution(num, filt[::-1], 0, 0)
    if min_cnt == float('inf'):
        min_cnt = -1
    print("#{0} {1}".format(i+1, min_cnt))
