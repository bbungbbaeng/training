n, k = map(int, input().split())
array = list()
cnt = 0

for i in range(n):
  array.append(int(input()))

array.sort(reverse = True)
# 동전의 크기 순서대로 내림차순 정렬

for coin in array:
  cnt += k // coin # 큰 동전으로 나눈 몫을 cnt에 할당
  k %= coin # 큰 동전으로 나누고 남은 나머지를 다시 k에 할당

print(cnt)
