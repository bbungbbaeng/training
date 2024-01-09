n = int(input())
texts = dict()

for i in range(n):
    text = input()
    texts[text] = len(text)

texts = sorted(texts.items(), key = lambda x: (x[1], x[0]))
for i in texts:
    print(i[0])
