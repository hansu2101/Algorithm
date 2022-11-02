n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def back_tracking(num):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            back_tracking(i+1)
            s.pop()
            visited[i] = False

back_tracking(0)
