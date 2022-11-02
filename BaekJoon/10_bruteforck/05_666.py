n = int(input())
cnt = 0
count =0

while True:
    if '666' in str(cnt):
        count+=1

    if count == n:
        print(cnt)
        break

    cnt += 1

# n = int(input())
# cnt = 0
# count =0
# flag = 0
# while True:
#     for s in str(cnt):
#         if s == '6':
#             flag += 1
#             if flag >= 3:
#                 count += 1
#                 break
#
#         elif s != '6' :
#             flag = 0
#
#     if count == n:
#         print(cnt)
#         break
#
#     flag = 0
#     cnt += 1