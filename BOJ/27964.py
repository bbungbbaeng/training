n = int(input())
toping = list(input().split())
cheese = []

for i in toping:
    if not i.find('Cheese') == -1:
        if not i.find('Cheese', len(i) - 6) == -1:
            cheese.append(i)

if len(set(cheese)) >= 4:
    print('yummy')
else:
    print('sad')
