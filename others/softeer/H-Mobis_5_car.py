

from collections import deque

v,e,start = map(int, input().split())

graph = [[]for i in range(v+1)]
graph_r = [[]for i in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_r[b].append(a)

dp1 = [0] * (v+1)
dp2 = [0] * (v+1)
q = deque()
q.append(start)
dp1[start]=1

while q:
    now = q.popleft()

    for i in graph[now]:
        if dp1[i] == 0:
            dp1[i]=1
            q.append(i)

q.append(start)
dp2[start]=1

while q:
    now = q.popleft()

    for i in graph_r[now]:
        if dp1[i] == 0:
            dp1[i]=1
            q.append(i)

print(v - sum(dp1)+1, end=' ')  # 최소 등수
print(sum(dp2))                 # 최대 등수