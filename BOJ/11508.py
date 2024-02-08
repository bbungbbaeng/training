import sys
input = sys.stdin.readline

n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse = True)
sum = 0

for i in range(1, len(price) + 1):
    if i % 3 == 0:
        pass
    else:
        sum += price[i - 1]

print(sum)
