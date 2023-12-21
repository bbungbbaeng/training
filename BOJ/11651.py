n = int(input())
nums = list()

for _ in range(n):
  x, y = map(int, input().split())
  nums.append([x, y])

for i in range(len(nums)):
  nums[i].reverse()

nums.sort()

for i in range(len(nums)):
  print(nums[i][1], nums[i][0])
