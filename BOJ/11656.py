s = input()
texts = [s[i:] for i in range(len(s))]
print('\n'.join(sorted(texts)))
