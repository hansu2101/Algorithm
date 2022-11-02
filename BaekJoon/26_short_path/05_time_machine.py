#실패 - 벨만포드로해야함

import heapq
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
INF=int(1e9)

start = 1
def dijkstra(start):
    q = []
    distance=[INF]*(n+1)
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost,i[0]))

    return distance

result = dijkstra(1)
for i in range(2,n+1):
    if result[i]==INF:
        print(-1)
    else:
        print(result[i])
