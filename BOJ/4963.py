import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    graph[y][x] = 2
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < w) and (0 <= Y < h) and (graph[Y][X] == 1):
            DFS(Y, X)

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        graph = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    DFS(i, j)
                    cnt += 1
        print(cnt)
