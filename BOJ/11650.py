n = int(input())
nums = list()

for _ in range(n):
  a, b = map(int, input().split())
  nums.append([a, b])

nums.sort()

for i in range(len(nums)):
  print(nums[i][0], nums[i][1])
