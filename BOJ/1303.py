import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    global w, b
    if graph[y][x] == 'W':
        w += 1
    if graph[y][x] == 'B':
        b += 1
    check = graph[y][x]
    graph[y][x] = '#'
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if (0 <= X < n) and (0 <= Y < m) and (graph[Y][X] == check):
            DFS(Y, X)

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
w, b = 0, 0
resw, resb = [], []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            DFS(i, j)
            resw.append(w)
            w = 0
        elif graph[i][j] == 'B':
            DFS(i, j)
            resb.append(b)
            b = 0

sum = 0
for i in resw:
    sum += i ** 2
print(sum, end = ' ')
sum = 0
for i in resb:
    sum += i ** 2
print(sum)
