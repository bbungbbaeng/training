import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    global v, o
    if graph[y][x] != '#': # 해당 위치에 울타리가 없으면
        if graph[y][x] == 'v': # 해당 위치에 있는 것이 늑대라면
            v += 1 # 늑대 수 카운트
        elif graph[y][x] == 'o': # 해당 위치에 있는 것이 양이라면
            o += 1 # 양 수 카운트
        graph[y][x] = '#' # 방문 표시
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (0 <= X < c) and (0 <= Y < r):
                DFS(Y, X)

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
v, o = 0, 0 # 각각의 울타리마다 존재하는 양과 늑대의 수
wolves, sheep = 0, 0 # 최종적으로 살아남는 양과 늑대의 수

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#': # 해당 위치에 울타리가 없으면
            DFS(i, j) # 깊이 탐색 실행
            if v >= o: # 울타리 안의 늑대의 수가 양의 수보다 같거나 많으면
                wolves += v # 늑대 승리
            else: # 울타리 안의 양의 수가 늑대의 수보다 많으면
                sheep += o # 양 승리
            v, o = 0, 0 # 늑대와 양 수 초기화
print(sheep, wolves)
