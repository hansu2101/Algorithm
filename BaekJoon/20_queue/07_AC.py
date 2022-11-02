import sys
input = sys.stdin.readline
from collections import deque

cases = int(input())
for case in range(cases):
    seq = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    flag = 0
    reverse = 0
    if n == 0:
        arr = []
    for s in seq:

        if s == 'R':

            reverse +=1
        if s == 'D':
            if len(arr) == 0 :
                flag = 1
                break
            else:
                if reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag == 0:
        if reverse % 2 == 1:
            arr.reverse()
        print('[' + ",".join(arr) + ']')
    else:
        print('error')
