# 재귀로 풀다가 실패 -> 최적의 방식(그리디)
if __name__=="__main__":
    n = int(input())
    timeList = []
    for i in range(n):
        start, end = map(int, input().split(' '))
        timeList.append((start, end))

    timeList.sort(key = lambda x: (x[1], x[0]))

    endTIme = timeList[0]
    res = 1
    for i in range(1, n):
        if endTIme[1] <= timeList[i][0]:
            endTIme = timeList[i]
            res += 1
    
    print(res)

