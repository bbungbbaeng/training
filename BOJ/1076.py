color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multi = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

rst = []
for i in range(3):
    rst.append(input())

res = []
for i in range(len(rst)):
    if i < 2:
        res.append(value[color.index(rst[i])])
    else:
        res.append(multi[color.index(rst[i])])

print(int(str(res[0]) + str(res[1])) * res[-1])
