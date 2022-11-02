n, k = map(int, input().split())
array = list(map(int, input().split()))

temp=0
for i in range(k):
    temp+=array[i]
prefix = [temp]
print(prefix)
for i in range(1, n-k+1):
    prefix.append(prefix[i-1] - array[i-1] + array[i-1+k])
print(max(prefix))
