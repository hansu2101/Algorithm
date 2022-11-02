n = int(input())

d = dict()
answer = 0
for i in range(n):
    word = input()
    l=len(word)-1
    for s in word:
        if s in d:
            d[s] += 10**l
        else:
            d[s] = 10**l
        l-=1

arr = []
for value in d.values():
    arr.append(value)
arr.sort(reverse=True)
for i in range(len(arr)):
    answer += arr[i] * (9-i)
print(answer)