x,y,w,h = map(int,input().split())
d1, d2, d3, d4 = x-0, y-0, w-x,h-y
print(min(d1,d2,d3,d4))