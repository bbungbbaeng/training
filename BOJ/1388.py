n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input()))

def DFS(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 'X'
        for i in [1, -1]:
            Y = y + i
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                DFS(x, Y)

    if graph[x][y] == '|':
        graph[x][y] = 'X'
        for i in [1, -1]:
            X = x + i
            if (X > 0 and X < n) and graph[X][y] == '|':
                DFS(X, y)

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            DFS(i, j)
            cnt += 1

print(cnt)
