string1 = input()
string2 = input()

len1, len2 = len(string1), len(string2)

if string1 * len2 == string2 * len1:
    print(1)
else:
    print(0)
