cases = int(input())
import sys
sys.setrecursionlimit(50000)
def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if graph[x][y] == 0:
        return False

    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)
    return True


for case in range(cases):
    n, m, p = map(int,input().split())
    graph=[[0] * m for j in range(n)]
    for i in range(p):
        r,c = map(int, input().split())
        graph[r][c] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                count+=1
    print(count)
