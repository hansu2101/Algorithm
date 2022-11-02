import math
tc = int(input())
for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == dist or r1+r2 == dist:
        print(1)
    elif abs(r1-r2) < dist < (r1+r2) :
        print(2)
    else:
        print(0)