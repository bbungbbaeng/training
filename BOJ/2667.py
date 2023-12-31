import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(input()) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
house = []
cnt = 0

def DFS(y, x):
    graph[y][x] = 'X'
    global cnt
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < n) and (0 <= Y < n) and (graph[Y][X] == '1'):
            DFS(Y, X)
            cnt += 1

block = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            DFS(i, j)
            block += 1
            house.append(cnt + 1) # 맨 처음 DFS가 실행될 때, graph[i][j]를 'X'로 설정하고 들어가므로 카운트가 1이 덜 세어지게 됨, 그러므로 1을 더해서 수를 맞춰 줌
            cnt = 0
print(block)
for i in sorted(house):
    print(i)
