import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x, limit):
    visited[y][x] = 1
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < n) and (0 <= Y < n) and (graph[Y][X] > limit) and (visited[Y][X] == 0):
            DFS(Y, X, limit)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

limit = [graph[i][j] for i in range(n) for j in range(n)]
limit = [i for i in range(max(limit) + 1)]
safe = []

for l in limit:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == 0) and (graph[i][j] > l):
                DFS(i, j, l)
                cnt += 1
    safe.append(cnt)
print(max(safe))
