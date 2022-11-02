n, m = map(int, input().split())

def GCD(a, b):
    if (a % b) == 0:
        return b
    else:
        return GCD(b, a%b)


def LCM(a,b):
    return a * b // GCD(a,b)

print(GCD(n, m))
print(LCM(n, m))
