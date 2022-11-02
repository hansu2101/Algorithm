import sys
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input())))

def quad(x, y, n):
    val = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if val != arr[i][j]:
                print('(',end='')
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                print(')', end='')
                return
    print(val, end='')

quad(0,0,n)