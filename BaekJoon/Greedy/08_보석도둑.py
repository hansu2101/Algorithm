import sys
input = sys.stdin.readline
import heapq

n, k = map(int,input().split())

jem = []
for i in range(n):
    m, v = map(int,input().split())
    heapq.heappush(jem,[m,v])

bags = []
for i in range(k):
    bags.append(int(input()))
bags.sort()

total_value = 0
capable_jem = []

for bag in bags:

    while jem and bag>=jem[0][0]:
        m, v = heapq.heappop(jem)
        heapq.heappush(capable_jem,-v)

    if capable_jem:
        total_value -= heapq.heappop(capable_jem)
    elif not jem:
        break
print(total_value)
