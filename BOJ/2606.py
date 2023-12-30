n = int(input())
m = int(input())
graph = list([] for _ in range(n + 1))

# 0부터 n까지를 나타내는 리스트를 생성

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 입력받은 두 수는 서로 연결되어 있는 상태
# 해당 두 수를 각각의 리스트에 추가함으로써 연결 상태를 표현

visited = [False] * (n + 1)
cnt = -1

# 1번 컴퓨터는 이미 바이러스에 감염된 상태이므로 cnt를 -1로 해줌
# 나머지 감염된 컴퓨터의 수를 얻을 수 있음

def DFS(v):
    visited[v] = True
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

# 깊이 탐색 알고리즘
# 1부터 방문을 시작해서, 방문하면 cnt를 증가시킴
# v에 해당하는 리스트의 원소들 중에서, 방문하지 않은 원소가 있다면 깊이 탐색을 실시
# 따라서 연결된 원소들만 탐색하여 그 수를 알아낼 수 있음

DFS(1)
print(cnt)
