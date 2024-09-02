num = int(input())

for i in range(2, num):
    num *= i

cnt = 0
if num == 0:
    print(0)
else:
    for i in str(num)[::-1]:
        if i == '0':
            cnt += 1
        else:
            break
    print(cnt)
