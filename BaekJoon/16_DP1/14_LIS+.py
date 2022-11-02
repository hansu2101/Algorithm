n = int(input())
array_a = []
for i in range(n):
    array_a.append(list(map(int, input().split())))

array_a.sort(key=lambda x: x[0])
dp=[1]*n

for i in range(n):
    for j in range(i):
        if array_a[j][1]<array_a[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))