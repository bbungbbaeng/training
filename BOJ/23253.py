import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = True

for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    if k != sorted(k, reverse = True):
        check = False

if check == True:
    print('Yes')
else:
    print('No')
