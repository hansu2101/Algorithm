n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([x,y])

array.sort(key = lambda x: (x[1], x[0]))

for i in range(n):
    print(array[i][0], array[i][1])