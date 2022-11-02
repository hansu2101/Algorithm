import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for j in range(n)]for i in range(n)]


for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1


for num_len in range(2,n):
    for start in range(n-num_len):
        end = start + num_len
        if dp[start+1][end-1]==1 and arr[start] == arr[end]:
            dp[start][end]=1


t = int(input())
for i in range(t):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])


