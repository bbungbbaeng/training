n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board = sorted(board, key = lambda x : (-x[1], -x[2], -x[3]))
idx = [board[i][0] for i in range(n)].index(k)

for i in range(n):
    if board[idx][1:] == board[i][1:]: # 금, 은, 동메달이 모두 동점인 경우에는 등수가 똑같이 출력되어야 하므로, 리스트에서 동점인 경우 중에서 제일 처음의 값을 등수로 출력함
        print(i + 1)
        break
