import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

for i in range(n):
    s= input().split()
    command = s[0]
    if command == 'push':
        q.append(int(s[1]))
    if command == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if command == 'size':
        print(len(q))
    if command == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if command == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if command == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
