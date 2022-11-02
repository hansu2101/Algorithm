n = int(input())
arr = list(map(int,input().split()))

dp = [[0,0]for _ in range(n)]

dp[0][0]=arr[0]
dp[0][1]=0

for i in range(1, n):

    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+arr[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0]-arr[i])

print(dp(max))