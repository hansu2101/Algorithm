from collections import deque
p, q = map(int,input().split())
ladder = dict()
snake = dict()
for i in range(p):
    inp, out = map(int, input().split())
    ladder[inp] = out
for i in range(q):
    inp, out = map(int, input().split())
    snake[inp] = out

graph = [0]*101
temp = [i for i in range(101)]

q = deque([1])
while q:
    x = q.popleft()
    for i in range(1,7):
        nx = x+i
        if 0<=nx<101 and graph[nx] == 0:
            if nx in ladder:
                graph[nx] = graph[x] + 1
                if graph[ladder[nx]] == 0:
                    graph[ladder[nx]] = graph[x]+1
                    q.append(ladder[nx])
            elif nx in snake:
                graph[nx] = graph[x] + 1
                if graph[snake[nx]] == 0:
                    graph[snake[nx]] = graph[x] + 1
                    q.append(snake[nx])
            else:
                graph[nx] = graph[x] + 1
                q.append(nx)
print(graph[100])


