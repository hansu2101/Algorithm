from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global count
    if graph[x][y]==0:
        return False
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx,ny))

                graph[nx][ny]=0
                count+=1
    return True


arr=[]
for x in range(n):
    for y in range(n):
        count = 1
        if bfs(x,y):
            arr.append(count)
arr.sort()
print(len(arr))
for i in range(len(arr)):
    print(arr[i])
