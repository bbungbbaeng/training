horse = []
for _ in range(4):
    horse.append('F.F.F.F.')
    horse.append('.F.F.F.F')

chess = []
cnt = 0
for i in range(8):
    chess.append(input())

for i in range(8):
    for j in range(8):
        if chess[i][j] == horse[i][j] == 'F':
            cnt += 1
        else:
            pass
print(cnt)
