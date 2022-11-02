import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int,(input().split()))
graph = [[]for i in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 1:
                q.append((k,i,j))


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while q:
        z,x,y = q.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny]==0:
                    q.append((nz,nx,ny))
                    graph[nz][nx][ny] = graph[z][x][y]+1
bfs()

ans = -1
for i in range(n):
    for j in range(m):
        for k in range(h):
                if graph[k][i][j]==0:
                    print(-1)
                    exit(0)
                ans = max(ans, graph[k][i][j])
print(ans-1)
