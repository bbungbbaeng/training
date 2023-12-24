n = int(input())
line = 1

# 대각선의 방향에 따라 정리
# line 1: 1/1
# line 2 : 1/2, 2/1 -> 분자 증가 / 분모 감소
# line 3 : 3/1, 2/2, 1/3 -> 분자 감소 / 분모 증가
# line 4 : 1/4, 2/3, 3/2, 4/1 -> 분자 증가 / 분모 감소

while n > line: # 주어진 n의 값이 어느 line에 위치한 값인지를 찾아야 함
    n -= line # n의 값에서 line을 빼주고, line에 1씩 더하는 과정을 반복하면 해당 n이 어느 line에 위치한 값인지를 알 수 있음
    line += 1 # 이 과정을 통해 얻은 n은 분모 또는 분자를 나타냄

# ex)
# n = 4일 때, while 문을 통해 얻게 되는 값들은 n = 1, line = 3
# n = 5일 때, while 문을 통해 얻게 되는 값들은 n = 2, line = 3
# n = 6일 때, while 문을 통해 얻게 되는 값들은 n = 3, line = 3
# line 3은 n이 증가할 수록 분모가 증가하기 때문에, n은 분모를 나타냄
# line에서 n을 빼주고, 1을 더해주면 분자 값 또한 얻을 수 있음

if line % 2 == 0: # line이 짝수일 때
    a = n # n은 분자를 나타냄
    b = line - n + 1 # (line - n + 1)값은 분모를 나타냄
else: # line이 홀수일 때
    a = line - n + 1 # (line - n + 1)값은 분자를 나타냄
    b = n # n은 분모를 나타냄

print(f'{a}/{b}')
