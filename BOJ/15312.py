nums = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name1 = input()
name2 = input()
arr = []

for i in range(len(name1)):
    arr.append(nums[ord(name1[i]) - 65])
    arr.append(nums[ord(name2[i]) - 65])

temp = []

while len(arr) != 2:
    for i in range(1, len(arr)):
        temp.append((arr[i] + arr[i - 1]) % 10)

    arr = temp
    temp = []

print(f'{arr[0]}{arr[-1]}')
