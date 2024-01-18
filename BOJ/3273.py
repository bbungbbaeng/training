n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
left, right = 0, len(nums) - 1
cnt = 0

while left < right:
    sum_nums = nums[left] + nums[right]
    if sum_nums < x:
        left += 1
    elif sum_nums > x:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)
