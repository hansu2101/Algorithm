n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()

temp = 0
for i in range(n):
    temp += arr1[i]* arr2.pop(arr2.index(max(arr2)))

print(temp)