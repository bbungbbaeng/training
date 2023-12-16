a, b = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

symset = ((set1 | set2) - (set1 & set2)) # 대칭차집합 공식

print(len(symset))
