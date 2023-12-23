n = int(input())
text = []
res = []
length = 0

for _ in range(n):
    a = input()
    text.append(a)
    length = len(a)

for i in range(len(text) - 1):
    for j in range(length):
        if i == 0:
            if text[i][j] == text[i+1][j]:
                res.append(text[i][j])
            else:
                res.append('?')
        elif i > 0:
            if text[i][j] == text[i+1][j]:
                pass
            else:
                res[j] = '?'

if len(res) == 0:
    print(''.join(text))
else:
    print(''.join(res))
