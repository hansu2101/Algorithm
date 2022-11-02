n, k = map(int,input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
coins.reverse()
count = 0
for coin in coins:
    if k == 0:
        break
    count += k//coin
    k %=  coin
print(count)


