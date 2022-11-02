import math
n = int(input())
temp = [i for i in range(n+1)]
prime_tmp = [True] * (n + 1)
prime = []

for i in range(2, int(math.sqrt(n))+1):
    if prime_tmp[i] == True:
        for j in range(i*2, n+1, i):
            if prime_tmp[j] ==True:
                prime_tmp[j] = False

for i in range(2, len(prime_tmp)):
    if prime_tmp[i]:
        prime.append(i)

prime +=[0]
start, end = 0, 0
interval_sum = 0
count = 0
while end < len(prime) and start<=end:

    if interval_sum<n:
        interval_sum += prime[end]
        end += 1

    elif interval_sum>=n:
        if interval_sum==n:
            count+=1
        interval_sum -= prime[start]
        start += 1

print(count)




