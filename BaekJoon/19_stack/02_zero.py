import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    num = int(input())
    if num>0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))