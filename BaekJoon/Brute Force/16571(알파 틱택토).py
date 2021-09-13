def enemy_win(turn):
    for i in range(3):
        if turn == board[i][0] == board[i][1] == board[i][2]:
            return True
        if turn == board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if turn == board[1][1]:
            return True
    return False

def put(turn):
    if enemy_win(3-turn):
        return LOSE

    enemy = 2
    for i in range(9):
        r, c = divmod(i, 3)
        if board[r][c] == 0:
            board[r][c] = turn
            enemy = min(enemy, put(3-turn))
            board[r][c] = 0

    if enemy == 2:
        return DRAW
    else:
        return -enemy

board=[list(map(int, input().split())) for _ in range(3)]
one, two = 0, 0
for row in board:
    one += row.count(1)
    two += row.count(2)

DRAW, WIN, LOSE = 0, 1, -1
result = 0
if one <= two:
    result = put(1)  # 'X' turn
else:        
    result = put(2)  # 'O' turn

if result == DRAW:
    print("D")
elif result == WIN:
    print("W")
else:
    print("L")