case = int(input())
for _ in range(case):
    n = int(input())
    cloth = {}
    for i in range(n):
        wear = list(input().split())
        if wear[1] in cloth:
            cloth[wear[1]].append(wear[0])
        else:
            cloth[wear[1]] = [wear[0]]
    cnt = 1
    for type in cloth:
        cnt *= (len(cloth[type])+1)
    print(cnt-1)
