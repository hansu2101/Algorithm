from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target_arr = list(map(int, input().split()))

arr.sort()
result = []
def count(arr, k):
    return bisect_right(arr, k) - bisect_left(arr, k)

for i in range(m):
    result.append(count(arr, target_arr[i]))

print(*result)