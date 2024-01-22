import sys
input = sys.stdin.readline

n = int(input())
ext = dict()

for _ in range(n):
    file =  input().strip().split('.')[1]
    if not file in ext:
        ext[file] = 1
    else:
        ext[file] += 1

ext = sorted(ext.items())

for k, v in ext:
    print(k, v)
