text = []
for _ in range(5):
    a = list(input())
    if len(a) == 15:
        text.append(a)
    else:
        for _ in range(15 - len(a)):
            a.append('?')
        text.append(a)

for i in range(15):
    for j in range(5):
        if text[j][i] == '?':
            pass
        else:
            print(text[j][i], end = '')
