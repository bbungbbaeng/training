k = int(input())

for i in range(k):
    grade = list(map(int, input().split()))
    del grade[0]
    res = [abs(sorted(grade)[j] - sorted(grade)[j + 1]) for j in range(len(grade)) if 0 <= j < len(grade) - 1]
    print(f'Class {i + 1}')
    print(f'Max {max(grade)}, Min {min(grade)}, Largest gap {max(res)}')
