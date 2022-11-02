self_num = []
arr=[]
n=1
while n<=10000:
    dn = n + sum(map(int, str(n)))
    arr.append(dn)
    n+=1

for i in range(1,10001):
    if i not in arr:
        print(i)

