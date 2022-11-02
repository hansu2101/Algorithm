from collections import deque
import copy
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
promising = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            promising.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))

visited = [False] * len(promising)

def back_tracking(num):
    global answer
    if num==3:
        answer = max(bfs(graph), answer)
        return

    for i in range(len(promising)):
            if not visited[i]:
                x, y = promising[i]
                graph[x][y] = 1
                visited[i]=True
                back_tracking(num+1)
                visited[i]=False
                graph[x][y] = 0

def bfs(graph):
    tmp_graph = copy.deepcopy(graph)
    q = deque(virus)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx <n and 0 <= ny < m:
                if tmp_graph[nx][ny]==0:
                    q.append((nx,ny))
                    tmp_graph[nx][ny]=2

    safe = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                safe += 1
    return safe


back_tracking(0)
print(answer)





