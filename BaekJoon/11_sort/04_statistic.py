import sys
from collections import Counter

n = int(input())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

print(int(round(sum(array)/n,0)))

array.sort()
print(array[n//2])

cnt = Counter(array).most_common()

# 카운터 객체 주석
# Counter('hello world').most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(array)-min(array))


