n = int(input())
board = [input().split() for _ in range(n)]

for num, name in sorted(board, key = lambda x : int(x[0])):
    print(num, name)
