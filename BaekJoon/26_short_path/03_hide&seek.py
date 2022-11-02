from collections import deque
n, m = map(int, input().split())
graph = [0]*100001
q = deque([n])
visited=[False]*100001
visited[n] = True
def bfs():
    while q:

        x = q.popleft()
        if x == m:
            print(graph[x])
            break

        x1 = x+1
        x2 = x*2
        x3 = x-1
        if 0<=x1<=100000 and (not visited[x1]):
            q.append(x1)
            visited[x1] = True
            graph[x1] = graph[x]+1
        if 0<=x2<=100000 and (not visited[x2]):
            q.appendleft(x2)
            visited[x2] = True
            graph[x2] = graph[x]
        if 0<=x3<=100000 and (not visited[x3]):
            q.append(x3)
            visited[x3] = True
            graph[x3] = graph[x]+1

bfs()
