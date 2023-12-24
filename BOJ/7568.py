n = int(input())
height = []
weight = []
rank = []

for i in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)

for i in range(len(height)):
    for j in range(i, i + 1):
        cnt = 1
        dup = 0
        for a in range(len(height)):
            for b in range(a, a + 1):
                if height[i] > height[a] and weight[j] > weight[b]:
                    pass
                else:
                    if height[i] < height[a] and weight[j] < weight[b]:
                        dup += 1
                    else:
                        pass
        rank.append(cnt + dup)

for i in rank:
    print(i, end = ' ')
