n = int(input())
array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append([x,y])

array.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    print(array[i][0], array[i][1])