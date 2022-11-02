n = int(input())
array = list(map(int,input().split()))
tool = list(map(int,input().split()))

def carculate(num1, num2, t):
    if t == 0:
        return num1 + num2
    elif t == 1:
        return num1 - num2
    elif t == 2:
        return num1 * num2
    elif t == 3:
        if num1 < 0:
            return -(abs(num1)//num2)
        else:
            return num1//num2

max_val = - int(1e9)
min_val = + int(1e9)
num = array[0]


def back_tracking(idx):
    global num, max_val, min_val
    if idx == n :
        max_val = max(max_val,num)
        min_val = min(min_val,num)
        return


    for t in range(4):
        temp = num
        if tool[t] > 0:
            tool[t]-=1
            num = carculate(temp, array[idx], t)
            back_tracking(idx+1)
            num = temp
            tool[t]+=1

back_tracking(1)
print(max_val)
print(min_val)

# from itertools import permutations
# from collections import deque
#
# n = int(input())
# array = list(map(int,input().split()))
# tool = list(map(int,input().split()))
#
# op = []
#
# for i in range(4):
#     for _ in range(tool[i]):
#         op.append(i)
#
# op_list = list(permutations(op,n-1))
#
# def carculate(num1, num2, t):
#     if t == 0:
#         return num1 + num2
#     elif t == 1:
#         return num1 - num2
#     elif t == 2:
#         return num1 * num2
#     elif t == 3:
#         if num1 < 0:
#             return -(abs(num1)//num2)
#         else:
#             return num1//num2
#
# q = deque(op_list)
#
# max_val = - int(1e9)
# min_val = + int(1e9)
#
# while q:
#     num = array[0]
#     op_l = q.popleft()
#     for i in range(n-1):
#         num = carculate(num, array[i+1], op_l[i])
#
#     max_val = max(max_val,num)
#     min_val = min(min_val,num)
#
# print(max_val)
# print(min_val)
