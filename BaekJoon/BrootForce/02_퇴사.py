n = int(input())
arr = [[0,0]]
for i in range(n):
    arr.append(list(map(int,input().split())))

dp = [0]*(n+2)
for i in range(n,0,-1):
    if i + arr[i][0] > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] =max(dp[i+1],dp[i+arr[i][0]]+arr[i][1])

print(dp[1])
