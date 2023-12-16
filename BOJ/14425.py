n, m = map(int, input().split())
s = set()
text = list()
cnt = 0

for i in range(n + m):
  if i <= n - 1:
    s.add(input())
  else:
    text.append(input())

for i in text: # 문자열이 집합 s에 포함되면 카운트
  if i in s:
    cnt += 1

print(cnt)
