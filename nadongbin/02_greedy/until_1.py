n, k = map(int, input().split())
result = 0

while True:
  target = (n//k) * k    # target까지 빼줘야함
  result += n - target
  n = target

  if n < k :
    break

  result += 1
  n //= k

result += (n-1)
print(result)