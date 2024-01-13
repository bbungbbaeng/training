nums = [(int(input()), i + 1) for i in range(8)]
s, id = [], []

for i in range(5):
    s.append(sorted(nums, key = lambda x : -x[0])[i][0])
    id.append(str(sorted(nums, key = lambda x : -x[0])[i][1]))

print(sum(s))
print(' '.join(sorted(id)))
