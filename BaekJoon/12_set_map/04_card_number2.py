import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
base = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
base.sort()

def count_range (array, left, right):
    return bisect_right(array, right) - bisect_left(array,left)

for i in target:
    print(count_range(base, i, i), end=' ')
