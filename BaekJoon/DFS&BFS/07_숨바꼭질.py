from collections import deque
n, m = map(int, input().split())
graph = [0]*100001
q = deque([n])
def bfs():
    while q:
        x = q.popleft()
        if x == m:
            print(graph[x])
            break
        x1 = x+1
        x2 = x*2
        x3 = x-1
        if 0<x1<=100000 and graph[x1]==0:
            q.append(x1)
            graph[x1] = graph[x]+1
        if 0<x2<=100000 and graph[x2]==0:
            q.append(x2)
            graph[x2] = graph[x] + 1
        if 0<=x3<=100000 and graph[x3]==0:
            q.append(x3)
            graph[x3] = graph[x] + 1

bfs()