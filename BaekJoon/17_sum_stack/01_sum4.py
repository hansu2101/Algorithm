import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int,(input().split())))
prefix_sum = [0]
temp = 0
for i in array:
    temp += i
    prefix_sum.append(temp)

for _ in range(m):
    p, q = map(int, input().split())

    print(prefix_sum[q]-prefix_sum[p-1])
