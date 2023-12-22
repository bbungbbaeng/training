n, m = map(int, input().split())
chess = []
cnt = []

for _ in range(n):
  chess.append(input())

for x in range(n - 7):
  for y in range(m - 7):
    b_count = 0 # (0, 0)이 검은색(B)로 시작하는 경우
    w_count = 0 # (0, 0)이 흰색(W)로 시작하는 경우

    for a in range(x, x + 8):
      for b in range(y, y + 8):

        if (a + b) % 2 == 0: # a와 b의 합이 짝수인 경우, (0, 0)과 [a][b] 위치의 색깔이 같아야 함
          if chess[a][b] != 'W': # (0, 0)이 W인 경우
            w_count += 1 # 해당 위치의 색깔이 같지 않다면 같은 색을 칠해줘야 하므로 카운트
          else: # (0, 0)이 B인 경우
            b_count += 1 # 해당 위치의 색깔이 같지 않다면 같은 색을 칠해줘야 하므로 카운트

        else: # a와 b의 합이 홀수인 경우, (0, 0)과 [a][b] 위치의 색깔이 달라야 함
          if chess[a][b] != 'W': # (0, 0)이 B일 때
            b_count += 1 # 색깔이 달라야하므로 다른 색을 칠해줘야 함
          else: # (0, 0)이 W일 때
            w_count += 1 # 색깔이 달라야하므로 다른 색을 칠해줘야 함

    cnt.append(b_count)
    cnt.append(w_count)
print(min(cnt))
