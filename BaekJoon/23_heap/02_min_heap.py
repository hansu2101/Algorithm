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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, tmp)
