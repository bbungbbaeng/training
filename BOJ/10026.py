import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS1(y, x):
    color1 = graph[y][x]
    graph[y][x] = '#'
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if (0 <= X < n) and (0 <= Y < n) and (graph[Y][X] == color1):
            DFS1(Y, X)

def DFS2(y, x):
    color2 = blind[y][x]
    blind[y][x] = '#'
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if (0 <= X < n) and (0 <= Y < n) and (blind[Y][X] == color2):
            DFS2(Y, X)

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
blind = [[0 for _ in range (n)] for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            blind[i][j] = 'G'
        else:
            blind[i][j] = graph[i][j]

cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != '#':
            DFS1(i, j)
            cnt1 += 1
        if blind[i][j] != '#':
            DFS2(i, j)
            cnt2 += 1
print(cnt1, cnt2)
