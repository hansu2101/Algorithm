n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    global count
    if graph[x][y] !=0:
        graph[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                count+=1
                dfs(nx,ny)
        return True
    return False

arr=[]
for x in range(n):
    for y in range(n):
        count = 1
        if dfs(x,y):
            arr.append(count)
arr.sort()
print(len(arr))
for i in range(len(arr)):
    print(arr[i])