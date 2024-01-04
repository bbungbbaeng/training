import math
import sys
input = sys.stdin.readline

n = int(input())
array = []
nums = dict()

for _ in range(n):
    num = int(input())
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1
    array.append(num)

nums = [k for k, v in nums.items() if v == max(nums.values())]

print(math.floor(sum(array) / n + 0.5))
print(sorted(array)[n // 2])
if len(sorted(nums)) > 1:
    print(sorted(nums)[1])
else:
    print(sorted(nums)[0])
print(abs(max(array) - min(array)))
