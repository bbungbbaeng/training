# N개의 나라가 모두 연결되어 있다면, 모든 나라를 방문하는 최소의 수는 N-1이다

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n - 1)
