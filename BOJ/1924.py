week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
nums = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = 0

x, y = map(int, input().split())

for i in range(x):
    if x == 1:
        num += y
    else:
        if 0 <= i < x - 1:
            num += nums[i]
        elif i == x - 1:
            num += y

if x == 1:
    print(week[num % 7 - 1])
else:
    print(week[num % 7])
