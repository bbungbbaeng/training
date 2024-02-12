n, d = map(int, input().split())
nums = [str(i) for i in range(1, n + 1)]
cnt = 0

for i in nums:
    for j in range(len(i)):
        if str(d) in i[j]:
            cnt += 1
print(cnt)
