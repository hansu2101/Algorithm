import sys
input = sys.stdin.readline
n, m = map(int,input().split())
graph = []
ans = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
