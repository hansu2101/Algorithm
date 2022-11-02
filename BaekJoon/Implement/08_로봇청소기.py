import sys
input = sys.stdin.readline
n, m = map(int,input().split())
r, c, d = map(int,input().split())
direction = d+8
dx = [-1,0,1,0] # LURD  URDL0123
dy = [0,1,0,-1]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
wall=[]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            wall.append([i,j])

cur_r, cur_c = r,c
direction = d
count = 0
check = True

while True:

    if direction < 8:
        direction += 8

    if graph[cur_r][cur_c] == 0 and check:
        graph[cur_r][cur_c] =1
        count+=1

    check = False
    for i in range(4):
        left = direction-1
        nx = cur_r + dx[left%4]
        ny = cur_c + dy[left%4]
        direction-=1

        if 0<nx<n and 0<ny<m:
            if graph[nx][ny] == 0:
                cur_r = nx
                cur_c = ny
                check = True
                break

    if check == False:
        nx = cur_r + dx[(direction+2)%4]
        ny = cur_c + dy[(direction+2)%4]

        if 0<nx<n and 0<ny<m and ([nx,ny] not in wall):
            cur_r = nx
            cur_c = ny

        else:
            print(count)
            break






