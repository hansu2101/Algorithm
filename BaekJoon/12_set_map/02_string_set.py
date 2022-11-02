# import sys
# n, m = map(int, input().split())
# array1 = []
# array2 = []
# count = 0
# for i in range(n):
#     array1.append(sys.stdin.readline())
# for i in range(m):
#     array2.append(sys.stdin.readline())
#
# for s in array2:
#     if s in array1:
#         count+=1
# print(count)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array1 = [input() for _ in range(n)]

count = 0
for i in range(m):
    word = input()
    if word in array1:
        count+=1
print(count)