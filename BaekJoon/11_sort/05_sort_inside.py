str1 = input()
array=[]
for s in str1:
    array.append(int(s))
array.sort(reverse=True)

for i in array:
    print(i, end='')