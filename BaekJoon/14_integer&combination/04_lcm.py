k = int(input())

def GCD(a, b):
    if (a % b) == 0:
        return b
    else:
        return GCD(b, a%b)


def LCM(a,b):
    return a * b // GCD(a,b)

for i in range(k):
    n, m = map(int, input().split())

    print(LCM(n, m))
