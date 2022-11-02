n = int(input())
array = list(map(int, input().split()))
temp = []
top = 1
bottom = 1
def gcd(a, b):
    if a % b==0:
        return b
    else:
        return gcd(b, a%b)

for i in range(n-1):
    top *= array[i]
    bottom *= array[i+1]
    greatest = gcd(top, bottom)
    print(str(round(top/greatest)) + '/' + str(round(bottom/greatest)))