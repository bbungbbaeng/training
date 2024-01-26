nums = []

import sys
input = sys.stdin.readline

while 1:
    temp = list(input().split())
    nums.extend(temp)

    if len(nums) == int(nums[0]) + 1:
        break

del nums[0]

for i in range(len(nums)):
    nums[i] = int(nums[i][::-1])

for i in sorted(nums):
    print(i)
