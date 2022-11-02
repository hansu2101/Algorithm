n = 5 # num of data
m = 5 # 찾고자 하는 부분합 m
data = [1,2,3,2,5]

count = 0
interval_sum=0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)