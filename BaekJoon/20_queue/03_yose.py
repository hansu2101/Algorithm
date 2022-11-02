from collections import deque

n, k = map(int,(input().split()))
answer = []
q = deque([i for i in range(1,n+1)])

for i in range(n):
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())
print('<',end='')
for i in range(n-1):
    print(answer[i], end= ', ')
print(answer[-1], end='')
print('>')