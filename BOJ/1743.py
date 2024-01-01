import sys
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())
graph = [['.' for _ in range(m)] for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
res = []
sum = 0

for i in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = '#'

def DFS(y, x):
    if graph[y][x] == '#':
        global sum
        sum += 1
        graph[y][x] = '.'
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (0 <= X < m) and (0 <= Y < n):
                DFS(Y, X)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            DFS(i ,j)
            res.append(sum)
            sum = 0

if res:
    print(max(res))
else:
    print(0)
