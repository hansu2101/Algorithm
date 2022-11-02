import sys
input = sys.stdin.readline
n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1]-arr[0]

while start <= end:
    mid = (start + end)//2
    count = 1
    current = arr[0]

    for i in range(1, n):
        if arr[i]-current >= mid:
            count+=1
            current = arr[i]
    if count < c:
        end = mid -1
    else:
        result = mid
        start = mid+1

print(result)
