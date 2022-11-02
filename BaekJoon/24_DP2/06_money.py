import sys
sys.stdin.readline
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()
dp = [0]* (k+1)
dp[0] = 1

for coin in coins:
    for v in range(coin, k+1):
        if v-coin >= 0:
            dp[v] += dp[v-coin]

print(dp[k])