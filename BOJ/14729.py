import sys
input = sys.stdin.readline

n = int(input())
score = [float(input()) for _ in range(n)]

for i in sorted(score)[:7]:
    print(f'{i:.3f}')
