word = list(input())
ans = []
temp = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp.append(a + b + c)

for a in temp:
    ans.append(''.join(a))

print(sorted(ans)[0])
