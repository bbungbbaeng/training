year = [1, 1, 1]
target = list(map(int, input().split()))
cnt = 1

while 1:
    if year == target:
        break
    year[0] += 1
    year[1] += 1
    year[2] += 1
    cnt += 1
    if year[0] > 15:
        year[0] = 1
    if year[1] > 28:
        year[1] = 1
    if year[2] > 19:
        year[2] = 1

print(cnt)
