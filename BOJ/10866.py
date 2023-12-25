import sys
input = sys.stdin.readline

# 이 문제는 from collections import deque로 불러올 수 있는 덱 클래스로도 풀 수 있음
# 파이썬에서 덱은 스택과 큐의 연산을 모두 지원하고, 양 끝에서 삽입(appendleft)과 삭제(popleft)를 할 수 있음
# 단순히 값을 삽입하고 삭제하는 용도로 활용할 때는 O(1)만큼의 시간 복잡도를 소모함.

deque = []
n = int(input())
for _ in range(n):
    cmd = list(input().split())

    if 'push_front' == cmd[0]:
        deque.append(cmd[-1])
    elif 'push_back' == cmd[0]:
        deque.insert(0, cmd[-1])
    elif 'pop_front' == cmd[0]:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif 'pop_back' == cmd[0]:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif 'size' == cmd[0]:
        print(len(deque))
    elif 'empty' == cmd[0]:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == cmd[0]:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    elif 'back' == cmd[0]:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
