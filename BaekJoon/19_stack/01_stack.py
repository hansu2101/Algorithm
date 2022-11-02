import sys
input = sys.stdin.readline
n = int(input())
arr = []
stack = []
for _ in range(n):
    arr.append(input().split())

for i in range(n):
    if arr[i][0] == 'push':
        stack.append(arr[i][1])
    elif arr[i][0] == 'top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif arr[i][0] =='pop':
        if len(stack) >0:
            print(stack.pop())
        else:
            print(-1)

