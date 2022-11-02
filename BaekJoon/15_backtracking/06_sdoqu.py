board = [list(map(int,input().split()))for i in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def check(x,y):
    promining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if board[x][i] in promining:
            promining.remove(board[x][i])
        if board[i][y] in promining:
            promining.remove(board[i][y])

    x//=3
    y//=3
    for p in range(x*3, (x+1)*3):
        for q in range(y*3, (y+1)*3):
            if board[p][q] in promining:
                promining.remove(board[p][q])

    return promining

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)

    else:
        x = blank[idx][0]
        y = blank[idx][1]
        array = check(x, y)

        for c in array:
            board[x][y]=c
            dfs(idx+1)
            board[x][y]=0

dfs(0)

