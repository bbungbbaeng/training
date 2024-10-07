import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    i = 1
    while 1:
        if (y - x) in range(((i - 1) * (i - 1) + 1), ((i - 1) * (i) + 1)):
            print((i - 1) * 2)
            break
        elif (y - x) in range(((i - 1) * (i) + 1), ((i) * (i) + 1)):
            print((i - 1) * 2 + 1)
            break
        else:
            i += 1
