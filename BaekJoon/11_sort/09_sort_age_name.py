import sys
n = int(input())
array = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    array.append([int(age), name])

array.sort(key = lambda x : x[0])

for i in range(n):
    print(array[i][0], array[i][1])