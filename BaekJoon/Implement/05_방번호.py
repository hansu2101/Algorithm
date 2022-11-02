word = input()
answer = 1
stack = [0,1,2,3,4,5,6,7,8,6]
for s in word:
    n = int(s)
    if n == 9:
        n=6

    if n in stack:
        stack.remove(n)
    else:
        stack += [0,1,2,3,4,5,6,7,8,6]
        answer+=1
        stack.remove(n)

print(answer)