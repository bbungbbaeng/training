n = int(input())
cnt = 0
num = 666
temp = 0

while 1:
  temp = num

  while (temp != 0):
    if temp % 1000 == 666: # 1000으로 나눴을 때의 나머지가 666이면 종말의 수
      cnt += 1
      break
    temp //= 10 # 나머지가 666이 아닐 경우, 10으로 나눠주어 자릿수를 하나 낮춰본다

  if cnt == n:
    print(num)
    break

  num += 1
