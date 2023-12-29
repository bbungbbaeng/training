cnt = 0
while 1:
    l, p, v = map(int, input().split())
    cnt += 1
    
    if l == 0 and p == 0 and v == 0:
        break
    else:
        if v % p <= l:
            print(f'Case {cnt}: {(v // p) * l + (v % p)}')
        else:
            print(f'Case {cnt}: {(v // p) * l + l}')
