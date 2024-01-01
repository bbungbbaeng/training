import sys
sys.setrecursionlimit(10 ** 6)

def DFS(y, x):
    if graph[y][x] == '1':
        global sum
        sum += 1
        graph[y][x] = '#'
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (0 <= X < m) and (0 <= Y < n):
                DFS(Y, X)

n, m = map(int, input().split())
graph = [list(input().split()) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
res = []
sum = 0

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            DFS(i, j)
            cnt += 1
            res.append(sum)
            sum = 0

print(cnt)
if not res: # 입력이 n = 1, m = 1, graph =[[0]]일 경우, res 리스트가 비어있게 됨
    print(0) # 비어있는 리스트에 max를 쓰면 런타임 에러(Value Error)가 발생하므로, 이를 체크하는 것이 중요함
else:
    print(max(res))
