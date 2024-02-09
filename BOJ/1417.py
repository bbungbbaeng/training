import sys
input = sys.stdin.readline

n = int(input())
one = int(input())
board = [int(input()) for i in range(n - 1)]
cnt = 0

if not board:
    print(0)
else:
    if one <= max(board):
        while 1:
            board.sort(reverse = True)
            board[0] -= 1
            one += 1
            cnt += 1

            if one > max(board):
                break
    print(cnt)
