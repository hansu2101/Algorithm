import sys
input = sys.stdin.readline
n, k = map(int, input().split())

items = [[0,0]]
for _ in range(n):
    items.append(list(map(int, input().split())))
items.sort(key = lambda x : (x[0], x[1]))

dp = [[0 for j in range(k+1)]for i in range(n+1)]

for i in range(1, n+1):
    w=items[i][0]
    v=items[i][1]
    for j in range(1,k+1):
        if j < w:
            dp[i][j]  = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])