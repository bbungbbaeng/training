n = int(input())

for _ in range(n):
    text = list(input().split())
    for i in range(len(text)):
        text[i] = text[i][::-1]
    print(' '.join(text))
