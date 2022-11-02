n = int(input())
answer = 0
for i in range(n):
    temp = []
    flag = 0
    word = input()
    for alpha in word:
        if alpha not in temp:
            temp.append(alpha)

        elif temp[-1]==alpha:
            pass
        else:
            flag = 1
            break
    if flag==0:
        answer+=1

print(answer)