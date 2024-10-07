import sys
input = sys.stdin.readline

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

n = int(input())
nums = [int(input()) for _ in range(n)]
subtract_nums = []

for i in range(len(nums) - 1):
    subtract_nums.append(nums[i + 1] - nums[i])

gcd_num = subtract_nums[0]
for i in subtract_nums:
    gcd_num = gcd(gcd_num, i)

cnt = 0
for i in subtract_nums:
    cnt += i / gcd_num
    cnt -= 1

print(int(cnt))
