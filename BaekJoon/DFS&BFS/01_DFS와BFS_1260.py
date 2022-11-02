import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

temp = []
for i in range(m):
    x, y = map(int, input().split())
    temp.append([x,y])
    temp.append([y,x])
temp.sort(key=lambda x: (x[0],x[1]))

graph = [[]for i in range(n+1)]
for i in range(len(temp)):
    x, y = temp[i]
    graph[x].append(y)

visited_dfs=[False]*(n+1)
visited_bfs=[False]*(n+1)

def dfs(graph, v, visited_dfs):
    print(v, end=' ')
    visited_dfs[v] = True

    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)


def bfs(graph, v, visited_bfs):
    visited_bfs[v] = True
    q = deque([v])
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i]=True


dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)