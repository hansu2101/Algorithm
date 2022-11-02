import sys

n, m = map(int, input().split())
name = dict()
number = dict()

for i in range(1, n+1):
    value = sys.stdin.readline().strip()
    name[value] = i
    number[i] = value

for _ in range(m):
    input = sys.stdin.readline().strip()
    if input.isalpha():
        print(name[input])
    else:
        print(number[int(input)])
