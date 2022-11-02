from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0 for i in range(n)]for i in range(n)]

for i in range(k):
    x, y = map(int,input().split())
    graph[x-1][y-1] = 2

l = int(input())
times = dict()

for i in range(l):
    x, c = input().split()
    times[int(x)] = c

# r0 u1 l2 d3
direction = 4*1000
dx = [0,-1,0,1]
dy = [1,0,-1,0]

q = deque()
q.append([0,0])
graph[0][0] = 1
time_step = 1

while True:

    x, y = q[-1]
    nx = x + dx[direction % 4]
    ny = y + dy[direction % 4]

    if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
        if graph[nx][ny]==0: #시과없음
            r,c = q.popleft()
            graph[r][c] = 0
        graph[nx][ny] = 1
        q.append([nx, ny])

        if time_step in times:
            if times[time_step] == 'L':
                direction += 1
            else:
                direction -= 1
        time_step+=1
    else:
        print(time_step)
        break
