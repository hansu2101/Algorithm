n = int(input())
result = 0
for i in range(n):
    str1 = str(i)
    sum = 0

    for s in str1:
        sum += int(s)

    division_sum = sum + i

    if division_sum == n:
        result = i
        break

if result == 0:
    print(0)
else:
    print(result)
