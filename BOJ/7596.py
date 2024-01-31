cnt = 1
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        board = [input() for _ in range(n)]
        print(cnt)
        for i in sorted(board):
            print(i)
        cnt += 1
