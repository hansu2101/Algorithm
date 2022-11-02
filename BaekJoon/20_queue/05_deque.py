import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque()
for i in range(n):
    s = input().split()
    command = s[0]

    if command == 'push_back':
        q.append(s[1])
    if command =='push_front':
        q.appendleft(s[1])
    if command =='front':
        if q:
            print(q[0])
        else:
            print(-1)
    if command == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    if command == 'size':
        print(len(q))
    if command =='empty':
        if q:
            print(0)
        else:
            print(1)
    if command == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if command == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
        pass