from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
promising = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            promising.append((i,j))
        if graph[i][j] == 1:
            house.append((i,j))

answer = 1e9

for c in combinations(promising,m):
    dist = 0
    for h in house:
        chicken_len =100
        for i in range(m):
            chicken_len = min(chicken_len,abs(c[i][0]-h[0]) + abs(c[i][1]-h[1]))
        dist+=chicken_len
    answer = min(answer,dist)

print(answer)









