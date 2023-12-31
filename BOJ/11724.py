import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline # 입력을 많이 받는 문제는 sys.stdin.readlin으로 받아야 시간초과가 안남

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1
print(cnt)
