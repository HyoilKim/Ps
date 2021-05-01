def solution(rows, columns, queries):
    # rotate 함수
    # [x1,y1, x2,y2] / x1->x2, y1->y2
    # 해당 둘레를 새롭게 저장해서 pop하고 insert한다
    # 다시 해당 둘레를 탐색하면서 값을 넣는다, 최솟값은 사이에 구한다
    answer = []
    
    # 초기화
    mat = [[0]*columns for _ in range(rows)]
    for i in range(0, rows):
        for j in range(1, columns+1):
            mat[i][j-1] = i*columns + j
          
    for x1, y1, x2, y2 in queries:
        ll = []
        # x1-1, y1-1 -> y2-1
        for y in range(y1-1, y2):
            ll.append(mat[x1-1][y])
        # x1 -> x2-1, y2-1
        for x in range(x1, x2):
            ll.append(mat[x][y2-1])
        # x2-1, y2-1 -> y1
        for y in range(y2-2, y1-1, -1):
            ll.append(mat[x2-1][y])
        # x2-1 -> x1-1, y1-1
        for x in range(x2-1, x1-1, -1):
            ll.append(mat[x][y1-1])
            
        # rotate
        ll.insert(0, ll.pop())
        answer.append(min(ll))
        print(ll, answer)
        while len(ll) > 0:
            for y in range(y1-1, y2):
                mat[x1-1][y] = ll.pop(0)
            for x in range(x1, x2):
                mat[x][y2-1] = ll.pop(0)
            for y in range(y2-2, y1-1, -1):
                mat[x2-1][y] = ll.pop(0)
            for x in range(x2-1, x1-1, -1):
                mat[x][y1-1] = ll.pop(0)
    return answer

rows=6
columns=6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns,queries))