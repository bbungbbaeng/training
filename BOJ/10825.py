n = int(input())
students = [list(input().split()) for _ in range(n)]
students = sorted(students, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
    print(i[0])
