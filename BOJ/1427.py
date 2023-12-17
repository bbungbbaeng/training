n = input()
nums = list(map(int, n))
nums.sort(reverse = True)

print(''.join(map(str, nums)))
