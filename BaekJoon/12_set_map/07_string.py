
string_array = input()
set_array = set()
for i in range(len(string_array)):
    for j in range(i,len(string_array)):
        set_array.add(string_array[i:j+1])

print(len(set_array))

# 집합자료형 추가 add