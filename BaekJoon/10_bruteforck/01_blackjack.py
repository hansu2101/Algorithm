from itertools import combinations

n, m = map(int, (input().split()))
array = list(map(int, input().split()))
combination = list(combinations(array, 3))

result = 0

for i in combination:
    temp = sum(list(i))
    if temp > m:
        continue
    else:
        result = max(result, temp)

print(result)