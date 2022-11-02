n = int(input())
current = n
cnt = 0


for i in range(n//3):    #3키로가 0~에서 n개
    if  current % 5 == 0:
        cnt = i + current//5
        print(cnt)
        exit(0)
    current-=3

if n%3 == 0:
    print(n//3)
else:
    print(-1)
