import heapq
import sys
input = sys.stdin.readline

n = int(input())
l_heap = []
r_heap = []
for i in range(n):
    x = int(input())

    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, -x)
    else:
        heapq.heappush(r_heap, x)

    if r_heap and -l_heap[0] > r_heap[0]:
        l = -heapq.heappop(l_heap)
        r = heapq.heappop(r_heap)
        heapq.heappush(l_heap, -r)
        heapq.heappush(r_heap, l)

    print(-l_heap[0])
