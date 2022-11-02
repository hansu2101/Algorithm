n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
gap= abs(arr[0] + arr[n-1])
answer = [arr[0], arr[n-1]]

while start<end:
    left = arr[start]
    right = arr[end]

    if abs(left + right) < abs(gap):
        answer=[left,right]
        gap = abs(left + right)
        if left + right == 0:
            break
    if left + right > 0:
        end -= 1
    else:
        start += 1

print(answer[0], answer[1])

