n, m = map(int,(input().split()))
board = []
for i in range(n):
    board.append(input())

result = 0
temp_count = 0
count = 1e9

for i in range(n-7):
    for j in range(m-7):
        count_w = 0
        count_b = 0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (r+c) % 2 == 0:  # 짝수번째
                    if board[r][c] != 'W': #짝수번째가 B이면
                        count_w += 1
                    if board[r][c] != 'B': #짝수번째가 W이면
                        count_b += 1
                else:
                    if board[r][c] != 'B': #홀수번째가 W이면
                        count_w += 1
                    if board[r][c] != 'W':  #홀수번째가 B이면
                        count_b += 1
        count = min(count_w, count_b, count)


print(count)


