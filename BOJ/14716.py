import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(y, x):
    graph[y][x] = 'X'
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if (0 <= X < n) and (0 <= Y < m) and (graph[Y][X] == 1):
            DFS(Y, X)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            DFS(i, j)
            cnt += 1
print(cnt)
