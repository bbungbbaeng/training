import sys
input = sys.stdin.readline

a = int(input())
n = set(map(int, input().split()))
b = int(input())
m = list(map(int, input().split()))

for i in m:
    if i in n:
        print(1)
    else:
        print(0)

# list에서 in의 동작은 O(N)만큼 걸리는 반면, set에서 in의 동작은 O(1)의 시간복잡도를 가짐
