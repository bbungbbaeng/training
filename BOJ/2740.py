n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(m)]

mat3 = [[0 for _ in range(k)] for _ in range(n)]

for a in range(n):
    for b in range(k):
        temp = 0
        for c in range(m):
            temp += mat1[a][c] * mat2[c][b]
        mat3[a][b] = temp

for i in range(n):
    for j in range(k):
        print(mat3[i][j], end = ' ')
    print()
