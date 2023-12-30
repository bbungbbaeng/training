import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    graph[y][x] = 'X' # 방문 표시
    for dx, dy in d:
        Y, X = y + dy, x + dx
        if (0 <= Y < h) and (0 <= X < w) and graph[Y][X] == '#': # (y, x)에서 상하좌우에 해당하는 위치의 원소가 '#'라면
            DFS(Y, X) # 재귀하여 연결된 양 무리를 모두 방문 표시함

t = int(input())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(t):
    h, w = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(input()))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#': # 그래프 안의 원소가 '#'라면
                DFS(i, j) # DFS 실행
                cnt += 1 # 카운트
    print(cnt)
