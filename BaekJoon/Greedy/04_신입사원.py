import sys
input = sys.stdin.readline
cases = int(input())
for case in range(cases):
    arr = []
    n = int(input())
    for i in range(n):
        a, b = map(int,input().split())
        arr.append([a,b])

    arr.sort(key = lambda x: x[0])

    result = 1
    top = 0
    for i in range(1,n):
        if arr[i][1]<arr[top][1]:
            top = i
            result+=1
    print(result)
