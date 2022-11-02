n = int(input())
array = list(map(int, input().split()))
array.sort()
prefix = []
temp = 0
for i in range(n):
    temp += array[i]
    prefix.append(temp)
print(sum(prefix))