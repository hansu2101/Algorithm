n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
count = [0,0]

def divide(x, y, n):
    global count, paper

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != paper[x][y]:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2 , n//2)
                return
    count[paper[x][y]] +=1

divide(0,0,n)
print(count[0])
print(count[1])