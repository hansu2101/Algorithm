a, b = map(int,input().split())
count=0

while a<=b:
    if b == a:
        print(count+1)
        break

    if (b-1) % 10 == 0:
        b = (b-1) //10
        count+=1
    elif b%2 == 0:
        b //= 2
        count+=1
    else:
        print(-1)
        break

if a>b:
    print(-1)


