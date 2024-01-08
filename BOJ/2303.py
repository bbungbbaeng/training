from itertools import combinations

n = int(input())
res = []
check = [i + 1 for i in range(n)]
for i in range(n):
  nums = list(map(int, input().split()))
  combi = [str(sum(i)) for i in list(combinations(nums, 3))]
  temp = [int(i[-1]) for i in combi]
  res.append(max(temp))

temp = []
for i in range(n):
  if res[i] == max(res):
    temp.append(i)
print(check[max(temp)])
