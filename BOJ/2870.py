import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]
nums = []

for i in board:
    temp = ''
    check = False
    for j in range(len(i)):
        if i[j].isdigit():
            temp += i[j]
            check = True
        else:
            if check:
                nums.append(int(temp))
                temp = ''
                check = False
            else:
                pass
    if temp:
        nums.append(int(temp))
    else:
        pass

for i in sorted(nums):
    print(i)
