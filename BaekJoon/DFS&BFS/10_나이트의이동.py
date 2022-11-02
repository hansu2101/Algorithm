import sys
input = sys.stdin.readline
from collections import deque

cases = int(input())
for _ in range(cases):
    n = int(input())
    r, c = map(int,input().split())
    goal_r, goal_c = map(int,input().split())
    graph=[[0 for _ in range(n)]for _ in range(n)]
    dx = [-1,-1,1,1,-2,-2,2,2]
    dy = [2,-2,2,-2,1,-1,1,-1]

    q = deque()
    q.append((r,c))
    while q:
        x, y = q.popleft()
        if x == goal_r and y == goal_c:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx,ny))
