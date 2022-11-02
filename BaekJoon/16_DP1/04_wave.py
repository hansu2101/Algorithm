t = int(input())
dp = [1]*101
dp[3] = 2
for _ in range(t):
    n = int(input())

    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[n-1])