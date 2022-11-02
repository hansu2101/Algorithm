def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target_arr = list(map(int, input().split()))
arr.sort()


for i in range(len(target_arr)):
    tmp = binary_search(arr, target_arr[i], 0, len(arr)-1)
    if tmp == None:
        print(0)
    else:
        print(1)
