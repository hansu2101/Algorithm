n = int(input())
hansu=0
for i in range(1,n+1):
    arr = list(map(int,str(i)))
    if i<100:
        hansu +=1
    elif arr[2]-arr[1] == arr[1]-arr[0]:
        hansu+=1

print(hansu)