n = int(input())
for i in range(n):
    m, n = map(int, input().split())

    dp = []
    for i in range(n+1):
        dp.append([1] * (n+1))

    for i in range(1, n+1):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][i] = dp[i-1][i-1]

    print(dp[n][m])