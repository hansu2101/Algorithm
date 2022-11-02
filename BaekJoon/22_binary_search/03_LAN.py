import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))


start = 1
end = max(arr)

while (start<=end):
    mid = (start+end)//2
    count = 0
    for i in range(k):
        count += arr[i]//mid

    if count >= n:
        start = mid+1
    else:
        end = mid-1

print(end)

