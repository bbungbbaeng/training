import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    graph[y][x] = 'X'
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < m) and (0 <= Y < n) and (graph[Y][X] == 1):
            DFS(Y, X)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt = 0
    graph = [[0 for i in range(m)] for j in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j)
                cnt += 1
    print(cnt)
