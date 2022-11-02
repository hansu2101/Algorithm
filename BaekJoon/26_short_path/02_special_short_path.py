import heapq
import sys
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[]for _ in range(n+1)]
for i in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = int(1e9)
start = 1

def dijkstra(start,v):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:    #i0 = to node i1 = cost
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[v]

v1, v2 = map(int, input().split())

path1 = dijkstra(1,v1)+ dijkstra(v1,v2) + dijkstra(v2,n)
path2 = dijkstra(1,v2)+ dijkstra(v2,v1) + dijkstra(v1,n)

result = min(path1,path2)
if result<INF:
    print(result)
else:
    print(-1)