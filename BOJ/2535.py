n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
students = sorted(students, key = lambda x : -x[2])
check = []
cnt = 0

for i in students:
    if check.count(i[0]) < 2:
        print(i[0], i[1])
        check.append(students[0][0])
        cnt += 1
    else:
        pass

    if cnt == 3:
        break
