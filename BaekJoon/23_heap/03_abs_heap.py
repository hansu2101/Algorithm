import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(tmp), tmp))



