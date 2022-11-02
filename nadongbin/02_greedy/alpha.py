data = input()

alpha = []
value = 0
for s in data:
  if s.isalpha():
    alpha.append(s)
  else :
    value += int(s)

alpha.sort()

if value != 0:
  alpha.append(str(value))
print(''.join(alpha))