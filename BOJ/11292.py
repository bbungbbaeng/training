while 1:
    n = int(input())
    if n == 0:
        break
    else:
        height = [input().split() for i in range(n)]
        height.sort(key = lambda x : -float(x[1]))
        for i in height:
            if i[1] == height[0][1]:
                print(i[0], end = ' ')
