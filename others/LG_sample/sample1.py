n, t = map(int, input().split())
arr=[]
predict = []
for i in range(n):
    p, s = map(int, input().split())
    predict.append(p+s*t)

for i in range(n-1, 0, -1):
    if predict[i-1]>predict[i]:
        predict[i-1] = predict[i]

print(len(set(predict)))





