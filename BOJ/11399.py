n = int(input())
p = list(map(int, input().split()))

p.sort() # 최단 시간부터 계산해야하므로 오름차순으로 정렬
ans = list()
time = 0

for i in p:
  time += i # 시간의 순차적 합들을 time에 할당
  ans.append(time) # time의 값을 ans 리스트에 저장

print(sum(ans))
