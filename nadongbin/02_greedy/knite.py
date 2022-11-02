input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [(1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, 2), (2, 1), (2, -1)]

count = 0

for step in steps:
  nx = row + step[0]
  ny = row + step[1]

  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  count += 1

print(count)