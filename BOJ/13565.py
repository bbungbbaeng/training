import sys
sys.setrecursionlimit(10 ** 6) # 재귀 허용 깊이를 늘려주는 기능, 백준 서버의 경우 허용 깊이가 1000 밖에 안되기 때문에 수동으로 늘려줘야 함

def DFS(y, x):
    graph[y][x] = 'X'
    for dy, dx in d:
        Y, X = y + dy, x + dx
        if (0 <= Y < m) and (0 <= X < n) and graph[Y][X] == '0':
            DFS(Y, X)

m, n = map(int, input().split())
graph = []
d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # (1, 0)은 없어도 됨, 전류가 위로 다시 흐르지 않기 때문

for _ in range(m):
    graph.append(list(input()))

for i in range(n):
    if graph[0][i] == '0':
        DFS(0, i)

if 'X' in graph[m - 1]:
    print('YES')
else:
    print('NO')
