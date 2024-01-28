text = input()
n = input()
cnt, a = 0, 0

for i in range(len(text)):
    if n in text[a:]:
        a += (text[a:].index(n) + len(n))
        cnt += 1
    elif n not in text[a:]:
        break

print(cnt)
