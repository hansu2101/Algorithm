import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
m = int(input())
array2 = list(map(int, sys.stdin.readline().split()))

array.sort()
def binary_search(array, target, start, end):
    while(start<=end):
        mid = (start + end) // 2
        if target == array[mid]:
            return 1
        elif array[mid] > target:
            end = mid-1
        elif array[mid] < target:
            start = mid +1
    return 0

for i in array2:
    result = binary_search(array, i, 0, len(array)-1)
    if result == 0:
        print(0, end=' ')
    else:
        print(1, end=' ')
