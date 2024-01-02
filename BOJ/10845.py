from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        d.append(cmd[-1])
    elif cmd[0] == 'pop':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
