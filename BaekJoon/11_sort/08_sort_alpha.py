import sys

n = int(input())
array=[]
for i in range(n):
    array.append(sys.stdin.readline().strip('\n'))

set_array = set(array)
array = list(set_array)

array.sort()
array.sort(key= len)

for i in range(len(array)):
    print(array[i])