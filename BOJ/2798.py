n, m = map(int, input().split())
nums = list(map(int, input().split()))

case = dict()

for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    for k in range(j+1, len(nums)):
      if m < nums[i]+nums[j]+nums[k]:
        continue
      else:
        case[m-(nums[i]+nums[j]+nums[k])] = nums[i]+nums[j]+nums[k]


print(case[min(case.keys())])
