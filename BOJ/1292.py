a, b = map(int, input().split())
cnt_a = 1
cnt_b = 1
sum = 0

while a > cnt_a:
    a -= cnt_a
    cnt_a += 1

while b > cnt_b:
    b -= cnt_b
    cnt_b += 1

for i in range(cnt_a, cnt_b + 1):
    if cnt_a == cnt_b:
        for j in range(a, b + 1):
            sum += i
    else:
        if i == cnt_a:
            for j in range(cnt_a - a + 1):
                sum += i
        elif i == cnt_b:
            for j in range(b):
                sum += i
        else:
            for j in range(i):
                sum += i
print(sum)
