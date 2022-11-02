import sys
input = sys.stdin.readline
from collections import deque
cases = int(input())
for case in range(cases):
    n, m = map(int,input().split())
    q = deque(list(map(int, input().split())))

    count = 0
    while q:

        max_val = max(q)
        if max_val == q[0]:
            q.popleft()
            m -= 1
            count+=1
            if m == -1:
                print(count)
                break

        else:
            q.append(q.popleft())
            if m>0:
                m-=1
            else:
                m= len(q)-1

