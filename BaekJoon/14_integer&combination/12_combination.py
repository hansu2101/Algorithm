n,m = map(int, input().split())

def count_n(x, num):
    cnt = 0
    while x > 0:
        x = x//num
        cnt+=x
    return cnt

count_two = count_n(n, 2) - count_n(m, 2) - count_n(n-m, 2)
count_five = count_n(n, 5) - count_n(m, 5) - count_n(n-m, 5)
print(min(count_five, count_two))