n, m = map(int,(input().split()))


graph = []
for i in range(n):
    graph.append(list(map(int,input())))

target = []
for i in range(n):
    target.append(list(map(int,input())))

count = 0
for i in range(n-2):
    for j in range(m-2):
        if graph[i][j] != target[i][j]:
            count += 1
            for p in range(i, i+3):
                for q in range(j, j+3):
                    if graph[p][q] ==1:
                        graph[p][q] = 0
                    else:
                        graph[p][q] = 1

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != target[i][j]:
                return False
    return True

if check():
    print(count)
else:
    print(-1)
