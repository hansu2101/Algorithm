n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

total= 0
low = cost[0]

for i in range(n-1):
    if cost[i] < low:
        low = cost[i]
    total += dist[i] * low
print(total)
