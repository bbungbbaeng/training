n = int(input())
nums = list()

for _ in range(n):
  nums.append(int(input()))

nums.sort(reverse=True)

nums_max = list()
nums_min = list()
nums_minus = list()
flag = False

for i in nums:
  if not flag:
    if i == 1 or i == 0 or i < 0:
      nums_min = nums[nums.index(i):]
      nums_max = nums[:nums.index(i)]
      flag = True
    else:
      nums_max.append(i)
  else:
    continue

flag = False

for i in nums_min:
  if not flag:
    if i < 0:
      nums_minus = nums_min[nums_min.index(i):]
      nums_min = nums_min[:nums_min.index(i)]
      flag = True
  else:
    continue

nums_minus.sort()

sum = 0
temp = 0
cnt = 0

if len(nums_max) % 2 == 1:
  sum += nums_max[-1]
  del nums_max[-1]

for i in range(len(nums_max)):
  if i % 2 == 0:
      temp += nums_max[i]
      cnt += 1
  elif i % 2 == 1:
      temp *= nums_max[i]
      cnt += 1
  if cnt > 1:
      sum += temp
      temp = 0
      cnt = 0

for i in range(len(nums_min)):
  sum += nums_min[i]

if (0 in nums_min) and (len(nums_minus)%2 == 1):
  del nums_minus[-1]

temp = 0
cnt = 0

if len(nums_minus) % 2 == 1:
  sum += nums_minus[-1]
  del nums_minus[-1]

for i in range(len(nums_minus)):
  if i % 2 == 0:
    temp += abs(nums_minus[i])
    cnt += 1
  elif i % 2 == 1:
    temp *= abs(nums_minus[i])
    cnt += 1

  if cnt > 1:
    sum += temp
    temp = 0
    cnt = 0

print(sum)
