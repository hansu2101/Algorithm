n = int(input())
dp = [1] * (n+1)
dp[0] = 0
count1, count2 = 0, 0
def pib1(x):
    global count1

    if x == 1 or x==2:
        return 1
    else:
        count1 += 1
        return pib1(x-1) + pib1(x-2)

def pib2(x):
    global dp, count2
    for i in range(2, x):
        dp[i] = dp[i-1] + dp[i-2]
        count2+=1

pib1(n)
pib2(n)
print(count1+1, count2)
