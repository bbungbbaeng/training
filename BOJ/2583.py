import sys
sys.setrecursionlimit(10 ** 6)

m, n, k = map(int, input().split())
graph = [[1 for _ in range(n)] for _ in range(m)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = []
sum = 0

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y2 - y1):
        for j in range(x2 - x1):
            graph[(m - 1) - y1 - i][x1 + j] = 0

def DFS(y, x):
    if graph[y][x] == 1:
        global sum
        sum += graph[y][x]
        graph[y][x] = '#'
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (0 <= X < n) and (0 <= Y < m):
                DFS(Y ,X)

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            DFS(i, j)
            cnt += 1
            result.append(sum)
            sum = 0

print(cnt)
for i in sorted(result):
    print(i, end = ' ')
