# import sys
#
# n = int(sys.stdin.readline())
# array = []
# for _ in range(n):
#     array.append(int(sys.stdin.readline()))
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start+1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#
#         if right<left:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[right], array[left] = array[left], array[right]
#
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
#
# quick_sort(array, 0, n-1)
#
# for i in array:
#     print(i)
#
#
#
#
#
import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in array:
    print(i)
