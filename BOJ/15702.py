n, m = map(int, input().split())
score = list(map(int, input().split()))
students = []

for _ in range(m):
    sum = 0
    student = list(input().split())
    for i in range(1, len(student)):
        if student[i] == 'O':
            sum += score[i - 1]
    students.append((int(student[0]), sum))

print(sorted(students, key = lambda x : (-x[1], x[0]))[0][0], sorted(students, key = lambda x : (-x[1], x[0]))[0][1])
