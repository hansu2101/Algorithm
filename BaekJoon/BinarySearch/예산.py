import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())


start = 1
end = max(arr)

while start<=end:
    mid = (start+end)//2
    total = 0
    for i in range(n):
        if arr[i]>= mid:
            total+=mid
        else:
            total+=arr[i]

    if total<=budget:
        start = mid+1
    elif total>budget:
        end = mid-1

print(end)