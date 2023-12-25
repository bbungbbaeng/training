from itertools import combinations
heights = []

for _ in range(9):
    heights.append(int(input()))

arr = list(combinations(heights, 7))
res = []

for i in range(len(arr)):
    sum = 0
    for j in range(7):
        sum += arr[i][j]

    if sum == 100:
        res.append(arr[i])
    else:
        pass

for i in sorted(res[0]):
    print(i)
