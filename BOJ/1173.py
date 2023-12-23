N, m, M, T, R = map(int, input().split())

exc = 0
rest = 0
x = m

if m + T > M:
    print(-1)
else:
    while exc < N:
        if x + T <= M:
            x += T
            exc += 1
        else:
            x = max(m, x - R)
            rest += 1
    print(exc + rest)
