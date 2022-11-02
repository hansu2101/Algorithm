n, k = map(int, input().split())
dp = []
for i in range(n+1):
    dp.append([1] * (i+1))

for i in range(1, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    dp[i][i] = dp[i-1][i-1]

print(dp[n][k]%10007)