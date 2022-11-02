import heapq
import sys
input = sys.stdin.readline
n = int(input())
max_h = []
min_h = []
total = 0
for i in range(n):
    k = int(input())
    if k > 1:
        heapq.heappush(max_h, -k)
    elif k <= 0:
        heapq.heappush(min_h, k)
    else:
        total+=k

while len(max_h)>1:
    x1 = heapq.heappop(max_h)
    x2 = heapq.heappop(max_h)
    total+= x1*x2

while len(min_h)>1:
    x1 = heapq.heappop(min_h)
    x2 = heapq.heappop(min_h)
    total+= x1*x2

if max_h:
    total-=heapq.heappop(max_h)
if min_h:
    total+=heapq.heappop(min_h)

print(total)
