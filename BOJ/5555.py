target = input()
n = int(input())
texts = [input() for i in range(n)]
cnt = 0

for i in texts:
    if target in (i + i + i):
        cnt += 1
print(cnt)
