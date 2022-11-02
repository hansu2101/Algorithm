import sys
import heapq
input = sys.stdin.readline

n = int(input())

all = 0
q=[]
for i in range(n):
    temp = int(input())
    all+=temp
    heapq.heappush(q,temp)

cost = 0
while q:
    x = heapq.heappop(q)
    if x == all:
        break
    y = heapq.heappop(q)
    cost += x+y
    heapq.heappush(q,x+y)

print(cost)