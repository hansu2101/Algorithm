import sys
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
count = [0,0,0] # -1 0 1

def divide(x, y, n):
    v = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):

            if v != arr[i][j]:
                for p in range(3):   # 0 1 2
                    for q in range(3):# 0 1 2
                        divide(x+p*n//3, y+q*n//3, n//3)
                return

    count[v+1] +=1

divide(0,0,n)
print(count[0])
print(count[1])
print(count[2])