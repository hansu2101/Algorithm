from collections import deque
m, n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    q.append([nx,ny])
                    graph[nx][ny] = graph[x][y]+1

bfs()
temp = -1

for i in range(n):
    for j in range(m):
        temp = max(temp,graph[i][j])
        if graph[i][j] == 0:
            print(-1)
            exit(0)
print(temp-1)
