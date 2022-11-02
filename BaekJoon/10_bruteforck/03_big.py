n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

result = [1] * n
for i in range(n-1):
    for j in range(i+1,n):
        if array[i][0] > array[j][0] and array[i][1] > array[j][1]:
            result[j] += 1
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            result[i] += 1
for i in range(n):
    print(result[i], end=' ')

