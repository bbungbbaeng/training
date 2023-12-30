n = int(input())
cnt = 0
plus = 1
sum = 0

while 1:
    if sum + plus > n:
        print(cnt)
        break
    else:
        sum += plus
        plus += 1
        cnt += 1

  # 서로 다른 N개의 자연수의 합이 S일 때, N의 최댓값(자연수의 개수)을 구하는 문제
  # 1부터 하나씩 작은 수들을 더해가는 것이 최댓값이 나오게 하는 방법
  # 자연수의 합과는 상관 없이, 1부터 더한 자연수들의 합이 S 직전까지 도달했을 때가 N이 최댓값을 얻을 수 있음
  # ex)
  # S = 20 이라고 할 때, 1 + 2 + 3 + 4 + 5 = 15 
  # 여기서 6을 더하게 되면 21이 나오게 되므로, 합 20을 맞추려면 1을 빼고 6을 더하면 됨
  # 그래도 서로 다른 자연수의 개수는 5개로 동일
  # S가 더 큰 수여도 이는 동일
  # 최솟값인 1부터 수를 1씩 증가시켜 합을 더해나갔기 때문에, S 직전까지만 자연수들의 합을 구해놓으면 그 자연수들의 개수가 바로 최댓값인 것