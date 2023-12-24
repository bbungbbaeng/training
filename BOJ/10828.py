import sys
input = sys.stdin.readline # 시간 제한이 촉박한 문제에서 절대 sys.stdin.readline을 쓰지 마

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
            print(stack.pop()) # pop() = 스택에서 맨 마지막 수를 리턴하고 해당 원소를 삭제
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
