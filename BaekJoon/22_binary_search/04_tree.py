import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int,input().split()))

start = 1
end = max(arr)
while start <= end:
    mid = (start + end)//2
    count = 0
    for i in range(n):
        if arr[i]-mid > 0:
            count+= arr[i]-mid
    if count >= m:
        start = mid + 1
    else:
        end = mid -1

print(end)

