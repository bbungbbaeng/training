import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    cmd = input().split()
    
    if 'push' in cmd[0]:
        stack.append(cmd[-1])
    elif 'pop' in cmd[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in cmd[0]:
        print(len(stack))
    elif 'empty' in cmd[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in cmd[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
