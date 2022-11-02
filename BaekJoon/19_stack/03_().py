n = int(input())
for i in range(n):
    stack = []
    temp = input()
    flag=0

    for s in temp:
        if s =='(':
            stack.append(s)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                flag=-1

    if len(stack)>0 or flag==-1:
        print('NO')
    else:
        print('YES')



