import sys
input = sys.stdin.readline
array = list(input())
n = int(input())

for case in range(n):

    target, l, r = input().split()
    target_n = ord(target)-ord('a')
    prefix = [[0] for i in range(26)]
    temp=0

    for i in range(len(array)):
        if target == array[i]:
            temp+=1
        prefix[target_n].append(temp)

    print(prefix[target_n][int(r)+1] - prefix[target_n][int(l)])

