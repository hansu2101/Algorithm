n, m = map(int, input().split())
import sys
input = sys.stdin.readline
no_see = set(input().strip() for _ in range(n))
no_hear = set(input().strip() for _ in range(m))
result = 0

both = list(no_see & no_hear)
both.sort()
print(len(both))
for i in both:
    print(i)

# 합집합 a|b
# 교집합 a&b



