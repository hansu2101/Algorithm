n = int(input())
#
# dp = [0] * (n+1)  #런타임에러
# dp[1] = 1
# dp[0] = 1
#
# def factorial(n):
#     if dp[n] == 0:
#         return n * factorial(n-1)
#     else:
#         return dp[n]
# print(factorial(n))
import math

temp = list(str(math.factorial(n)))
cnt=0
while True:
    val = temp.pop()
    if val == '0':
        cnt+=1
    else:
        break
print(cnt)