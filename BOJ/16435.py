n, l = map(int, input().split())
nums = list(map(int, input().split()))

for i in sorted(nums):
    if l >= i:
        l += 1
    else:
        break
print(l)
