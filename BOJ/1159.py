n = int(input())
names = []
res = set()

for _ in range(n):
    name = input()
    names.append(name[:1])

for i in range(len(names)):
    if names.count(names[i]) >= 5:
        res.add(names[i])
    else:
        pass

if len(res) == 0:
    print('PREDAJA')
else:
    print(''.join(sorted(res)))
