n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)
count = 0
def dfs(graph, v, visited):
    global count
    count+=1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


dfs(graph,1,visited)

print(count-1)