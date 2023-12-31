import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    tv[y][x] = 0
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if (0 <= X < m) and (0 <= Y < n) and (tv[Y][X] == 255):
            DFS(Y, X)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tv = [[0 for _ in range(m)] for _ in range(n)]
t = int(input())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        if (graph[i][3 * j] + graph[i][3 * j + 1] + graph[i][3 * j + 2]) / 3 >= t: # R, G, B 값이 각각 3개씩 배치되어 있으므로 3의 배수대로 리스트의 원소들을 끊어줌
            tv[i][j] = 255
        else:
            tv[i][j] = 0

cnt = 0
for i in range(n):
    for j in range(m):
        if tv[i][j] == 255:
            DFS(i, j)
            cnt += 1
print(cnt)
