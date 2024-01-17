n = int(input())
nums = set(list(map(int, input().split())))

for i in sorted(list(nums)):
    print(i, end = ' ')
