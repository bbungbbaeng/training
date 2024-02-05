n = int(input())
node = list(map(int, input().split()))
num = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    if node[i] != -1:
        if i != num:
            graph[node[i]].append(i)

def DFS(a):
    while graph[a]:
        x = graph[a].pop()
        DFS(x)
    graph[a].append(False)

DFS(num)
cnt = 0

for i in range(n):
    if not graph[i]:
        cnt += 1
print(cnt)
