import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = deque()
answer = [-1]*n

for i in range(n):
    while stack and (stack[-1][0] < arr[i]):
        tmp, idx = stack.pop()
        answer[idx] = arr[i]
    stack.append([arr[i], i])
print(*answer)