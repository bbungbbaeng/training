t = int(input())
for _ in range(t):
    s, p = input().split()
    if p in s:
        print(len(s.replace(p, '-')))
    else:
        print(len(s))
