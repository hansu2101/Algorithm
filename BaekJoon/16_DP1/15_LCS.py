array1 = list(input())
array2 = list(input())
print(array1)
dp = [0]* 1001
for i in range(array1):
    for j in range(i):
        if array1[j] < array1[i]:
            dp[i] = max(dp[i], dp[j+1])