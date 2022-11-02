import sys
input = sys.stdin.readline
n = int(input)

arr = [i for i in range(8,0,-1)] # 8 7 6 5 4 3 2 1

stack = [0]
answer = []
seq=[]

for i in range(n):
    seq.append(int(input()))


for target in seq:

    while True:

        if target == stack[-1]:
            stack.pop()
            answer.append('-')
            break

        if target < stack[-1]:
            stack.pop()
            answer.append('-')

        elif target > stack[-1]:
            stack.append(arr.pop())
            answer.append('+')




