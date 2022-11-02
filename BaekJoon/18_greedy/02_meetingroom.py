import sys
input = sys.stdin.readline
n = int(input())
meetings=[]
for i in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x : (x[1],x[0]))

end = 0
count=0
for meet in meetings:
    if end <= meet[0]:
        end = meet[1]
        count+=1

print(count)
