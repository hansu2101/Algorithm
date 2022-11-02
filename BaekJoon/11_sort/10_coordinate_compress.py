import sys
n = int(input())
dict = {}
array = list(map(int, sys.stdin.readline().split()))
sorted_array = sorted(set(array))

for i in range(len(sorted_array)):
    dict[sorted_array[i]] = i

for i in array:
    print(dict[i], end= ' ')

