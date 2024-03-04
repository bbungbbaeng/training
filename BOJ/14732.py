board = [[0] * 501 for _ in range(501)]
n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

cnt = 0
for row in board:
    cnt += sum(row)
print(cnt)  
