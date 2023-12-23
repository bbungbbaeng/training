n, m = map(int, input().split())
castle = []
# 경비원이 없는 행과 열의 갯수 중에 가장 큰 수를 출력하면 되는 문제 (경비원이 없는 행과 열의 갯수는 서로 중복될 수 밖에 없기 때문에, 큰 수만큼 경비원을 채워주면 모든 행과 열에 경비원이 존재하게 됨)
row = 0 # 행
col = 0 # 열

for i in range(n):
    temp = input()
    castle.append(temp)

    if 'X' not in temp: # 경비원이 없는 행의 갯수를 저장
        row += 1

for i in range(m):
    cnt = 0
    for j in range(n): # for문에서 n에 해당하는 변수인 j가 밑에 가도록 두면, 행렬의 열 부분을 파악할 수 있음 ([0][0] -> [1][0] -> [2][0] ...)
        if castle[j][i] == 'X': # 열 부분에서 경비원이 1명이라도 있다면, 해당 열에 대한 반복문을 종료
            break
        else: # 열 부분에 경비원이 없을 경우, 카운트 증가
            cnt += 1
    if cnt == n: # 카운트의 수가 열의 수(n)과 같다면, 경비원이 없는 열이므로 해당 경우를 저장
        col += 1

print(max(row, col)) # 행과 열의 갯수 중 큰 것을 출력
