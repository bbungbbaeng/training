import sys
input = sys.stdin.readline

def dog(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n == 0:
    print(0)
else:
    nums = [int(input()) for i in range(n)]
    nums.sort()
    target = dog(n * 0.15)
    print(dog(sum(nums[target : n - target]) / len(nums[target : n - target])))
