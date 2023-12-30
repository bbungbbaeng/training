def DFS(x, y):
    X = x + graph[x][y]
    Y = y + graph[x][y]
    graph[x][y] = 'X'
    if 0 < X < n and graph[X][y] != 'X':
        DFS(X, y)
    if 0 < Y < n and graph[x][Y] != 'X':
        DFS(x, Y)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

DFS(0, 0)

if graph[n - 1][n - 1] == 'X':
    print('HaruHaru')
else:
    print('Hing')
