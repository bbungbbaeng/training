import sys
input = sys.stdin.readline

# 'add 1'에서 '1'을 문자열로 취급할 경우 시간초과가 나게 됨
# 1을 정수형으로 반환해서 진행하면 시간초과가 나지 않음
# 빠른 입출력에서는 정수형이 더 시간복잡도에 있어 유리한가?

m = int(input())
s = set()
for i in range(m):
    cmd = input().split()

    if 'add' == cmd[0]:
        s.add(int(cmd[-1]))
    elif 'remove' == cmd[0]:
        if int(cmd[-1]) in s:
            s.remove(int(cmd[-1]))
        else:
            pass
    elif 'check' == cmd[0]:
        if int(cmd[-1]) in s:
            print(1)
        else:
            print(0)
    elif 'toggle' == cmd[0]:
        if int(cmd[-1]) in s:
            s.remove(int(cmd[-1]))
        else:
            s.add(int(cmd[-1]))
    elif 'all' == cmd[0]:
        s = set([i for i in range(1, 21)])
    elif 'empty' == cmd[0]:
        s = set()
