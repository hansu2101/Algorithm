n = 1260
count = 0

cash = [500, 100, 50, 10]

for coin in cash :
  count += n // coin
  n %= coin

print(count)