from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[]for i in range(n+1)]
for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

q = deque([1])
root = [1]*(n+1)

while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            root[i] = v

for i in range(2,n+1):
    print(root[i])
