import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse = True)

temp = []
answer = 0
for i in range(n):
    temp.append(arr[i])
    weight = temp[-1]*len(temp)
    answer = max(answer, weight)

print(answer)
