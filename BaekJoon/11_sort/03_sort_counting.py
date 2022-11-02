import sys

n = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
