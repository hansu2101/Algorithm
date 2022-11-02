import math
tc = int(input())

for _ in range(tc):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count=0
    for i in range(n):
        cx, cy, r = map(int,input().split())
        dist1, dist2 = math.sqrt((cx-x1)**2 + (cy-y1)**2), math.sqrt((cx-x2)**2 + (cy-y2)**2)
        if (dist1 > r and dist2 < r) or (dist1 < r and dist2 > r):
            count+=1
    print(count)