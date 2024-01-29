import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

while len(nums) > 0:
    temp = set(sorted(nums))
    for i in temp:
        del nums[nums.index(i)]
    cnt += 1

print(cnt)
