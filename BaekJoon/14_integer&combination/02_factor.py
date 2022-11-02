n = int(input())
array = list(map(int,input().split()))
array.sort()
if n % 2 ==0:
    print(array[0] * array[-1])
else:
    print(array[n//2]**2)