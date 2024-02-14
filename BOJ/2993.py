text = input()
res = text
for i in range(1, len(text)):
    for j in range(i + 1, len(text)):
        res = min(res, text[:i][::-1] + text[i:j][::-1] + text[j:][::-1])
print(res)
