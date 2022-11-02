n, m = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

sum_set = set_a | set_b
and_set = set_a & set_b
print(len(sum_set)- len(and_set))