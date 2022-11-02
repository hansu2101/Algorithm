n = int(input())
array = list(map(int,input().split()))
array_r = array[::-1]
dp_up=[1]*n
dp_down=[1]*n
for i in range(1,n):
    for j in range(i):
        if array[j]<array[i]:
            dp_up[i]= max(dp_up[i], dp_up[j]+1)
        if array_r[j]<array_r[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

dp_max=[]
dp_down.reverse()
for i in range(n):
    dp_max.append(dp_up[i] + dp_down[i])
print(max(dp_max)-1)

