from collections import deque
n, m = map(int, input().split())
q = deque([i for i in range(1, n+1)])
target_l = list(map(int, input().split()))
count=0

for i in range(m):
    target = target_l[i]

    if q.index(target) <= len(q)//2:
        for i in range(q.index(target)):
            q.append(q.popleft())
            count += 1
    else:
        for i in range(len(q) - q.index(target)):
            q.appendleft(q.pop())
            count+=1

    if target == q[0]:
        q.popleft()
print(count)
