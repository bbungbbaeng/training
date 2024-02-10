import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().strip() for i in range(n)]
res = []
sum = 0

for j in range(m):
    check = dict()
    for i in range(n):
        if dna[i][j] not in check:
            check[dna[i][j]] = 1
        else:
            check[dna[i][j]] += 1
    
    check = sorted(check.items(), key = lambda x : (-x[1], x[0]))
    res.append(check[0][0])

    for k, v in check[1:]:
        sum += v

print(''.join(res))
print(sum)
