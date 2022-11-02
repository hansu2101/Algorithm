from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    left = bisect_left(array, left_val)
    right = bisect_right(array, right_val)
    return right-left

n, m = map(int, input().split())
array = list(map(int, input().split()))

result = count_by_range(array, m, m)

if result == 0:
    print(-1)
else:
    print(result)