import sys
input = sys.stdin.readline
n, m = map(int,input().split())

table=[]
for i in range(n):
    table.append(list(map(int, input().split())))

prefix = [[0 for j in range(n+1)]for i in range(n+1)]
for i in range(n):
    temp = 0
    for j in range(n):
        temp+=table[i][j]
        prefix[i+1][j+1] = temp
for j in range(n):
    temp = 0
    for i in range(n):
        temp+=prefix[i+1][j+1]
        prefix[i+1][j+1] = temp

for case in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])





