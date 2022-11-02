import sys
input = sys.stdin.readline
import heapq

v,e=map(int, input().split())
start_node = int(input())
INF = int(1e9)
graph = [[]for i in range(v+1)]
for i in range(e):
    n, m, c = map(int,input().split())
    graph[n].append((m,c))

distance = [INF]*(v+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))




dijkstra(start_node)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])