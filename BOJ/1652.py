n = int(input())
graph = [input() for _ in range(n)]
row, col = [], []

for i in range(n):
    cnt = 0
    bed = []
    for j in range(n):
        if 0 <= j < n - 1:
            if graph[i][j] == '.':
                cnt += 1
                if graph[i][j + 1] == 'X':
                    if cnt > 1:
                        bed.append(cnt)
                        cnt = 0
                    else:
                        cnt = 0
        elif j == n - 1:
            if graph[i][j] == '.':
                cnt += 1
                if cnt > 1:
                    bed.append(cnt)
    if bed:
        for i in bed:
            row.append(i)

for i in range(n):
    cnt = 0
    bed = []
    for j in range(n):
        if 0 <= j < n - 1:
            if graph[j][i] == '.':
                cnt += 1
                if graph[j + 1][i] == 'X':
                    if cnt > 1:
                        bed.append(cnt)
                        cnt = 0
                    else:
                        cnt = 0
        elif j == n - 1:
            if graph[j][i] == '.':
                cnt += 1
                if cnt > 1:
                    bed.append(cnt)
    if bed:
        for i in bed:
            col.append(i)

print(len(row), len(col))
