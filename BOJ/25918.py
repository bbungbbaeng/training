n = int(input())
s = input()

nums = []

for i in s:
    if i == '(':
        nums.append(1)
    else:
        nums.append(-1)

cnt = []

if sum(nums) != 0:
    print(-1)
else:
    sum_nums = 0
    for i in nums:
        sum_nums += i
        cnt.append(abs(sum_nums))
    print(max(cnt))
