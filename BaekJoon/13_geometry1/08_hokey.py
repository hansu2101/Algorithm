import math
W, H, X, Y, P = map(int,input().split())
count = 0
for i in range(P):
    x, y = map(int,input().split())

    dist1 = math.sqrt((X - x) ** 2 + (Y + H / 2 - y) ** 2)
    dist2 = math.sqrt((X + W - x) ** 2 + (Y + H / 2 - y) ** 2)

    if dist1<=H/2 or dist2<=H/2 or (X<=x<=X+W and Y<=y<=Y+H):
        count+=1
print(count)