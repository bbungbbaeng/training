matrix = [[0] * 100 for _ in range(100)]

n = int(input())
cnt = 0

for i in range(n):
  x, y = map(int, input().split())

  for j in range(x-1, x + 9): 
    for k in range(y-1, y + 9):
      if matrix[j][k] == 0:
        matrix[j][k] = 1
        cnt += 1

# 100 by 100의 행렬에서 좌표가 주어졌을 때, 10 by 10의 크기의 영역을 1로 표시, 배열이 0일 때만 카운트하면 중복된 넓이를 제외하고 구할 수 있음

print(cnt)
