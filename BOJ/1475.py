import sys, math
input = sys.stdin.readline

nums = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
n = list(input().strip())

for i in n:
    if i == '9':
        nums['6'] += 1
    else:
        nums[i] += 1

if max(nums.values()) == nums['6']:
    nums['6'] = math.ceil(nums['6']/2)
    print(max(nums.values()))
else:
    print(max(nums.values()))
