n, s = map(int,input().split())
arr = list(map(int,input().split()))

interval_sum = arr[0]
answer = n+1
end = 0
for start in range(n):

    while end < n-1 and interval_sum < s:
        end += 1
        interval_sum += arr[end]
    if interval_sum >= s:
        answer = min(answer,end-start+1)

    interval_sum-=arr[start]

if answer == n+1:
    print(0)
else:
    print(answer)

