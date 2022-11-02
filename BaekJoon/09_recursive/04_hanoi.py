n = int(input())

count = 0
array = []
def hanoi(n, base,temp, goal):
    if n == 1:
        array.append(str(base) + ' ' + str(goal))

    else:
        hanoi(n-1, base, goal, temp)
        array.append(str(base) + ' ' + str(goal))
        hanoi(n-1, temp, base, goal)


hanoi(n, 1, 2, 3)
print(len(array))
print('\n'.join(array))